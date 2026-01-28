import pandas as pd
import re
from collections import defaultdict

def validate_email(email):
    """Validate email format"""
    if pd.isna(email) or email == "" or email == "nan":
        return False, "Email vacío"
    
    email = str(email).strip().lower()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True, "OK"
    else:
        return False, f"Formato inválido: {email}"

def validate_phone(phone):
    """Validate phone format (Dominican Republic)"""
    if pd.isna(phone) or phone == "" or phone == "nan":
        return False, "Teléfono vacío"
    
    phone = str(phone).strip()
    # Remove common separators
    phone_clean = re.sub(r'[\s\-\(\)]', '', phone)
    
    # Dominican phone patterns: 809/829/849 + 7 digits
    if re.match(r'^(809|829|849)\d{7}$', phone_clean):
        return True, "OK"
    elif re.match(r'^\d{10}$', phone_clean):
        return True, "OK (10 dígitos)"
    elif len(phone_clean) >= 7:
        return True, "OK (formato alternativo)"
    else:
        return False, f"Formato sospechoso: {phone}"

def validate_name(name):
    """Validate student name"""
    if pd.isna(name) or name == "" or name == "nan" or name == "NAN":
        return False, "Nombre vacío"
    
    name = str(name).strip()
    
    if len(name) < 3:
        return False, f"Nombre muy corto: {name}"
    
    if name.upper() == name and len(name) > 10:
        return True, "OK (mayúsculas)"
    
    return True, "OK"

def validate_program(program):
    """Validate program name against known programs"""
    known_programs = [
        "COCINERO PANADERO Y PASTELERO",
        "COCINERO, PANADERO Y PASTELERO",
        "PANADERO Y PASTELERO",
        "COCINERO PROFESIONAL",
        "PANADERO PROFESIONAL",
        "PASTELERO PROFESIONAL",
        "DIPLOMADO"
    ]
    
    if pd.isna(program) or program == "" or program == "nan":
        return False, "Programa vacío"
    
    program_upper = str(program).upper().strip()
    
    for known in known_programs:
        if known in program_upper:
            return True, "OK"
    
    return False, f"Programa desconocido: {program}"

def find_duplicates(df):
    """Find potential duplicate students"""
    duplicates = defaultdict(list)
    
    # Check by email
    email_groups = df[df['Email'].notna() & (df['Email'] != "")].groupby('Email')
    for email, group in email_groups:
        if len(group) > 1:
            duplicates['email'].append({
                'value': email,
                'count': len(group),
                'students': group['Nombre_Completo'].tolist()
            })
    
    # Check by phone
    phone_groups = df[df['Telefono'].notna() & (df['Telefono'] != "")].groupby('Telefono')
    for phone, group in phone_groups:
        if len(group) > 1:
            duplicates['phone'].append({
                'value': phone,
                'count': len(group),
                'students': group['Nombre_Completo'].tolist()
            })
    
    # Check by cedula
    cedula_groups = df[df['Cedula'].notna() & (df['Cedula'] != "")].groupby('Cedula')
    for cedula, group in cedula_groups:
        if len(group) > 1:
            duplicates['cedula'].append({
                'value': cedula,
                'count': len(group),
                'students': group['Nombre_Completo'].tolist()
            })
    
    return duplicates

