# 🗺️ MAPA DEL PROYECTO - Agente de IA para Escuela de Gastronomía

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         ARQUITECTURA DEL SISTEMA                        │
└─────────────────────────────────────────────────────────────────────────┘

┌──────────────────┐
│   ESTUDIANTES    │
│   (59 hojas)     │ ◄─── Problema: Datos fragmentados y mal estructurados
└────────┬─────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    FASE 1: CONSOLIDACIÓN DE DATOS                       │
│                         (COMPLETADA ✅)                                 │
└─────────────────────────────────────────────────────────────────────────┘
         │
         ├──► [inspect_database.py]
         │    └─► inspection_results.txt (202 KB)
         │
         ├──► [consolidate_database.py]
         │    └─► ESTUDIANTES_CONSOLIDADO.xlsx (489 KB)
         │        • 10,423 estudiantes
         │        • Formato unificado
         │        • Duplicados marcados
         │
         ├──► [validate_data.py]
         │    └─► validation_report.txt
         │        • Validación de emails
         │        • Validación de teléfonos
         │        • Detección de duplicados
         │
         └──► [extract_to_json.py]
              └─► estudiantes_database.json (5.3 MB)
                  • Formato JSON estructurado
                  • Metadatos y estadísticas
                  • Listo para el agente

┌─────────────────────────────────────────────────────────────────────────┐
│                    FASE 2: INTEGRACIÓN CON AGENTE                       │
│                         (PENDIENTE ⚠️)                                  │
└─────────────────────────────────────────────────────────────────────────┘
         │
         ├──► [upload_to_google_sheets.py] (Por crear)
         │    └─► Google Sheets
         │        • Acceso en tiempo real
         │        • Actualización colaborativa
         │
         ├──► [extract_courses_info.py] (Por crear)
         │    └─► cursos_database.json
         │        • Info de INFORMACION PARA IA.pdf
         │        • Carreras y Diplomados
         │
         └──► [create_knowledge_base.py] (Por crear)
              └─► knowledge_base.json
                  • Estudiantes + Cursos
                  • Base completa para RAG

┌─────────────────────────────────────────────────────────────────────────┐
│                    FASE 3: CONFIGURACIÓN n8n                            │
│                         (PENDIENTE ⚠️)                                  │
└─────────────────────────────────────────────────────────────────────────┘
         │
         ├──► Workflow 1: Consulta de Estudiantes
         │    • Webhook de Chatwoot
         │    • Búsqueda en Google Sheets
         │    • Respuesta con GPT-4
         │
         ├──► Workflow 2: Información de Cursos
         │    • RAG con knowledge_base.json
         │    • Respuestas sobre programas
         │
         └──► Workflow 3: Registro de Leads
              • Captura de datos
              • Guardado en Google Sheets
              • Notificación al equipo

┌─────────────────────────────────────────────────────────────────────────┐
│                    FASE 4: INTEGRACIÓN CHATWOOT                         │
│                         (PENDIENTE ⚠️)                                  │
└─────────────────────────────────────────────────────────────────────────┘
         │
         ├──► Configurar Inbox
         ├──► Configurar Agent Bot
         ├──► Conectar con n8n (Webhooks)
         └──► Pruebas de conversación

┌─────────────────────────────────────────────────────────────────────────┐
│                         AGENTE EN PRODUCCIÓN                            │
│                         (OBJETIVO FINAL 🎯)                             │
└─────────────────────────────────────────────────────────────────────────┘

         Usuario (WhatsApp/Web)
              │
              ▼
         ┌──────────┐
         │ Chatwoot │ ◄──┐
         └────┬─────┘    │
              │          │
              ▼          │
         ┌──────────┐    │
         │   n8n    │    │ Respuesta
         └────┬─────┘    │
              │          │
              ├──► Google Sheets (Estudiantes)
              ├──► Knowledge Base (Cursos)
              ├──► OpenAI GPT-4
              │
              └──────────┘

═══════════════════════════════════════════════════════════════════════════

                            CASOS DE USO

═══════════════════════════════════════════════════════════════════════════

