import pandas as pd
import numpy as np

def limpiar_csv(path, out_path=None):
    df = pd.read_csv(path)

    print("Filas originales:", len(df))

    # Eliminar duplicados y nulos
    df = df.drop_duplicates().dropna()

    print("Filas después de limpiar:", len(df))

    if out_path:
        df.to_csv(out_path, index=False)
        print(f"Archivo limpio guardado en: {out_path}")

    return df


def main(
        dataframe, 
        order,
        col_delete: list = None,
        col_mean: list = None,
        out_path=None):

    df = dataframe.copy()

    # Ordenar
    df = df.sort_values(by=order)

    # Eliminar columnas
    if col_delete:
        df = df.drop(columns=col_delete)
        print(f"Columnas eliminadas: {col_delete}")

    # Calcular medias
    if col_mean:
        for col in col_mean:
            if col in df.columns:
                print(f"Media de '{col}': {df[col].mean()}")
            else:
                print(f"⚠️ La columna '{col}' no existe en el DataFrame")

    # Guardar al final
    if out_path:
        df.to_csv(out_path, index=False)
        print(f"Archivo final guardado en: {out_path}")

    return df

def guardar_excel(df, out_excel):
    with pd.ExcelWriter(out_excel, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Data")

        workbook = writer.book
        worksheet = writer.sheets["Data"]

        # Formato de encabezado
        header = workbook.add_format({
            "bold": True,
            "bg_color": "#DDEBF7",
            "border": 1
        })
        worksheet.set_row(0, None, header)

        # Colorear columnas
        formato_col = workbook.add_format({"bg_color": "#FFF2CC", "border": 1})
        worksheet.set_column(1, 1, 15, formato_col)

        # Aplicar formula, para precio
        if "Price" in df.columns and "Quantity" in df.columns:
            col_total = len(df.columns)
            worksheet.write(0, col_total, "Total", header)

            for row in range(1, len(df) + 1):
                worksheet.write_formula(
                    row,
                    col_total,
                    f"=F{row+1}*G{row+1}"
                )
            
            col_total = col_total + 1
            worksheet.write(0, col_total, "Prueba", header)

        print(f"Excel guradado correctamente en: {out_excel}")

if __name__ == "__main__":
    df_limpio = limpiar_csv("./data/3.csv", "./limpio3.csv")

    df_final = main(
        df_limpio,
        order="iPhone_Model",
        col_delete=["Order_ID"],
        col_mean=["Price"],
        out_path="./final_iphone.csv"
    )

    print(df_final.head())
    guardar_excel(df_final, "excelbonito.xlsx")
