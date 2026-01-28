import pandas as pd
import os
import re

file_input = "ESTUDIANTES.xlsx"
file_output = "ESTUDIANTES_CONSOLIDADO.xlsx"

def normalize_text(text):
    if not isinstance(text, str):
        return str(text) if pd.notna(text) else ""
    return text.strip().upper()


def find_header_row(df, keywords=["NOMBRE", "ALUMNO", "ESTUDIANTE"]):
    """Finds the index of the header row based on keywords."""
    for i in range(min(25, len(df))): # Scan more rows just in case
        row_values = [str(val).upper() for val in df.iloc[i].values]
        
        # Check if 'NOMBRE' is present (Primary Key for being a header)
        if any("NOMBRE" in v for v in row_values):
            return i
            
    # Fallback: If no "NOMBRE", look for "CORREO" AND "TELEFONO" together
    for i in range(min(25, len(df))):
        row_values = [str(val).upper() for val in df.iloc[i].values]
        has_email = any("CORREO" in v for v in row_values) or any("EMAIL" in v for v in row_values)
        has_phone = any("TELEFONO" in v for v in row_values) or any("TLÉFONO" in v for v in row_values)
        if has_email and has_phone:
             return i
             
    return None


def clean_phone(phone):
    if pd.isna(phone): return ""
    # Keep only digits, +, -
    return re.sub(r'[^\d\+\-\(\)\s]', '', str(phone)).strip()

def process_sheet(sheet_name, df):
    header_idx = find_header_row(df)
    if header_idx is None:
        print(f"Skipping {sheet_name}: No header found.")
        return None
    
    # Set header
    df.columns = df.iloc[header_idx]
    df = df.iloc[header_idx+1:].reset_index(drop=True)
    
    # Normalize columns
    df.columns = [str(c).upper().strip() for c in df.columns]
    
    # Identify target columns
    cols = df.columns
    col_map = {}
    
    # Mapping heuristics
    full_name_col = next((c for c in cols if "NOMBRE Y APELLIDO" in c), None)
    first_name_col = next((c for c in cols if c == "NOMBRE"), None)
    last_name_col = next((c for c in cols if c == "APELLIDO" or "APELLIDOS" in c), None)
    
    email_col = next((c for c in cols if "CORREO" in c or "EMAIL" in c), None)
    phone_col = next((c for c in cols if "TELEFONO" in c or "TLÉFONO" in c or "CELULAR" in c), None)
    cedula_col = next((c for c in cols if "CEDULA" in c or "CÉDULA" in c), None)
    program_col = next((c for c in cols if "CARRERA" in c or "PROGRAMA" in c), None)
    
    # Create standardized DataFrame
    new_data = pd.DataFrame()
    
    # Name handling
    if full_name_col:
        new_data["Nombre_Completo"] = df[full_name_col]
    elif first_name_col:
        if last_name_col:
            new_data["Nombre_Completo"] = df[first_name_col].astype(str) + " " + df[last_name_col].astype(str)
        else:
            new_data["Nombre_Completo"] = df[first_name_col]
    else:
        # Fallback for sheets like "DIPLOMADO..." that might have "NOMBRE" only
        potential_name = next((c for c in cols if "NOMBRE" in c), None)
        if potential_name:
             new_data["Nombre_Completo"] = df[potential_name]
        else:
             print(f"Skipping {sheet_name}: No Name column found in {cols}")
             return None

    # Other columns
    new_data["Email"] = df[email_col] if email_col else ""
    new_data["Telefono"] = df[phone_col] if phone_col else ""
    new_data["Cedula"] = df[cedula_col] if cedula_col else ""
    new_data["Programa_Original"] = df[program_col] if program_col else ""
    
    # Metadata
    new_data["Fuente_Hoja"] = sheet_name
    
    # Infer Status
    status = "Desconocido"
    sn_upper = sheet_name.upper()
    if "RETIRADO" in sn_upper: status = "Retirado"
    elif "GRADUADO" in sn_upper: status = "Graduado"
    elif "2025" in sn_upper or "2026" in sn_upper: status = "Activo/Futuro"
    elif "RESPALDO" in sn_upper or "2024" in sn_upper or "2023" in sn_upper: status = "Inactivo/Historico"
    else: status = "Activo"
    
    new_data["Estado_Inferido"] = status
    
    # Clean data
    new_data["Nombre_Completo"] = new_data["Nombre_Completo"].apply(normalize_text).replace("NAN NAN", "").replace("NAN", "")
    new_data["Email"] = new_data["Email"].astype(str).str.lower().replace("nan", "").str.strip()
    new_data["Telefono"] = new_data["Telefono"].apply(clean_phone)
    
    # Filter empty rows (no name)
    new_data = new_data[new_data["Nombre_Completo"].str.len() > 2]
    
    return new_data

# Main processing
try:
    xl = pd.ExcelFile(file_input)
    all_data = []
    
    print(f"Processing {len(xl.sheet_names)} sheets...")
    
    for sheet in xl.sheet_names:
        try:
            df = xl.parse(sheet)
            processed_df = process_sheet(sheet, df)
            if processed_df is not None and not processed_df.empty:
                all_data.append(processed_df)
                print(f"  + Added {len(processed_df)} records from {sheet}")
        except Exception as e:
            print(f"  - Error processing {sheet}: {e}")
            
    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        print(f"\nTotal records found: {len(final_df)}")
        
        # Deduplication (Simple check by Email if present, or Name)
        final_df["Duplicado"] = final_df.duplicated(subset=["Nombre_Completo", "Email"], keep="first")
        
        # Save
        final_df.to_excel(file_output, index=False)
        print(f"Successfully saved consolidated database to {file_output}")
    else:
        print("No valid data found to consolidate.")
        
except Exception as e:
    print(f"Fatal error: {e}")
