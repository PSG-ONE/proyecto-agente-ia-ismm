# Plan de Desarrollo: Agente de IA para Escuela de Gastronomía (n8n + Chatwoot)

## 1. Visión General
Desarrollar un Agente de IA capaz de interactuar con prospectos y estudiantes de la escuela de gastronomía a través de Chatwoot. El agente utilizará n8n como orquestador para procesar consultas, buscar información en la base de conocimientos y gestionar datos de estudiantes.

**Objetivos del Agente:**
1.  **Atención al Prospecto:** Responder dudas sobre Carreras (Cocinero, Panadero, Pastelero) y Diplomados.
2.  **Orientación Académica:** Recomendar cursos según el perfil.
3.  **Captación de Leads:** Registrar interesados.
4.  **Consultas de Estudiantes (Opcional/Futuro):** Verificar estado de alumnos (basado en la data de estudiantes).

## 2. Arquitectura del Sistema
*   **Canal de Comunicación:** Chatwoot (Widget web / WhatsApp / Redes Sociales).
*   **Orquestador:** n8n (Self-hosted o Cloud).
*   **Cerebro (LLM):** OpenAI (GPT-4o) o Anthropic (Claude 3.5 Sonnet) vía API.
*   **Base de Conocimientos (RAG):**
    *   Información de cursos estructurada (extraída de `INFORMACION PARA IA.pdf`).
    *   (Opcional) Base vectorial (Pinecone/Qdrant) si el volumen de texto crece.
*   **Base de Datos de Estudiantes:**
    *   Archivo `ESTUDIANTES.xlsx` como referencia inicial (se recomienda migrar a Google Sheets, Airtable o Supabase para acceso en tiempo real).

## 3. Plan de Trabajo por Fases

### Fase 1: Preparación de Datos (Knowledge Base)
**Objetivo:** Estructurar la información "cruda" para que el agente la consuma sin alucinaciones.
*   [ ] **Estructuración de `INFORMACION PARA IA.pdf`:**
    *   Crear un JSON o Tabla maestra con: Nombre del Programa, Duración, Costo, Horarios, Temario, Requisitos.
    *   *Ejemplo:* `{"programa": "Diplomado Cocina Básica", "precio": 37000, "duracion": "12 semanas", ...}`
*   [x] **Limpieza de `ESTUDIANTES.xlsx`:**
    *   **COMPLETADO:** Se ha generado el archivo `ESTUDIANTES_CONSOLIDADO.xlsx`.
    *   **Resumen de Datos:** 13,190 registros consolidados.
        *   Activos/Futuros (2025-2026): ~2,800 registros.
        *   Inactivos/Históricos (2024 y ant.): ~8,400 registros.
        *   Retirados: ~677 registros.
        *   Graduados: ~350 registros.
    *   **Acción Siguiente:** Subir este archivo consolidado a Google Sheets para conectarlo con n8n.

### Fase 2: Configuración de Herramientas
*   [ ] **Chatwoot:**
    *   Crear Inbox de "Atención al Cliente".
    *   Configurar "Agent Bot" para enviar eventos a n8n.
*   [ ] **n8n:**
    *   Configurar credenciales (OpenAI, Chatwoot, Google Sheets).
    *   Crear Workflow Principal.

### Fase 3: Desarrollo del Workflow en n8n
**Flujo Lógico:**
1.  **Webhook:** Recibe mensaje de Chatwoot.
2.  **Clasificación de Intención:** ¿Es venta? ¿Es soporte? ¿Es alumno antiguo?
3.  **Rama de Ventas (RAG):**
    *   Si pregunta por cursos, consultar el JSON/Vector Store de cursos.
    *   Responder con detalles específicos (Precio, Inicio, etc.).
4.  **Rama de Registro:**
    *   Si el usuario muestra interés, solicitar datos (Nombre, Teléfono) y guardar en Google Sheets/CRM.
5.  **Respuesta:** Enviar texto formateado a Chatwoot.

### Fase 4: Pruebas y Despliegue
*   [ ] Pruebas de conversación con preguntas del archivo de requerimientos.
*   [ ] Validación de captura de leads.
*   [ ] Ajuste de "Prompt del Sistema" (Personalidad, tono de voz de la escuela).

