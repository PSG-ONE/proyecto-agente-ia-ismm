# 🚀 Guía: Subir Proyecto a GitHub y Activar GitHub Pages

## ✅ **ESTADO ACTUAL**
- ✅ Repositorio Git inicializado
- ✅ Archivos agregados y commiteados
- ✅ Listo para subir a GitHub

---

## 📋 **PASOS PARA SUBIR A GITHUB**

### **PASO 1: Crear Repositorio en GitHub**

1. **Abre tu navegador** y ve a [github.com](https://github.com)

2. **Inicia sesión** con tu cuenta de GitHub
   - Si no tienes cuenta, créala gratis en [github.com/signup](https://github.com/signup)

3. **Haz clic en el botón verde "New"** (o el ícono "+" arriba a la derecha → "New repository")

4. **Configura el repositorio:**
   - **Repository name:** `proyecto-agente-ia-ismm`
   - **Description:** `Proyecto de Agente IA para Escuela de Gastronomía ISMM - Diagrama de Gantt Interactivo`
   - **Visibilidad:** 
     - ✅ **Public** (para que GitHub Pages funcione gratis)
     - O **Private** (si prefieres que sea privado, pero GitHub Pages requiere plan de pago)
   - **NO marques** "Initialize this repository with a README"
   - **NO agregues** .gitignore ni license (ya los tenemos)

5. **Haz clic en "Create repository"**

---

### **PASO 2: Conectar tu Repositorio Local con GitHub**

Después de crear el repositorio, GitHub te mostrará instrucciones. Copia el **URL del repositorio**.

Ejemplo: `https://github.com/tuusuario/proyecto-agente-ia-ismm.git`

**Ejecuta estos comandos en tu terminal:**

```bash
# Conectar con GitHub (reemplaza con tu URL)
git remote add origin https://github.com/tuusuario/proyecto-agente-ia-ismm.git

# Renombrar rama a main (si es necesario)
git branch -M main

# Subir archivos a GitHub
git push -u origin main
```

**IMPORTANTE:** Si te pide usuario y contraseña:
- **Usuario:** Tu nombre de usuario de GitHub
- **Contraseña:** Usa un **Personal Access Token** (no tu contraseña normal)
  - Ve a: GitHub → Settings → Developer settings → Personal access tokens → Generate new token
  - Marca: `repo` (acceso completo)
  - Copia el token y úsalo como contraseña

---

### **PASO 3: Activar GitHub Pages**

1. **Ve a tu repositorio** en GitHub

2. **Haz clic en "Settings"** (Configuración)

3. **En el menú lateral izquierdo**, haz clic en **"Pages"**

4. **Configura GitHub Pages:**
   - **Source:** Deploy from a branch
   - **Branch:** `main` (o `master`)
   - **Folder:** `/ (root)`

5. **Haz clic en "Save"**

6. **Espera 1-2 minutos** mientras GitHub despliega tu sitio

7. **Verás un mensaje verde:**
   ```
   Your site is live at https://tuusuario.github.io/proyecto-agente-ia-ismm/
   ```

---

### **PASO 4: Acceder al Gantt**

Tu diagrama de Gantt estará disponible en:

```
https://tuusuario.github.io/proyecto-agente-ia-ismm/gantt_proyecto.html
```

**¡Comparte este link con quien quieras!** 🎉

---

## 🔧 **COMANDOS COMPLETOS (Copia y Pega)**

Abre tu terminal en la carpeta del proyecto y ejecuta:

```bash
# 1. Conectar con GitHub (REEMPLAZA con tu URL)
git remote add origin https://github.com/TUUSUARIO/proyecto-agente-ia-ismm.git

# 2. Renombrar rama a main
git branch -M main

# 3. Subir a GitHub
git push -u origin main
```

---

## 🆘 **SOLUCIÓN DE PROBLEMAS**

### **Error: "remote origin already exists"**
```bash
git remote remove origin
git remote add origin https://github.com/TUUSUARIO/proyecto-agente-ia-ismm.git
```

### **Error: "Authentication failed"**
- Usa un **Personal Access Token** en lugar de tu contraseña
- Genera uno en: GitHub → Settings → Developer settings → Personal access tokens

### **Error: "Permission denied"**
- Verifica que el repositorio sea tuyo
- Verifica que tengas permisos de escritura

---

## 📝 **ACTUALIZAR EL README**

Después de subir, edita el archivo `README_GITHUB.md` en GitHub y reemplaza:

```markdown
[Haz clic aquí](https://tuusuario.github.io/proyecto-agente-ia/gantt_proyecto.html)
```

Por tu URL real:

```markdown
[Haz clic aquí](https://TUUSUARIO.github.io/proyecto-agente-ia-ismm/gantt_proyecto.html)
```

---

## ✅ **VERIFICACIÓN FINAL**

Después de completar todos los pasos, verifica:

- ✅ El repositorio está en GitHub
- ✅ GitHub Pages está activado
- ✅ El Gantt se ve correctamente en el navegador
- ✅ Puedes compartir el link

---

## 🎯 **PRÓXIMOS PASOS**

1. **Comparte el link** con tu equipo o stakeholders
2. **Actualiza el proyecto** cuando sea necesario:
   ```bash
   git add .
   git commit -m "Actualización del proyecto"
   git push
   ```
3. **GitHub Pages se actualizará automáticamente** en 1-2 minutos

---

## 📞 **¿NECESITAS AYUDA?**

Si tienes problemas en algún paso:
1. Envíame una captura de pantalla del error
2. Dime en qué paso estás
3. Te ayudo a resolverlo

---

**¡Tu proyecto estará online en menos de 5 minutos!** 🚀
