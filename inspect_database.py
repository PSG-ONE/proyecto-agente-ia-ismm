import pandas as pd
import os

file_estudiantes = "ESTUDIANTES.xlsx"

if not os.path.exists(file_estudiantes):
    print(f"File {file_estudiantes} not found.")
else:
    try:

        # Load the Excel file to list sheet names
        xl = pd.ExcelFile(file_estudiantes)
        # Open output file
        with open("inspection_results.txt", "w", encoding="utf-8") as f:
            f.write(f"Sheet names: {xl.sheet_names}\n")
            
            # Iterate through sheets and print a summary of each
            for sheet in xl.sheet_names:
                f.write(f"\n--- Sheet: {sheet} ---\n")
                df = xl.parse(sheet)
                f.write(f"Shape: {df.shape}\n")
                # Find the first row that looks like a header (contains "NOMBRE" or "CORREO")
                # We'll look at the first 10 rows
                f.write("First 10 rows:\n")
                f.write(df.head(10).to_string() + "\n")

            
    except Exception as e:
        print(f"Error reading Excel: {e}")
