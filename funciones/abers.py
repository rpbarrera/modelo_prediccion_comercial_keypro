import pandas as pd

df = pd.read_excel("funciones/version_conHH.xlsx", engine="openpyxl", header=2)

def filtrar_datos(df,tipo_cliente=None, tipo_ingenieria=None, contrato_marco=None):
    filtro = df
    if tipo_cliente:
        filtro = filtro[filtro['Cliente_x'].astype(str).str.contains(tipo_cliente, case=False, na=False)]
    if tipo_ingenieria:
        filtro = filtro[filtro['TIPO DE INGENIERÍA'].astype(str).str.contains(tipo_ingenieria, case=False, na=False)]
    if contrato_marco:
        filtro = filtro[filtro['Contrato Marco_x'].astype(str).str.contains(contrato_marco, case=False, na=False)]
    
    return filtro


#df_nuevo = filtrar_datos(df, "BHP", "Detalles", "SI" )
#df_nuevo.to_excel("dataframe_filtrado_por_BHP_BLABLABLA.xlsx", index=False, engine="openpyxl") #para ver si queda la estructura que quiero