## 4. Estructura de Datos Requerida (basada en PDFs)
Según `Información_requerida...pdf`, necesitamos consolidar para cada curso:
*   [x] Nombre y Descripción (Disponible en PDF Info)
*   [x] Duración y Horarios (Disponible en PDF Info)
*   [x] Costos (Disponible para Diplomados, verificar para Carreras)
*   [ ] Requisitos de Ingreso (Validar si está completo)
*   [ ] Preguntas Frecuentes (Crear lista base)

## 5. Problema Identificado: Base de Datos Mal Estructurada

### 5.1 Diagnóstico del Problema
El archivo `ESTUDIANTES.xlsx` presenta los siguientes problemas críticos:

**Problemas Estructurales:**
- ✗ **Múltiples hojas con diferentes formatos**: Cada hoja tiene su propia estructura de columnas
- ✗ **Encabezados inconsistentes**: Algunas hojas tienen encabezados en diferentes filas
- ✗ **Datos mezclados**: Estudiantes activos, retirados y graduados en diferentes hojas
- ✗ **Columnas variables**: No todas las hojas tienen las mismas columnas (NOMBRE, APELLIDO, vs NOMBRE Y APELLIDO)
- ✗ **Información duplicada**: Posibles registros duplicados entre hojas
- ✗ **Datos de diferentes períodos**: Hojas por año (2023, 2024, 2025, 2026) sin consolidar

**Impacto en el Agente de IA:**
- El agente NO puede leer directamente esta base de datos
- Imposible hacer búsquedas eficientes de estudiantes
- Riesgo de información contradictoria o desactualizada
- No se puede generar estadísticas ni reportes confiables

### 5.2 Solución: Script de Extracción y Consolidación

**Objetivo:** Crear una base de datos consolidada y estructurada que el agente pueda consultar eficientemente.

**Scripts Necesarios:**

#### Script 1: `inspect_database.py` ✅ (YA EXISTE)
- **Función**: Inspeccionar todas las hojas del Excel
- **Output**: `inspection_results.txt` con la estructura de cada hoja
- **Estado**: COMPLETADO

#### Script 2: `consolidate_database.py` ✅ (YA EXISTE)
- **Función**: Consolidar todas las hojas en un formato único
- **Output**: `ESTUDIANTES_CONSOLIDADO.xlsx`
- **Características**:
  - Normaliza nombres de columnas
  - Detecta automáticamente encabezados
  - Unifica formatos (NOMBRE + APELLIDO → Nombre_Completo)
  - Clasifica estudiantes por estado (Activo, Retirado, Graduado)
  - Detecta duplicados
  - Limpia datos (emails, teléfonos)

#### Script 3: `extract_to_json.py` ⚠️ (PENDIENTE)
- **Función**: Convertir el Excel consolidado a JSON para el agente
- **Output**: `estudiantes_database.json`
- **Estructura sugerida**:
```json
{
  "estudiantes": [
    {
      "id": "unique_id",
      "nombre_completo": "Juan Pérez",
      "email": "juan@example.com",
      "telefono": "809-123-4567",
      "cedula": "001-1234567-8",
      "programa": "COCINERO PANADERO Y PASTELERO",
      "estado": "Activo",
      "semestre": "I SEMESTRE",
      "año_ingreso": "2026",
      "fuente": "CPP 1 MARZO 2026"
    }
  ],
  "metadata": {
    "total_estudiantes": 1500,
    "ultima_actualizacion": "2026-01-27",
    "estados": {
      "activos": 800,
      "retirados": 500,
      "graduados": 200
    }
  }
}
```

#### Script 4: `upload_to_google_sheets.py` ⚠️ (PENDIENTE)
- **Función**: Subir la base consolidada a Google Sheets
- **Ventajas**:
  - Acceso en tiempo real desde n8n
  - Actualización colaborativa
  - API nativa de Google
  - Historial de cambios

#### Script 5: `validate_data.py` ⚠️ (PENDIENTE)
- **Función**: Validar la calidad de los datos consolidados
- **Validaciones**:
  - Emails válidos
  - Teléfonos con formato correcto
  - Nombres no vacíos
  - Programas reconocidos
  - Detección de duplicados por email/cédula

### 5.3 Plan de Ejecución (Orden Secuencial)