def validate_consolidated_database(input_file):
    """Validate consolidated database"""
    
    print(f"📊 Validating database: {input_file}\n")
    
    df = pd.read_excel(input_file)
    total_records = len(df)
    
    print(f"Total records: {total_records}\n")
    
    # Validation results
    validation_results = {
        'emails': {'valid': 0, 'invalid': 0, 'errors': []},
        'phones': {'valid': 0, 'invalid': 0, 'errors': []},
        'names': {'valid': 0, 'invalid': 0, 'errors': []},
        'programs': {'valid': 0, 'invalid': 0, 'errors': []}
    }
    
    # Validate each record
    for idx, row in df.iterrows():
        # Validate email
        is_valid, msg = validate_email(row['Email'])
        if is_valid:
            validation_results['emails']['valid'] += 1
        else:
            validation_results['emails']['invalid'] += 1
            if len(validation_results['emails']['errors']) < 10:  # Limit errors shown
                validation_results['emails']['errors'].append(f"Row {idx}: {msg}")
        
        # Validate phone
        is_valid, msg = validate_phone(row['Telefono'])
        if is_valid:
            validation_results['phones']['valid'] += 1
        else:
            validation_results['phones']['invalid'] += 1
            if len(validation_results['phones']['errors']) < 10:
                validation_results['phones']['errors'].append(f"Row {idx}: {msg}")
        
        # Validate name
        is_valid, msg = validate_name(row['Nombre_Completo'])
        if is_valid:
            validation_results['names']['valid'] += 1
        else:
            validation_results['names']['invalid'] += 1
            if len(validation_results['names']['errors']) < 10:
                validation_results['names']['errors'].append(f"Row {idx}: {msg}")
        
        # Validate program
        is_valid, msg = validate_program(row['Programa_Original'])
        if is_valid:
            validation_results['programs']['valid'] += 1
        else:
            validation_results['programs']['invalid'] += 1
            if len(validation_results['programs']['errors']) < 10:
                validation_results['programs']['errors'].append(f"Row {idx}: {msg}")
    
    # Print validation results
    print("=" * 60)
    print("VALIDATION RESULTS")
    print("=" * 60)
    
    for field, results in validation_results.items():
        print(f"\n{field.upper()}:")
        print(f"  ✅ Valid: {results['valid']}")
        print(f"  ❌ Invalid: {results['invalid']}")
        
        if results['errors']:
            print(f"  Sample errors (showing {len(results['errors'])}):")
            for error in results['errors'][:5]:
                print(f"    - {error}")
    
    # Find duplicates
    print("\n" + "=" * 60)
    print("DUPLICATE DETECTION")
    print("=" * 60)
    
    duplicates = find_duplicates(df)
    
    if duplicates.get('email'):
        print(f"\n📧 Duplicate emails found: {len(duplicates['email'])}")
        for dup in duplicates['email'][:5]:
            print(f"  - {dup['value']}: {dup['count']} students")
            for student in dup['students']:
                print(f"    → {student}")
    
    if duplicates.get('phone'):
        print(f"\n📱 Duplicate phones found: {len(duplicates['phone'])}")
        for dup in duplicates['phone'][:5]:
            print(f"  - {dup['value']}: {dup['count']} students")
    
    if duplicates.get('cedula'):
        print(f"\n🆔 Duplicate cedulas found: {len(duplicates['cedula'])}")
        for dup in duplicates['cedula'][:5]:
            print(f"  - {dup['value']}: {dup['count']} students")
    
    # Overall quality score
    print("\n" + "=" * 60)
    print("QUALITY SCORE")
    print("=" * 60)
    
    total_validations = sum(r['valid'] + r['invalid'] for r in validation_results.values())
    total_valid = sum(r['valid'] for r in validation_results.values())
    quality_score = (total_valid / total_validations * 100) if total_validations > 0 else 0
    
    print(f"\nOverall Quality: {quality_score:.2f}%")
    
    if quality_score >= 80:
        print("✅ Database quality is GOOD - Ready for production")
    elif quality_score >= 60:
        print("⚠️ Database quality is ACCEPTABLE - Some cleanup recommended")
    else:
        print("❌ Database quality is POOR - Cleanup required before use")
    
    # Save validation report
    report_file = "validation_report.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("VALIDATION REPORT\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total records: {total_records}\n")
        f.write(f"Quality score: {quality_score:.2f}%\n\n")
        
        for field, results in validation_results.items():
            f.write(f"\n{field.upper()}:\n")
            f.write(f"  Valid: {results['valid']}\n")
            f.write(f"  Invalid: {results['invalid']}\n")
            if results['errors']:
                f.write(f"  Errors:\n")
                for error in results['errors']:
                    f.write(f"    - {error}\n")
    
    print(f"\n📄 Detailed report saved to: {report_file}")

def main():
    input_file = "ESTUDIANTES_CONSOLIDADO.xlsx"
    
    try:
        validate_consolidated_database(input_file)
    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found.")
        print("Please run 'consolidate_database.py' first.")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
