import json
import random

# Load JSON database
with open('estudiantes_database.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

estudiantes = data['estudiantes']

print("=" * 70)
print("EJEMPLOS DE DATOS CONSOLIDADOS")
print("=" * 70)

# Filter students with complete information
complete_students = [
    s for s in estudiantes 
    if s['email'] and s['telefono'] and s['programa'] != "No especificado"
]

print(f"\nEstudiantes con información completa: {len(complete_students)}")

# Show 5 random examples
print("\n--- EJEMPLOS DE ESTUDIANTES ACTIVOS ---\n")

active_students = [s for s in complete_students if "Activo" in s['estado']]

if active_students:
    samples = random.sample(active_students, min(5, len(active_students)))
    
    for i, student in enumerate(samples, 1):
        print(f"{i}. {student['nombre_completo']}")
        print(f"   Email: {student['email']}")
        print(f"   Teléfono: {student['telefono']}")
        print(f"   Programa: {student['programa']}")
        print(f"   Estado: {student['estado']}")
        print(f"   Año: {student['año_ingreso']}")
        print(f"   Horario: {student['horario']}")
        print()

# Show retirados examples
print("\n--- EJEMPLOS DE ESTUDIANTES RETIRADOS ---\n")

retired_students = [s for s in estudiantes if s['estado'] == "Retirado"]

if retired_students:
    samples = random.sample(retired_students, min(3, len(retired_students)))
    
    for i, student in enumerate(samples, 1):
        print(f"{i}. {student['nombre_completo']}")
        print(f"   Email: {student['email'] or 'No disponible'}")
        print(f"   Programa: {student['programa']}")
        print(f"   Fuente: {student['fuente_hoja']}")
        print()

# Show programs distribution
print("\n--- DISTRIBUCIÓN DE PROGRAMAS (Top 10) ---\n")

programs = {}
for s in estudiantes:
    prog = s['programa']
    programs[prog] = programs.get(prog, 0) + 1

sorted_programs = sorted(programs.items(), key=lambda x: x[1], reverse=True)

for i, (program, count) in enumerate(sorted_programs[:10], 1):
    percentage = (count / len(estudiantes)) * 100
    bar = "█" * int(percentage / 2)
    print(f"{i:2}. {program[:40]:40} | {count:5} ({percentage:5.1f}%) {bar}")

print("\n" + "=" * 70)
print("CASOS DE USO PARA EL AGENTE")
print("=" * 70)

print("\n1. BÚSQUEDA POR NOMBRE:")
print("   Usuario: 'Hola, soy María García'")
print("   Agente busca en JSON por nombre_completo")
print("   → Encuentra registro y muestra estado/programa")

print("\n2. BÚSQUEDA POR EMAIL:")
print("   Usuario proporciona email")
print("   Agente busca en JSON por email")
print("   → Identifica si es estudiante activo/retirado/nuevo")

print("\n3. REACTIVACIÓN:")
print("   Usuario: 'Me retiré el año pasado'")
print("   Agente busca registros con estado='Retirado'")
print("   → Ofrece proceso de reincorporación")

print("\n4. VALIDACIÓN DE DUPLICADOS:")
print("   Usuario intenta inscribirse")
print("   Agente busca por email/teléfono/cédula")
print("   → Detecta si ya existe en la base")

print("\n" + "=" * 70)
