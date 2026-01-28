import json

# Load and display JSON statistics
with open('estudiantes_database.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=" * 60)
print("RESUMEN DE BASE DE DATOS CONSOLIDADA")
print("=" * 60)

metadata = data['metadata']
stats = metadata['estadisticas']

print(f"\nTotal estudiantes: {metadata['total_estudiantes']}")
print(f"Ultima actualizacion: {metadata['ultima_actualizacion']}")

print("\n--- Contacto ---")
print(f"Con email: {stats['con_email']}")
print(f"Con telefono: {stats['con_telefono']}")
print(f"Con cedula: {stats['con_cedula']}")

print("\n--- Por Estado ---")
for estado, count in stats['por_estado'].items():
    print(f"  {estado}: {count}")

print("\n--- Por Programa ---")
for programa, count in sorted(stats['por_programa'].items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"  {programa}: {count}")

print("\n" + "=" * 60)
print("Archivo JSON generado exitosamente!")
print("=" * 60)
