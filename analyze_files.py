import pandas as pd
from pypdf import PdfReader
import os

# Filenames
file_estudiantes = "ESTUDIANTES.xlsx"
file_info_ia = "INFORMACION PARA IA.pdf"
file_reqs = "Información_requerida_para_iniciar_la_creación_de_de_Agente_de_IA._ISMM[1].pdf"

def read_pdf(path):
    try:
        if not os.path.exists(path):
            return f"File not found: {path}"
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading PDF {path}: {e}"

def read_excel(path):
    try:
        if not os.path.exists(path):
            return f"File not found: {path}"
        # Read the first few rows to get an idea of the structure
        df = pd.read_excel(path, nrows=5)
        
        # Also get basic stats
        info = f"Columns: {list(df.columns)}\n"
        return info + df.to_string()
    except Exception as e:
        return f"Error reading Excel {path}: {e}"


with open("analysis_output.txt", "w", encoding="utf-8") as f:
    f.write("--- CONTENIDO DE INFORMACION PARA IA.pdf ---\n")
    f.write(read_pdf(file_info_ia)[:4000])
    f.write("\n" + "="*50 + "\n")

    f.write("--- CONTENIDO DE REQUERIMIENTOS ---\n")
    f.write(read_pdf(file_reqs)[:4000])
    f.write("\n" + "="*50 + "\n")

    f.write("--- CONTENIDO DE ESTUDIANTES.xlsx ---\n")
    f.write(read_excel(file_estudiantes))

