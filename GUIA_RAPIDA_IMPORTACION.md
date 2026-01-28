# 🚀 GUÍA RÁPIDA: Importar EDT a Poryecto MS.mpp

## ⚡ PASOS RÁPIDOS (5 minutos)

### 1️⃣ Abrir Microsoft Project
1. Abre **Microsoft Project**
2. Abre tu archivo **Poryecto MS.mpp**

### 2️⃣ Importar el CSV
1. Ve a **Archivo → Abrir**
2. Cambia el filtro a **"Todos los archivos (*.*)"**
3. Selecciona **EDT_PROYECTO_AGENTE_IA.csv**
4. Aparecerá el **Asistente de importación**

### 3️⃣ Configurar el Asistente

**Pantalla 1:** Selecciona **"Nuevo mapa"** → Siguiente

**Pantalla 2:** Selecciona **"Tareas"** → Siguiente

**Pantalla 3:** Verifica que el delimitador sea **"Coma"** → Siguiente

**Pantalla 4:** Mapea las columnas así:

| Columna CSV | Campo de MS Project |
|-------------|---------------------|
| WBS | WBS |
| Task Name | Name |
| Duration | Duration |
| Start Date | Start |
| Finish Date | Finish |
| Predecessors | Predecessors |
| Resource Names | Resource Names |
| Work (hours) | Work |
| Milestone | Milestone |
| Notes | Notes |

**Pantalla 5:** Haz clic en **Finalizar**

### 4️⃣ Verificar la Importación
- ✅ Verifica que las **80+ tareas** se importaron
- ✅ Verifica que las **dependencias** están correctas
- ✅ Verifica que los **hitos** están marcados
- ✅ Verifica que las **fechas** son correctas (inicio: 03/02/2026)

### 5️⃣ Guardar
1. Ve a **Archivo → Guardar como**
2. Guarda como **Poryecto MS.mpp** (sobrescribe el archivo anterior)
3. O guarda como **Poryecto_MS_EDT_Completo.mpp** (nuevo archivo)

---

## 🎨 CONFIGURACIONES RECOMENDADAS

### Después de Importar:

#### 1. Configurar Calendario
```
Herramientas → Cambiar calendario laboral
- Lunes a Viernes: 8:00 AM - 5:00 PM (8 horas)
- Sábado y Domingo: No laborables
```

#### 2. Configurar Opciones
```
Archivo → Opciones → Programación
- Horas por día: 8
- Horas por semana: 40
- Días por mes: 20
```

#### 3. Activar Ruta Crítica
```
Formato → Tareas críticas
```

#### 4. Crear Línea Base
```
Proyecto → Establecer línea base → Línea base
```

---

## 📊 VERIFICACIÓN FINAL

Después de importar, verifica que tienes:

- [ ] **9 fases principales** (tareas de resumen)
- [ ] **80+ subtareas** distribuidas
- [ ] **9 hitos** marcados (con rombo ◆)
- [ ] **2 recursos:** Persona 1 y Persona 2
- [ ] **Fecha de inicio:** 03/02/2026
- [ ] **Fecha de fin:** 09/04/2026
- [ ] **Duración total:** 47 días
- [ ] **Horas totales:** 752h
- [ ] **Dependencias** funcionando
- [ ] **Ruta crítica** visible en rojo

---

## ⚠️ PROBLEMAS COMUNES

### Problema: "Las fechas no coinciden"
**Solución:**
1. Verifica que el calendario sea Lunes-Viernes
2. Ve a **Proyecto → Calcular proyecto**

### Problema: "Las dependencias no funcionan"
**Solución:**
1. Verifica que usaste el **número de ID de tarea**, no el WBS
2. Formato correcto: `2;3` para múltiples predecesoras

### Problema: "La importación falla"
**Solución:**
1. Abre el CSV en Excel
2. Verifica que las fechas estén en formato **DD/MM/AAAA**
3. Guarda y vuelve a importar

---

## 📁 ARCHIVOS NECESARIOS

- **EDT_PROYECTO_AGENTE_IA.csv** ← Este es el que importas
- **GUIA_IMPORTACION_MS_PROJECT.md** ← Guía completa
- **Poryecto MS.mpp** ← Tu archivo de MS Project

---

## 🆘 ¿NECESITAS AYUDA?

Si tienes problemas:
1. Consulta **GUIA_IMPORTACION_MS_PROJECT.md** (guía completa)
2. Revisa la sección de "Solución de problemas"
3. Verifica que MS Project esté actualizado

---

**Tiempo estimado:** 5-10 minutos  
**Dificultad:** Fácil  
**Resultado:** EDT completa en MS Project

---

**Creado:** 27 de enero de 2026  
**Para:** Proyecto Agente IA ISMM
