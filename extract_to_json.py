import pandas as pd
import json
from datetime import datetime
import hashlib

def generate_student_id(row):
    """Generate unique ID from student data"""
    unique_string = f"{row['Nombre_Completo']}_{row['Email']}_{row['Fuente_Hoja']}"
    return hashlib.md5(unique_string.encode()).hexdigest()[:12].upper()

def extract_year_from_source(source):
    """Extract year from source sheet name"""
    for year in ['2026', '2025', '2024', '2023', '2022']:
        if year in str(source):
            return int(year)
    return None

def normalize_program_name(program):
    """Normalize program names to standard format"""
    if pd.isna(program) or program == "":
        return "No especificado"
    
    program = str(program).upper().strip()
    
    # Mapping common variations
    if "COCINERO" in program and "PANADERO" in program and "PASTELERO" in program:
        return "Cocinero, Panadero y Pastelero Profesional"
    elif "PANADERO" in program and "PASTELERO" in program:
        return "Panadero y Pastelero Profesional"
    elif "COCINERO" in program:
        return "Cocinero Profesional"
    elif "DIPLOMADO" in program:
        return program.title()
    else:
        return program.title()

def extract_horario(source):
    """Extract schedule from source sheet name"""
    source_upper = str(source).upper()
    if "MAÑANA" in source_upper or "8 AM" in source_upper or "8AM" in source_upper:
        return "Mañana"
    elif "TARDE" in source_upper or "1 PM" in source_upper or "1PM" in source_upper:
        return "Tarde"
    elif "NOCHE" in source_upper or "6 PM" in source_upper or "6PM" in source_upper:
        return "Noche"
    else:
        return "No especificado"

def process_consolidated_database(input_file):
    """Process consolidated Excel and convert to JSON"""
    
    print(f"Reading consolidated database: {input_file}")
    df = pd.read_excel(input_file)
    
    print(f"Total records found: {len(df)}")
    
    # Filter out duplicates (keep first occurrence)
    df_clean = df[df['Duplicado'] == False].copy()
    print(f"Records after removing duplicates: {len(df_clean)}")
    
    # Build student records
    students = []
    
    for idx, row in df_clean.iterrows():
        student = {
            "id": generate_student_id(row),
            "nombre_completo": str(row['Nombre_Completo']).strip(),
            "email": str(row['Email']).lower().strip() if pd.notna(row['Email']) and row['Email'] != "" else None,
            "telefono": str(row['Telefono']).strip() if pd.notna(row['Telefono']) and row['Telefono'] != "" else None,
            "cedula": str(row['Cedula']).strip() if pd.notna(row['Cedula']) and row['Cedula'] != "" else None,
            "programa": normalize_program_name(row['Programa_Original']),
            "programa_original": str(row['Programa_Original']).strip() if pd.notna(row['Programa_Original']) else "No especificado",
            "estado": str(row['Estado_Inferido']),
            "año_ingreso": extract_year_from_source(row['Fuente_Hoja']),
            "horario": extract_horario(row['Fuente_Hoja']),
            "fuente_hoja": str(row['Fuente_Hoja']),
            "metadata": {
                "fecha_registro": datetime.now().strftime("%Y-%m-%d"),
                "indice_original": int(idx)
            }
        }
        
        students.append(student)
    
    # Generate statistics
    estados_count = df_clean['Estado_Inferido'].value_counts().to_dict()
    programas_count = df_clean['Programa_Original'].apply(normalize_program_name).value_counts().to_dict()
    
    # Build final JSON structure
    output_data = {
        "estudiantes": students,
        "metadata": {
            "total_estudiantes": len(students),
            "ultima_actualizacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "archivo_origen": input_file,
            "estadisticas": {
                "por_estado": estados_count,
                "por_programa": programas_count,
                "con_email": int(df_clean['Email'].notna().sum()),
                "con_telefono": int(df_clean['Telefono'].notna().sum()),
                "con_cedula": int(df_clean['Cedula'].notna().sum())
            }
        }
    }
    
    return output_data

def main():
    input_file = "ESTUDIANTES_CONSOLIDADO.xlsx"
    output_file = "estudiantes_database.json"
    
    try:
        # Process database
        data = process_consolidated_database(input_file)
        
        # Save to JSON
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Successfully created {output_file}")
        print(f"\nStatistics:")
        print(f"  - Total students: {data['metadata']['total_estudiantes']}")
        print(f"  - With email: {data['metadata']['estadisticas']['con_email']}")
        print(f"  - With phone: {data['metadata']['estadisticas']['con_telefono']}")
        print(f"\nBy status:")
        for estado, count in data['metadata']['estadisticas']['por_estado'].items():
            print(f"  - {estado}: {count}")
        
    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found.")
        print("Please run 'consolidate_database.py' first.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
