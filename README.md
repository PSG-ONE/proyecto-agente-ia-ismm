# 🤖 Sistema de Consolidación de Base de Datos - Agente IA

## 📋 Descripción

Este sistema consolida la base de datos de estudiantes de la escuela de gastronomía, transformando **59 hojas de Excel** con diferentes formatos en una base de datos estructurada lista para ser consumida por un agente de IA.

---

## 🚀 Inicio Rápido

### Ejecutar Todo el Pipeline

```bash
python run_pipeline.py
```

Este comando ejecutará automáticamente:
1. Inspección de la base de datos
2. Consolidación de todas las hojas
3. Validación de calidad de datos
4. Extracción a formato JSON

### Ver Estadísticas

```bash
python check_json.py
```

### Ver Ejemplos de Datos

```bash
python show_examples.py
```

---

## 📁 Estructura de Archivos

### Scripts Principales

- `README.md` - Este archivo

---

## 📊 Resultados de la Consolidación

- **Total de estudiantes:** 10,423
- **Con email:** 9,116 (87.5%)
- **Con teléfono:** 3,687 (35.4%)
- **Hojas procesadas:** 59

### Distribución por Estado

- Inactivo/Histórico: 6,390 (61.3%)
- Activo/Futuro: 2,332 (22.4%)
- Activo: 794 (7.6%)
- Retirado: 666 (6.4%)
- Graduado: 241 (2.3%)

---

## 🔧 Uso Individual de Scripts

### 1. Inspeccionar Base de Datos

```bash
python inspect_database.py
```

Genera `inspection_results.txt` con la estructura de cada hoja.

### 2. Consolidar Hojas

```bash
python consolidate_database.py
```

Genera `ESTUDIANTES_CONSOLIDADO.xlsx` con todos los datos unificados.

### 3. Validar Datos

```bash
python validate_data.py
```

Valida:
- Formatos de email
- Formatos de teléfono (809/829/849)
- Nombres válidos
- Programas reconocidos
- Duplicados

### 4. Extraer a JSON

```bash
python extract_to_json.py
```

Genera `estudiantes_database.json` con estructura:

```json
{
  "estudiantes": [
    {
      "id": "ABC123DEF456",
      "nombre_completo": "Juan Pérez",
      "email": "juan@example.com",
      "telefono": "809-555-1234",
      "programa": "Cocinero Profesional",
      "estado": "Activo",
      "año_ingreso": 2026
    }
  ],
  "metadata": {
    "total_estudiantes": 10423,
    "estadisticas": {...}
  }
}
```

---

## 🎯 Casos de Uso para el Agente

### 1. Consulta de Estado

**Usuario:** "Hola, soy María García, ¿en qué semestre estoy?"

**Proceso del Agente:**
1. Buscar en JSON por `nombre_completo: "María García"`
2. Verificar `estado: "Activo"`
3. Responder con información del semestre

### 2. Reactivación de Estudiante

**Usuario:** "Me retiré el año pasado, quiero volver"

**Proceso del Agente:**
1. Buscar por teléfono/email
2. Encontrar `estado: "Retirado"`
3. Ofrecer proceso de reincorporación

### 3. Validación de Prospecto

**Usuario:** "Quiero inscribirme en Panadería"

**Proceso del Agente:**
1. Buscar por email/teléfono
2. Si existe: "Veo que ya estuviste con nosotros..."
3. Si no existe: "Perfecto, te registro como nuevo estudiante..."

### 4. Búsqueda Múltiple

El agente puede buscar por:
- `nombre_completo`
- `email`
- `telefono`
- `cedula`
- `programa`
- `estado`

---

## 🔄 Proceso de Actualización

### Cuando hay nuevos estudiantes:

1. Actualizar `ESTUDIANTES.xlsx` con nuevos datos
2. Ejecutar pipeline completo:
   ```bash
   python run_pipeline.py
   ```
3. Revisar `validation_report.txt` para errores
4. Subir `estudiantes_database.json` actualizado a Google Sheets/n8n

### Frecuencia Recomendada:

- **Períodos de inscripción:** Semanal
- **Períodos regulares:** Mensual

---

## 🛠️ Integración con n8n

### Opción 1: Google Sheets (Recomendado)

1. Crear script `upload_to_google_sheets.py`
2. Subir `ESTUDIANTES_CONSOLIDADO.xlsx` a Google Sheets
3. Configurar credenciales en n8n
4. Usar nodo "Google Sheets" para consultas

### Opción 2: JSON Directo

1. Subir `estudiantes_database.json` a servidor
2. Usar nodo "HTTP Request" en n8n
3. Implementar API REST para consultas

### Opción 3: Base de Datos

1. Importar a PostgreSQL/MySQL
2. Usar nodo "PostgreSQL" en n8n
3. Consultas SQL directas

---

## ⚠️ Problemas Conocidos

### 1. Programas No Especificados

**Problema:** 9,390 registros (90%) sin programa especificado

**Solución:** Revisar hojas originales y completar información manualmente

### 2. Teléfonos Faltantes

**Problema:** Solo 35% tiene teléfono registrado

**Solución:** Campaña de actualización de datos de contacto

### 3. Cédulas Faltantes

**Problema:** Solo 7% tiene cédula registrada

**Solución:** Solicitar cédula obligatoria en proceso de inscripción

---

## 📞 Próximos Pasos

### Esta Semana
- [ ] Revisar `ESTUDIANTES_CONSOLIDADO.xlsx`
- [ ] Completar información de programas faltantes
- [ ] Crear `upload_to_google_sheets.py`
- [ ] Extraer info de `INFORMACION PARA IA.pdf` a JSON

### Próxima Semana
- [ ] Subir a Google Sheets
- [ ] Configurar n8n
- [ ] Crear workflow de consulta
- [ ] Integrar base de conocimientos

### Próximas 2 Semanas
- [ ] Configurar Chatwoot
- [ ] Crear prompts del sistema
- [ ] Pruebas end-to-end
- [ ] Implementar casos de uso

---

## 📚 Documentación Adicional

- Ver `PLAN_DESARROLLO_AGENTE.md` para el plan completo
- Ver `RESUMEN_CONSOLIDACION.md` para resumen ejecutivo
- Ver archivos de output para detalles técnicos

---

## ✅ Estado del Proyecto

**Fase Actual:** 🟢 CONSOLIDACIÓN COMPLETADA

**Próxima Fase:** Integración con n8n y Chatwoot

---

## 🤝 Contribución

Para modificar el proceso de consolidación:

1. Editar `consolidate_database.py` para cambiar lógica
2. Editar `extract_to_json.py` para cambiar estructura JSON
3. Ejecutar `python run_pipeline.py` para probar cambios

---

## 📄 Licencia

Proyecto interno - Escuela de Gastronomía

---

**Última actualización:** 2026-01-27