```
FASE A: ANÁLISIS Y CONSOLIDACIÓN (1-2 días)
├── [✅] Paso 1: Ejecutar inspect_database.py
├── [✅] Paso 2: Ejecutar consolidate_database.py
├── [⚠️] Paso 3: Revisar ESTUDIANTES_CONSOLIDADO.xlsx
└── [⚠️] Paso 4: Identificar problemas de calidad de datos

FASE B: TRANSFORMACIÓN Y VALIDACIÓN (1 día)
├── [⚠️] Paso 5: Crear extract_to_json.py
├── [⚠️] Paso 6: Ejecutar extract_to_json.py
├── [⚠️] Paso 7: Crear validate_data.py
└── [⚠️] Paso 8: Ejecutar validate_data.py y corregir errores

FASE C: INTEGRACIÓN CON AGENTE (1 día)
├── [⚠️] Paso 9: Crear upload_to_google_sheets.py
├── [⚠️] Paso 10: Subir datos a Google Sheets
├── [⚠️] Paso 11: Configurar acceso API en n8n
└── [⚠️] Paso 12: Crear workflow de consulta en n8n

FASE D: PRUEBAS Y OPTIMIZACIÓN (1 día)
├── [⚠️] Paso 13: Probar consultas desde n8n
├── [⚠️] Paso 14: Optimizar búsquedas (índices, filtros)
└── [⚠️] Paso 15: Documentar proceso de actualización
```

### 5.4 Estructura Final de Datos para el Agente

**Campos Esenciales:**
| Campo | Tipo | Ejemplo | Uso en el Agente |
|-------|------|---------|------------------|
| `id` | String | "EST-2026-001" | Identificador único |
| `nombre_completo` | String | "María García" | Búsqueda por nombre |
| `email` | String | "maria@gmail.com" | Contacto y validación |
| `telefono` | String | "809-555-1234" | Contacto WhatsApp |
| `cedula` | String | "001-1234567-8" | Identificación única |
| `programa` | String | "Cocinero Profesional" | Filtro por carrera |
| `estado` | Enum | "Activo/Retirado/Graduado" | Segmentación |
| `semestre_actual` | String | "III SEMESTRE" | Seguimiento académico |
| `año_ingreso` | Integer | 2026 | Análisis temporal |
| `horario` | String | "Mañana/Tarde" | Organización |
| `valor_semestre` | Float | 95000 | Información financiera |

### 5.5 Casos de Uso del Agente con la Base de Datos

**Caso 1: Consulta de Estado de Estudiante**
```
Usuario: "Hola, soy María García, quiero saber en qué semestre estoy"
Agente: 
  1. Busca en la base por nombre "María García"
  2. Verifica estado = "Activo"
  3. Responde: "Hola María, estás en III SEMESTRE de Cocinero Profesional"
```

**Caso 2: Reactivación de Estudiante Retirado**
```
Usuario: "Me retiré el año pasado, quiero volver"
Agente:
  1. Busca por teléfono/email
  2. Encuentra estado = "Retirado"
  3. Responde: "Veo que estuviste en [Programa]. Te puedo ayudar a reincorporarte..."
```

**Caso 3: Validación de Prospecto**
```
Usuario: "Quiero inscribirme en Panadería"
Agente:
  1. Busca por email/teléfono
  2. Si existe: "Veo que ya estuviste con nosotros..."
  3. Si no existe: "Perfecto, te registro como nuevo estudiante..."
```

## 6. Próximos Pasos Inmediatos

### Acción Inmediata (HOY):
1. ✅ Verificar que `consolidate_database.py` funcione correctamente
2. ⚠️ Ejecutar consolidación y revisar output
3. ⚠️ Crear `extract_to_json.py` para formato JSON
4. ⚠️ Crear `validate_data.py` para control de calidad

### Esta Semana:
5. ⚠️ Subir datos consolidados a Google Sheets
6. ⚠️ Configurar credenciales de Google Sheets en n8n
7. ⚠️ Crear workflow de prueba en n8n para consultar estudiantes
8. ⚠️ Extraer información de `INFORMACION PARA IA.pdf` a JSON estructurado

### Próxima Semana:
9. ⚠️ Integrar base de conocimientos (cursos) con base de estudiantes
10. ⚠️ Crear prompts del sistema para el agente
11. ⚠️ Configurar Chatwoot y conectar con n8n
12. ⚠️ Pruebas de conversación end-to-end