1️⃣  CONSULTA DE ESTADO
   Usuario: "Hola, soy María García, ¿en qué semestre estoy?"
   
   Flujo:
   Chatwoot → n8n → Buscar en Google Sheets por nombre
                 → GPT-4 genera respuesta personalizada
                 → Respuesta: "Hola María, estás en III SEMESTRE..."

2️⃣  INFORMACIÓN DE CURSO
   Usuario: "¿Cuánto cuesta el Diplomado de Cocina Básica?"
   
   Flujo:
   Chatwoot → n8n → Buscar en Knowledge Base
                 → GPT-4 con contexto del curso
                 → Respuesta: "El Diplomado cuesta 37,000 pesos..."

3️⃣  REACTIVACIÓN
   Usuario: "Me retiré el año pasado, quiero volver"
   
   Flujo:
   Chatwoot → n8n → Buscar en Google Sheets (estado: Retirado)
                 → GPT-4 con contexto de reactivación
                 → Respuesta: "Veo que estuviste en [Programa]..."

4️⃣  REGISTRO DE LEAD
   Usuario: "Quiero inscribirme en Panadería"
   
   Flujo:
   Chatwoot → n8n → Verificar si existe en base
                 → Si no existe: Solicitar datos
                 → Guardar en Google Sheets
                 → Notificar al equipo

═══════════════════════════════════════════════════════════════════════════

                        ESTRUCTURA DE DATOS

═══════════════════════════════════════════════════════════════════════════

📊 ESTUDIANTES (estudiantes_database.json)
{
  "id": "ABC123DEF456",
  "nombre_completo": "Juan Pérez",
  "email": "juan@example.com",
  "telefono": "809-555-1234",
  "cedula": "001-1234567-8",
  "programa": "Cocinero Profesional",
  "estado": "Activo",
  "semestre_actual": "III SEMESTRE",
  "año_ingreso": 2026,
  "horario": "Mañana"
}

📚 CURSOS (cursos_database.json - Por crear)
{
  "id": "CURSO-001",
  "nombre": "Diplomado de Cocina Básica",
  "tipo": "Diplomado",
  "duracion": "12 semanas",
  "precio": 37000,
  "horarios": ["Miércoles 6-9pm", "Sábado 4-7pm"],
  "inicio": "2026-01-14",
  "temario": [...]
}

═══════════════════════════════════════════════════════════════════════════

                          CRONOGRAMA

═══════════════════════════════════════════════════════════════════════════

SEMANA 1 (Actual) ✅
├─ Consolidación de base de datos
├─ Validación de datos
├─ Extracción a JSON
└─ Documentación

SEMANA 2 ⚠️
├─ Extracción de info de cursos (PDF → JSON)
├─ Creación de knowledge base
├─ Upload a Google Sheets
└─ Configuración de credenciales

SEMANA 3 ⚠️
├─ Configuración de n8n
├─ Creación de workflows
├─ Integración con Google Sheets
└─ Pruebas de consultas

SEMANA 4 ⚠️
├─ Configuración de Chatwoot
├─ Integración Chatwoot ↔ n8n
├─ Creación de prompts del sistema
└─ Pruebas end-to-end

SEMANA 5 ⚠️
├─ Ajustes y optimización
├─ Pruebas con usuarios reales
├─ Documentación final
└─ 🚀 LANZAMIENTO

═══════════════════════════════════════════════════════════════════════════

                      MÉTRICAS DE ÉXITO

═══════════════════════════════════════════════════════════════════════════

✅ Consolidación de Datos
   • 10,423 estudiantes procesados
   • 59 hojas unificadas
   • 87.5% con email válido

⚠️ Calidad de Datos (Por mejorar)
   • 90% sin programa especificado
   • 35% con teléfono
   • 7% con cédula

🎯 Objetivos del Agente
   • Responder consultas en < 5 segundos
   • 90% de precisión en respuestas
   • Capturar 100% de leads
   • Reducir carga de trabajo manual en 70%

═══════════════════════════════════════════════════════════════════════════
```
