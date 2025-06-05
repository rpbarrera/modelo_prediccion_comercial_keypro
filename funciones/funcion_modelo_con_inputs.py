# PRUEBAS MODELO CON INPUTS
import numpy as np
import joblib
import pandas as pd


modelo = joblib.load("modelo_entrenado.pkl")

df = pd.read_excel(r"version_conHH.xlsx", engine="openpyxl", header=2)

def filtrar_datos(df,tipo_cliente=None, tipo_ingenieria=None, contrato_marco=None):
    filtro = df
    if tipo_cliente:
        filtro = filtro[filtro['Cliente_x'].astype(str).str.contains(tipo_cliente, case=False, na=False)]
    if tipo_ingenieria:
        filtro = filtro[filtro['TIPO DE INGENIERÍA'].astype(str).str.contains(tipo_ingenieria, case=False, na=False)]
    if contrato_marco:
        filtro = filtro[filtro['Contrato Marco_x'].astype(str).str.contains(contrato_marco, case=False, na=False)]
    
    return filtro


def resultados_modelo(modelo, precio_total_propuesta, precio_keypro, uf_keypro, hh_keypro, ips, instrumentacion, estudios_disciplinarios,
    estructural, hidraulica, estudios_y_general, piping, hormigones, mecanica, civil, terreno,  general, electricidad):


    variables = [
    "UF/HH", "UF/Entr.", "UF", "Entr.", "Contrato Marco_x", "Cliente_x", "Total\n$;UF/USD", "HH", "Descuento\n[%]", "$;UF;USD", 
    "UF3", "$;UF;USD4", "UF5", "$;UF;USD61", "UF7", "$;UF;USD9", "UF10", "HH30", "Entr.31", "PyA;Promec", "FDA;Propipe", "ER", "JA", 
    "TIPO DE INGENIERÍA", "$;UF;USD12", "$;UF;USD15", "$;UF;USD21", "$;UF;USD27", "$;UF;USD28", "$;UF;USD33", "$;UF;USD36", "$;UF;USD39",
    "IPS_Control de documentos", "IPS_HH Ingeniero A", "IPS_HH Jefe Proyecto", "IPS_HH Lider de disciplina", "IPS_N° ACT", "IPS_N° DOC", 
    "IPS_N° Planos", "IPS_Proyectista A", "Instrumentacion_Control de documentos", "Instrumentacion_HH Ingeniero A", "Instrumentacion_HH Lider de disciplina", 
    "Instrumentacion_N° DOC", "estudios disciplinarios_HH Ingeniero A", "estudios disciplinarios_HH Ingeniero Senior", "estudios disciplinarios_HH Jefe Proyecto", 
    "estudios disciplinarios_HH Lider de disciplina", "estudios disciplinarios_N° ACT", "estudios disciplinarios_N° DOC", "estudios disciplinarios_Proyectista A", 
    "estudios disciplinarios_Total HH", "estructural_HH Ingeniero A", "estructural_HH Ingeniero Senior", "estructural_Proyectista A", "estructural_Total HH", 
    "hidraulica_HH Ingeniero A", "hidraulica_HH Jefe Proyecto", "hidraulica_HH Lider de disciplina", "hidraulica_Total HH", "estudios y general_HH Ingeniero A", 
    "estudios y general_HH Jefe Proyecto", "estudios y general_HH Lider de disciplina", "estudios y general_Total HH", "piping_Control de Proyecto", 
    "piping_Control de documentos", "piping_HH Ingeniero A", "piping_HH Ingeniero B", "piping_HH Ingeniero Senior", "piping_HH Jefe Proyecto", "piping_N° ACT", 
    "piping_N° DOC", "piping_N° Planos", "piping_Proyectista A", "piping_consultor", "hormigones_Control de Proyecto", "hormigones_Control de documentos", 
    "hormigones_HH Ingeniero A", "hormigones_HH Ingeniero Senior", "hormigones_HH Lider de disciplina", "hormigones_N° ACT", "hormigones_N° DOC", 
    "hormigones_N° Planos", "hormigones_consultor", "mecanica_HH Ingeniero A", "mecanica_HH Ingeniero Senior", "mecanica_HH Jefe Proyecto", "civil_Control de documentos", 
    "civil_HH Ingeniero A", "civil_HH Ingeniero B", "civil_HH Ingeniero C", "civil_HH Ingeniero Senior", "civil_HH Jefe Proyecto", "civil_N° ACT", "civil_N° DOC", 
    "civil_N° Planos", "civil_Proyectista A", "civil_consultor", "terreno_HH Ingeniero A", "terreno_HH Lider de disciplina", "terreno_N° Planos", "terreno_Total HH", 
    "general_Calidad", "general_Control de Proyecto", "general_Control de documentos", "general_HH Ingeniero A", "general_HH Ingeniero B", "general_HH Ingeniero Senior", 
    "general_HH Jefe Proyecto", "general_HH Lider de disciplina", "general_N° ACT", "general_N° DOC", "general_N° Planos", "general_Proyectista A", "general_Total HH", 
    "general_consultor", "electricidad_Calidad", "electricidad_Control de Proyecto", "electricidad_Control de documentos", "electricidad_HH Ingeniero A", 
    "electricidad_HH Ingeniero B", "electricidad_HH Ingeniero Senior", "electricidad_HH Jefe Proyecto", "electricidad_N° ACT", "electricidad_N° DOC", 
    "electricidad_N° Planos", "electricidad_consultor"
    ]

    # Crear un diccionario con todas las variables inicializadas en 0
    datos = {var: 0 for var in variables}

    # Convertir en DataFrame (opcional, si necesitas usarlo con pandas)
    df_variables = pd.DataFrame([datos])

    # IPS | instrumentacion | estudios disciplinarios| estructural | hidraulica | estudios y general | piping | hormigones | mecanica | civil | terreno | general | electricidad 

    descuento =0
    precio_penta =0
    uf_penta =0
    desconocido =0
    uf_k1111 =0
    precio_kip =0
    uf_kip = 0
    entr_keypro = 400
    precio_dcl_dcla =0 
    precio_axios =0
    precio_syntec =0
    precio_kri = 0
    precio_corrotek =0
    precio_c2 =0
    precio_c3 =0
    precio_c4 = 0
    


# "MEL-CM": 1, "MLP-CM": 0, "BHP-MEL-CM": 1, "BHP-MEL": 1, "BHP-SP-CM":1, "BHP-Spence":1, "MLP-Penta":0, "MLP":0 }
#"basica": 1, "detalles": 0, "Conceptual": 2,"Prefactibilidad": 3, "Perfil":4, "Factibilidad":5, "Estudio":6, "Servicio":7, "SPS/DPS":8, 
#"Enlace y Terreno":9, "Estudio":10, "Fase Ejecución (EXE)":11 ,"Servicio":12, "IPS":13, "SPS/DPS EXE":14, "IPS SPS/DPS":15, "IPS SPS/DPS EXE":14, "SPS/DPS (Ingeniería de Detalle)":15, "no hay":16, "no claro": 17

#ESTO SE EDITA AAAAAAAAAAAAAAA
    input_inicial = {
        "cliente": 0,
        "contrato_marco": 1 ,
        "tipo_ingenieria": 0,
        "PyA;Promec": 0,
        "FDA;Propipe": 0,
        "ER":0, 
        "JA":0,
        "Total\n$;UF/USD": precio_total_propuesta,
        "Descuento\n[%]" : descuento , 
        "$;UF;USD" : precio_keypro  ,
        "UF3" : uf_keypro,
        "$;UF;USD4" : precio_penta,
        "UF5" : uf_penta,
        "$;UF;USD61" : desconocido, 
        "UF7" : uf_k1111,
      "$;UF;USD9": precio_kip,
      "UF10": uf_kip,
     "HH30": hh_keypro, 
     "Entr.31": entr_keypro,
     "$;UF;USD12": precio_dcl_dcla, 
     "$;UF;USD15": precio_axios,
    "$;UF;USD21": precio_syntec, 
    "$;UF;USD27": precio_kri, 
    "$;UF;USD28": precio_corrotek, 
    "$;UF;USD33": precio_c2,
    "$;UF;USD36": precio_c3,
    "$;UF;USD39": precio_c4
    }
# PRIMERO QUIERO FILTRAR POR LOS INPUTS QUE INGRESE EL USUARIO

    df_inicial = pd.read_excel(r"C:/Users/renata.barrera/OneDrive - KEYPRO/Escritorio/análisis datos/con_HH/prueba_modelo/version_conHH.xlsx", engine="openpyxl", header=2)
    df_filtrado = filtrar_datos(df_inicial, "BHP", "Detalles", "" )
    cantidad_filas = df_filtrado.shape[0]
    if cantidad_filas == 0:
        df_filtrado = filtrar_datos(df_inicial,"BHP", None , "" )





#UF/HH| UF/Entr.| UF | Entr.| Contrato Marco_x | Cliente_x| Total\n$;UF/USD | HH | Descuento\n[%] | $;UF;USD |UF3 | $;UF;USD4| UF5 |$;UF;USD61| UF7 | $;UF;USD9| UF10
# HH30| Entr.31 | PyA;Promec| FDA;Propipe| ER| JA| TIPO DE INGENIERÍA| $;UF;USD12| $;UF;USD15| $;UF;USD21| $;UF;USD27| $;UF;USD28| $;UF;USD33| $;UF;USD36| $;UF;USD39
# IPS_Control de documentos| IPS_HH Ingeniero A| IPS_HH Jefe Proyecto| IPS_HH Lider de disciplina| IPS_N° ACT| IPS_N° DOC| IPS_N° Planos| IPS_Proyectista A| 
# Instrumentacion_Control de documentos| Instrumentacion_HH Ingeniero A| Instrumentacion_HH Lider de disciplina| Instrumentacion_N° DOC| estudios disciplinarios_HH Ingeniero A 
# estudios disciplinarios_HH Ingeniero Senior| estudios disciplinarios_HH Jefe Proyecto| estudios disciplinarios_HH Lider de disciplina| estudios disciplinarios_N° ACT 
# estudios disciplinarios_N° DOC| estudios disciplinarios_Proyectista A| estudios disciplinarios_Total HH| estructural_HH Ingeniero A| estructural_HH Ingeniero Senior
# estructural_Proyectista A| estructural_Total HH| hidraulica_HH Ingeniero A| hidraulica_HH Jefe Proyecto| hidraulica_HH Lider de disciplina| hidraulica_Total HH
# estudios y general_HH Ingeniero A| estudios y general_HH Jefe Proyecto| estudios y general_HH Lider de disciplina| estudios y general_Total HH| piping_Control de Proyecto
# piping_Control de documentos| piping_HH Ingeniero A| piping_HH Ingeniero B| piping_HH Ingeniero Senior| piping_HH Jefe Proyecto| piping_N° ACT| piping_N° DOC
# piping_N° Planos| piping_Proyectista A| piping_consultor| hormigones_Control de Proyecto| hormigones_Control de documentos| hormigones_HH Ingeniero A| 
# hormigones_HH Ingeniero Senior| hormigones_HH Lider de disciplina| hormigones_N° ACT| hormigones_N° DOC| hormigones_N° Planos| hormigones_consultor| 
# piping_Control de Proyecto| piping_Control de documentos| mecanica_HH Ingeniero A| mecanica_HH Ingeniero Senior| mecanica_HH Jefe Proyecto| civil_Control de documentos
# civil_HH Ingeniero A| civil_HH Ingeniero B| civil_HH Ingeniero C| civil_HH Ingeniero Senior| civil_HH Jefe Proyecto| civil_N° ACT| civil_N° DOC| civil_N° Planos
# civil_Proyectista A| civil_consultor| terreno_HH Ingeniero A| terreno_HH Lider de disciplina| terreno_N° Planos| terreno_Total HH| general_Calidad| general_Control de Proyecto
# general_Control de documentos| general_HH Ingeniero A| general_HH Ingeniero B| general_HH Ingeniero Senior| general_HH Jefe Proyecto| general_HH Lider de disciplina
# general_N° ACT| general_N° DOC| general_N° Planos| general_Proyectista A| general_Total HH| general_consultor| electricidad_Calidad| electricidad_Control de Proyecto
# electricidad_Control de documentos| electricidad_HH Ingeniero A| electricidad_HH Ingeniero B| electricidad_HH Ingeniero Senior| electricidad_HH Jefe Proyecto
# electricidad_N° ACT| electricidad_N° DOC| electricidad_N° Planos electricidad_consultor

    valor_a_buscar = "estudios y general"


    def buscar_valor(df, valor_a_buscar):
        df_filtrado = df[df["Disciplina"].astype(str).str.contains(valor_a_buscar, case=False, na=False)]

        columnas_a_promediar = [
        "HH Jefe Proyecto", "consultor", "HH Ingeniero Senior",
        "HH Lider de disciplina", "HH Ingeniero A", "HH Ingeniero B", "HH Ingeniero C",
        "Proyectista A", "Proyectista B", "Dibujante", "Control de documentos",
        "Control de Proyecto", "Calidad", "Total HH", "Disciplina HH reales",
        "N° DOC", "N° Planos", "N° ACT"
        ]

# Crear un diccionario para almacenar los promedios
        promedios = {}

# Calcular y guardar el promedio de cada columna en una variable
        for columna in columnas_a_promediar:
            if columna in df_filtrado.columns:
                promedios[columna] = df_filtrado[columna].mean()
        return promedios

    if estudios_y_general  == 1:
        valor_a_buscar =="estudios y general"
        diccionario = buscar_valor(df_filtrado,valor_a_buscar )
        promedios = {k: float(v) for k, v in diccionario.items()}
        datos["estudios y general_HH Ingeniero A"] = promedios['HH Ingeniero A']
        datos["estudios y general_HH Jefe Proyecto"] = promedios['HH Jefe Proyecto']
        datos["estudios y general_HH Lider de disciplina"] = promedios['HH Lider de disciplina']
        datos[ "estudios y general_Total HH"] = promedios['Total HH']

        print("ESTDUIOS Y GENERAL ")
        print(datos["estudios y general_HH Ingeniero A"])
        print( datos["estudios y general_HH Jefe Proyecto"])
        print(datos["estudios y general_HH Lider de disciplina"])
        print(datos[ "estudios y general_Total HH"])
        print(promedios)

    if ips  == 1:
        valor_a_buscar =="IPS"
        diccionario = buscar_valor(df_filtrado,valor_a_buscar )
        promedios = {k: float(v) for k, v in diccionario.items()}
        datos[ "IPS_Control de documentos"] = promedios['Control de documentos']
        datos["IPS_HH Ingeniero A"] = promedios['HH Ingeniero A']
        datos["IPS_HH Jefe Proyecto"] = promedios['HH Jefe Proyecto']
        datos[ "IPS_HH Lider de disciplina"] = promedios['HH Lider de disciplina']
        datos[ "IPS_N° ACT"] = promedios['N° ACT']
        datos["IPS_N° DOC"] = promedios['N° DOC']
        datos["IPS_N° Planos"] = promedios['N° Planos']
        datos[ "IPS_Proyectista A"] = promedios['Proyectista A']


    if instrumentacion  == 1:
        valor_a_buscar =="instrumentacion"
        diccionario = buscar_valor(df_filtrado,valor_a_buscar )
        promedios = {k: float(v) for k, v in diccionario.items()}
        datos["Instrumentacion_Control de documentos"] = promedios['Control de documentos']
        datos["Instrumentacion_HH Ingeniero A"] = promedios['HH Ingeniero A']
        datos["Instrumentacion_HH Lider de disciplina"] = promedios['HH Jefe Proyecto']
        datos["Instrumentacion_N° DOC" ] = promedios['HH Lider de disciplina']

    



        print(promedios)

    if estudios_disciplinarios  == 1:
        valor_a_buscar =="estudios y general"
        diccionario = buscar_valor(df_filtrado,valor_a_buscar )
        promedios = {k: float(v) for k, v in diccionario.items()}
        datos["estudios disciplinarios_HH Ingeniero A"] = promedios['HH Ingeniero A']
        datos["estudios disciplinarios_HH Ingeniero Senior"] = promedios['HH Ingeniero Senior']
        datos["estudios disciplinarios_HH Jefe Proyecto"] = promedios['HH Jefe Proyecto']
        datos["estudios disciplinarios_HH Lider de disciplina" ] = promedios['HH Lider de disciplina']
        datos["estudios disciplinarios_N° ACT"] = promedios['N° ACT']
        datos["estudios disciplinarios_N° DOC"] = promedios['N° DOC']
        datos["estudios disciplinarios_Proyectista A"] = promedios['Proyectista A']
        datos["estudios disciplinarios_Total HH" ] = promedios['Total HH']


        print(promedios)

    if hidraulica  == 1:
        valor_a_buscar =="estudios y general"
        diccionario = buscar_valor(df_filtrado,valor_a_buscar )
        promedios = {k: float(v) for k, v in diccionario.items()}
        datos["hidraulica_HH Ingeniero A"] = promedios['HH Ingeniero A']
        datos["hidraulica_HH Jefe Proyecto"] = promedios['HH Jefe Proyecto']
        datos["hidraulica_HH Lider de disciplina"] = promedios['HH Lider de disciplina']
        datos["hidraulica_Total HH" ] = promedios['Total HH']

        print(promedios)

    if hormigones  == 1:
        valor_a_buscar =="estudios y general"
        diccionario = buscar_valor(df_filtrado,valor_a_buscar )
        promedios = {k: float(v) for k, v in diccionario.items()}
        datos["hormigones_Control de Proyecto"] = promedios['Control de Proyecto']
        datos["hormigones_Control de documentos"] = promedios['Control de documentos']
        datos["hormigones_HH Ingeniero A"] = promedios['HH Ingeniero A']
        datos["hormigones_HH Ingeniero Senior" ] = promedios['HH Ingeniero Senior']
        datos["hormigones_HH Lider de disciplina"] = promedios['HH Lider de disciplina']
        datos["hormigones_N° ACT"] = promedios['N° ACT']
        datos["hormigones_N° DOC"] = promedios['N° DOC']
        datos["hormigones_N° Planos"] = promedios['N° Planos']
        datos["hormigones_consultor"] = promedios['consultor']






        print(promedios)

    if piping  == 1:
        valor_a_buscar =="estudios y general"
        diccionario = buscar_valor(df_filtrado,valor_a_buscar )
        promedios = {k: float(v) for k, v in diccionario.items()}

        datos["piping_Control de Proyecto"] = promedios['Control de Proyecto']
        datos["piping_Control de documentos"] = promedios['Control de documentos']
        datos["piping_HH Ingeniero A"] = promedios['HH Ingeniero A']
        datos["piping_HH Ingeniero B"] = promedios['HH Ingeniero B']
        datos["piping_HH Ingeniero Senior"] = promedios['HH Ingeniero Senior']
        datos["piping_HH Jefe Proyecto"] = promedios['HH Jefe Proyecto']
        datos["piping_N° ACT"] = promedios['N° ACT']
        datos["piping_N° DOC"] = promedios['N° DOC']
        datos[ "piping_N° Planos"] = promedios['N° Planos']
        datos["piping_Proyectista A"] = promedios['Proyectista A']
        datos[ "piping_consultor"] = promedios['consultor']

        print(promedios)

    if mecanica  == 1:
        valor_a_buscar =="estudios y general"
        diccionario = buscar_valor(df_filtrado,valor_a_buscar )
        promedios = {k: float(v) for k, v in diccionario.items()}
        datos["mecanica_HH Ingeniero A"] = promedios['HH Ingeniero A']
        datos["mecanica_HH Ingeniero Senior"] = promedios['HH Ingeniero Senior']
        datos["mecanica_HH Jefe Proyecto"] = promedios['HH Jefe Proyecto']

        print(promedios)

    if civil  == 1:
        valor_a_buscar =="estudios y general"
        diccionario = buscar_valor(df_filtrado,valor_a_buscar )
        promedios = {k: float(v) for k, v in diccionario.items()}

        datos["civil_Control de documentos"] = promedios['HH Ingeniero A']
        datos["civil_HH Ingeniero A"] = promedios['HH Ingeniero Senior']
        datos["civil_HH Ingeniero B"] = promedios['HH Jefe Proyecto']
        datos["civil_HH Ingeniero C"] = promedios['HH Ingeniero A']
        datos["civil_HH Ingeniero Senior"] = promedios['HH Ingeniero Senior']
        datos["civil_HH Jefe Proyecto"] = promedios['HH Jefe Proyecto']

        datos["civil_N° ACT"] = promedios['N° ACT']
        datos["civil_N° DOC"] = promedios['N° DOC']
        datos["civil_N° Planos"] = promedios['N° Planos']
        datos["civil_Proyectista A"] = promedios['Proyectista A']
        datos["civil_consultor"] = promedios['consultor']

        print(promedios)

    if terreno  == 1:
        valor_a_buscar =="estudios y general"
        diccionario = buscar_valor(df_filtrado,valor_a_buscar )
        promedios = {k: float(v) for k, v in diccionario.items()}

        datos["terreno_HH Ingeniero A"] = promedios['HH Ingeniero A']
        datos["terreno_HH Lider de disciplina"] = promedios['HH Lider de disciplina']
        datos["terreno_N° Planos"] = promedios['N° Planos']
        datos["terreno_Total HH"] = promedios['Total HH']


        print(promedios)

    if general  == 1:
        valor_a_buscar =="estudios y general"
        diccionario = buscar_valor(df_filtrado,valor_a_buscar )
        promedios = {k: float(v) for k, v in diccionario.items()}

        datos["general_Calidad"] = promedios['Calidad']
        datos["general_Control de Proyecto"] = promedios['Control de Proyecto']
        datos["general_Control de documentos"] = promedios['Control de documentos']
        datos["general_HH Ingeniero A"] = promedios['HH Ingeniero A']
        datos["general_HH Ingeniero B"] = promedios['HH Ingeniero B']
        datos["general_HH Ingeniero Senior"] = promedios['HH Ingeniero Senior']
        datos["general_HH Jefe Proyecto"] = promedios['HH Jefe Proyecto']
        datos["general_HH Lider de disciplina"] = promedios['HH Lider de disciplina']

        datos["general_N° ACT"] = promedios['N° ACT']
        datos["general_N° DOC"] = promedios['N° DOC']
        datos["general_N° Planos"] = promedios['N° Planos']
        datos["general_Proyectista A"] = promedios['N° Planos']
        datos["general_Total HH"] = promedios['Total HH']
        datos["general_consultor"] = promedios['consultor']



        print(promedios)

    if electricidad  == 1:
        valor_a_buscar =="estudios y general"
        diccionario = buscar_valor(df_filtrado,valor_a_buscar )
        promedios = {k: float(v) for k, v in diccionario.items()}

        datos["electricidad_Calidad"] = promedios['Calidad']
        datos["electricidad_Control de Proyecto"] = promedios['Control de Proyecto']
        datos["electricidad_Control de documentos"] = promedios['Control de documentos']
        datos["electricidad_HH Ingeniero A"] = promedios['HH Ingeniero A']
        datos["electricidad_HH Ingeniero B"] = promedios['HH Ingeniero B']
        datos["electricidad_HH Ingeniero Senior"] = promedios['HH Ingeniero Senior']
        datos["electricidad_HH Jefe Proyecto"] = promedios['HH Jefe Proyecto']
        datos["electricidad_N° ACT"] = promedios['N° ACT']
        datos["electricidad_N° DOC",] = promedios['N° DOC']
        datos["electricidad_N° Planos"] = promedios['N° Planos']
        datos["electricidad_consultor"] = promedios['consultor'] 

        print(promedios)

    if estructural  == 1:
        valor_a_buscar =="estudios y general"
        diccionario = buscar_valor(df_filtrado,valor_a_buscar )
        promedios = {k: float(v) for k, v in diccionario.items()}
        datos["estructural_HH Ingeniero A"] = promedios['HH Ingeniero A']
        datos["estructural_HH Ingeniero Senior"] = promedios['HH Ingeniero Senior']
        datos["estructural_Proyectista A"] = promedios['Proyectista A']
        datos["estructural_Total HH"] = promedios['Total HH']



        print(promedios)

    uf_hh = precio_total_propuesta/hh_keypro
    uf_entr = precio_total_propuesta/entr_keypro


    nuevo_proyecto = np.array([[uf_hh, uf_entr, uf_keypro, entr_keypro, input_inicial["contrato_marco"], input_inicial["cliente"], input_inicial["Total\n$;UF/USD"], hh_keypro, input_inicial["Descuento\n[%]"], input_inicial["$;UF;USD"], 
        input_inicial["UF3"], input_inicial["$;UF;USD4"], input_inicial["UF5"], input_inicial["$;UF;USD61"], input_inicial["UF7"] , input_inicial ["$;UF;USD9"],input_inicial["UF10"], input_inicial["HH30"], input_inicial["Entr.31"] , 0, 1, 0, 1, 
        input_inicial["tipo_ingenieria"], input_inicial["$;UF;USD12"] , input_inicial["$;UF;USD15"] , input_inicial["$;UF;USD21"] , input_inicial["$;UF;USD27"], input_inicial["$;UF;USD28"], input_inicial["$;UF;USD33"], input_inicial["$;UF;USD36"], input_inicial["$;UF;USD39"],
        datos["IPS_Control de documentos"],datos["IPS_HH Ingeniero A"] ,datos["IPS_HH Jefe Proyecto"] , datos["IPS_HH Lider de disciplina"], datos["IPS_N° ACT"],datos["IPS_N° DOC"] , 
        datos["IPS_N° Planos"], datos["IPS_Proyectista A"], datos["Instrumentacion_Control de documentos"], datos["Instrumentacion_HH Ingeniero A"], datos["Instrumentacion_HH Lider de disciplina"], 
        datos["Instrumentacion_N° DOC"], datos["estudios disciplinarios_HH Ingeniero A"], datos["estudios disciplinarios_HH Ingeniero Senior"], datos["estudios disciplinarios_HH Jefe Proyecto"], 
        datos["estudios disciplinarios_HH Lider de disciplina"], datos["estudios disciplinarios_N° ACT"], datos["estudios disciplinarios_N° DOC"], datos["estudios disciplinarios_Proyectista A"],
        datos["estudios disciplinarios_Total HH"], datos["estructural_HH Ingeniero A"], datos["estructural_HH Ingeniero Senior"], datos["estructural_Proyectista A"], datos["estructural_Total HH"],
        datos["hidraulica_HH Ingeniero A"], datos["hidraulica_HH Jefe Proyecto"], datos["hidraulica_HH Lider de disciplina"], datos["hidraulica_Total HH"], datos["estudios y general_HH Ingeniero A"], 
        datos["estudios y general_HH Jefe Proyecto"], datos["estudios y general_HH Lider de disciplina"], datos["estudios y general_Total HH"], datos["piping_Control de Proyecto"], 
        datos["piping_Control de documentos"], datos["piping_HH Ingeniero A"], datos["piping_HH Ingeniero B"], datos["piping_HH Ingeniero Senior"], datos["piping_HH Jefe Proyecto"], datos["piping_N° ACT"], 
        datos["piping_N° DOC"], datos["piping_N° Planos"], datos["piping_Proyectista A"], datos["piping_consultor"], datos["hormigones_Control de Proyecto"], datos["hormigones_Control de documentos"],
        datos["hormigones_HH Ingeniero A"], datos["hormigones_HH Ingeniero Senior"], datos["hormigones_HH Lider de disciplina"], datos["hormigones_N° ACT"], datos["hormigones_N° DOC"], datos["hormigones_N° Planos"],
        datos["hormigones_consultor"],datos["piping_Control de Proyecto"],	datos["piping_Control de documentos"], 
        datos["mecanica_HH Ingeniero A"], datos["mecanica_HH Ingeniero Senior"], datos["mecanica_HH Jefe Proyecto"], datos["civil_Control de documentos"], datos["civil_HH Ingeniero A"], 
        datos["civil_HH Ingeniero B"], datos["civil_HH Ingeniero C"], datos["civil_HH Ingeniero Senior"], datos["civil_HH Jefe Proyecto"], datos["civil_N° ACT"], datos["civil_N° DOC"],
        datos["civil_N° Planos"], datos["civil_Proyectista A"], datos["civil_consultor"], datos["terreno_HH Ingeniero A"], datos["terreno_HH Lider de disciplina"], datos["terreno_N° Planos"], datos["terreno_Total HH"], 
        datos["general_Calidad"], datos["general_Control de Proyecto"], datos["general_Control de documentos"], datos["general_HH Ingeniero A"], datos["general_HH Ingeniero B"], datos["general_HH Ingeniero Senior"], 
        datos["general_HH Jefe Proyecto"], datos["general_HH Lider de disciplina"], datos["general_N° ACT"], datos["general_N° DOC"], datos["general_N° Planos"], datos["general_Proyectista A"], datos["general_Total HH"], 
        datos["general_consultor"], datos["electricidad_Calidad"], datos["electricidad_Control de Proyecto"], datos["electricidad_Control de documentos"], datos["electricidad_HH Ingeniero A"], 
        datos["electricidad_HH Ingeniero B"], datos["electricidad_HH Ingeniero Senior"], datos["electricidad_HH Jefe Proyecto"], datos["electricidad_N° ACT"], datos["electricidad_N° DOC"], 
        datos["electricidad_N° Planos"], datos["electricidad_consultor"],0]])


    # Obtener la probabilidad de que el proyecto sea "Ganado"
    probabilidad_ganar = modelo.predict_proba(nuevo_proyecto)[:, 1]

    # Obtener la predicción (0 = no ganado, 1 = ganado)
    prediccion = modelo.predict(nuevo_proyecto)

    #print(X.describe())
    #print(nuevo_proyecto)

    print("🔹 Probabilidad de ganar:", probabilidad_ganar[0])
    print("🔹 Predicción del modelo:", "Ganado" if prediccion[0] == 1 else "No ganado")
    return(probabilidad_ganar[0])



# resultados_modelo(modelo, precio_total_propuesta, precio_keypro, uf_keypro, hh_keypro, ips, instrumentacion, estudios_disciplinarios,
# estructural, hidraulica, estudios_y_general, piping, hormigones, mecanica, civil, terreno,  general, electricidad)
#resultados_modelo(modelo,986211, 986211,25, 300, 0,1,1,0,1,1,0,0,1,0,0,0,0)
#resultados_modelo(modelo,986211, 986211,25, 200, 0,1,1,0,1,1,0,0,1,0,0,0,0)    #0,66
#resultados_modelo(modelo,1972422, 1972422,25, 200, 0,1,1,0,1,1,0,0,1,0,0,0,0)  #0,51
#resultados_modelo(modelo,1972422, 1972422,51, 200, 0,1,1,0,1,1,0,0,1,0,0,0,0) #0,51
#resultados_modelo(modelo,19, 19,0.005, 200, 0,1,1,0,1,1,0,0,1,0,0,0,0) #0,79




#resultados_modelo(modelo,2958633, 2958633,77, 600, 0,1,1,0,1,1,0,0,1,0,0,0,0)
#resultados_modelo(modelo,2958633, 2958633,77,100,0,1,1,0,1,1,0,0,1,0,0,0,0)

# nuevo_proyecto = np.array([[ ufhh , uf_entr, uf , entr , contr_marco , cliente , Total , hh, ufusd, uf3]])
def resultados_modelo2(modelo, precio_total_propuesta, precio_keypro, entr, cliente, hh):
    uf = int(precio_total_propuesta)/39000
    print("ESTAS SON LAS UF")
    print(uf)
    uf_hh =  uf/hh
    uf_entr = uf/entr
    uf_keypro = int(precio_keypro)/39000
    print("ESTAS SON LAS UF KEYPRO")
    print(uf_keypro)
    nuevo_proyecto = np.array([[uf_hh,uf_entr,uf,entr ,1, 1, precio_total_propuesta, hh, precio_keypro, uf_keypro  ]])

    # Obtener la probabilidad de que el proyecto sea "Ganado"
    probabilidad_ganar = modelo.predict_proba(nuevo_proyecto)[:, 1]

    # Obtener la predicción (0 = no ganado, 1 = ganado)
    prediccion = modelo.predict(nuevo_proyecto)

    #print(X.describe())
    #print(nuevo_proyecto)

    print("🔹 Probabilidad de ganar:", probabilidad_ganar[0])
    print("🔹 Predicción del modelo:", "Ganado" if prediccion[0] == 1 else "No ganado")
    return(probabilidad_ganar[0])

def resultados_modelo3(modelo, precio_total_propuesta, precio_keypro, entr, cliente, hh, mecanica,piping, electricidad, estrutural,
                       estudiosygeneral, instrumentacion, hormigones, general, hidraulica, estudiosdisciplinarios, civil, ips, terreno ):
    uf = int(precio_total_propuesta)/39000
    print("ESTAS SON LAS UF")
    print(uf)
    uf_hh =  uf/hh
    uf_entr = uf/entr
    uf_keypro = int(precio_keypro)/39000
    print("ESTAS SON LAS UF KEYPRO")
    print(uf_keypro)
    nuevo_proyecto = np.array([[uf_hh,uf_entr,uf,entr ,1, 1, precio_total_propuesta, hh, precio_keypro, uf_keypro, mecanica,piping, electricidad, estrutural,
                       estudiosygeneral, instrumentacion, hormigones, general, hidraulica, estudiosdisciplinarios, civil, ips, terreno,0  ]])

    # Obtener la probabilidad de que el proyecto sea "Ganado"
    probabilidad_ganar = modelo.predict_proba(nuevo_proyecto)[:, 1]

    # Obtener la predicción (0 = no ganado, 1 = ganado)
    prediccion = modelo.predict(nuevo_proyecto)

    #print(X.describe())
    #print(nuevo_proyecto)

    print("🔹 Probabilidad de ganar:", probabilidad_ganar[0])
    print("🔹 Predicción del modelo:", "Ganado" if prediccion[0] == 1 else "No ganado")
    return(probabilidad_ganar[0])


# UF/HH, UF/Entr., UF, Entr., Contrato Marco_x, Cliente_x , Total\n$;UF/USD, HH , $;UF;USD ,  UF3 ,  TIPO DE INGENIERÍA,
#       tarifa jefe proyecto CLP , tarifa consultor CLP , tarifa ingeniero senior CLP ,	 tarifa jefe disciplina CLP ,	
#   tarifa ingeniero A CLP ,	 tarifa ingeniero B CLP , tarifa proyectista CLP , tarifa dibujante CLP , tarifa control documentos CLP ,
#  tarifa control de proyectos CLP , tarifa calidad CLP ,  HH totales jefe proyecto ,	 HH totales ingeniero senior ,	HH totales lider de disciplina , 	
#  HH totales ingeniero A, HH totales proyectista A, HH totales control documentos , HH totales control proyecto,
# Total HH mecanica, Total HH piping, Total HH electricidad, Total HH estructural, Total HH estudios y general,	
# Total HH instrumentacion, Total HH hormigones, Total HH general ,	Total HH hidraulica, Total HH estudios disciplinarios,
#  Total HH civil,	Total HH IPS,	Total HH terreno

def resultados_modelo4(modelo, precio_total_propuesta, precio_keypro, entr, cliente, hh, mecanica,piping, electricidad, estrutural,
                       estudiosygeneral, instrumentacion, hormigones, general, hidraulica, estudiosdisciplinarios, civil, ips, terreno,
                        tfa_jefeproyecto, tfa_consultor, tfa_ingsenior, tfa_jefedisciplina, tfa_ingA, tfa_ingB, tfa_proyectista,
                         tfa_dibujante, tfa_controldctos, tfa_controlproyectos, tfa_calidad, hh_jefeproyecto, hh_ingsenior,
                          hh_liderdisciplina, hh_ingA, hh_proyectistaA, hh_controldoc, hh_controlproyecto ):
    uf = int(precio_total_propuesta)/39000
    print("ESTAS SON LAS UF")
    print(uf)
    uf_hh =  uf/hh
    uf_entr = uf/entr
    uf_keypro = int(precio_keypro)/39000
    print("ESTAS SON LAS UF KEYPRO")
    print(uf_keypro)
    nuevo_proyecto = np.array([[uf_hh,uf_entr,uf,entr ,1, 1, precio_total_propuesta, hh, precio_keypro, uf_keypro,1, tfa_jefeproyecto,
                                tfa_consultor, tfa_ingsenior,  tfa_jefedisciplina,  tfa_ingA,  tfa_ingB, tfa_proyectista, tfa_dibujante,
                                tfa_controldctos,  tfa_controlproyectos,tfa_calidad,  hh_jefeproyecto, hh_ingsenior,  hh_liderdisciplina, 
                                hh_ingA, hh_proyectistaA, hh_controldoc, hh_controlproyecto, mecanica,piping, electricidad, estrutural,
                       estudiosygeneral, instrumentacion, hormigones, general, hidraulica, estudiosdisciplinarios, civil, ips, terreno ]])

    # Obtener la probabilidad de que el proyecto sea "Ganado"
    probabilidad_ganar = modelo.predict_proba(nuevo_proyecto)[:, 1]

    # Obtener la predicción (0 = no ganado, 1 = ganado)
    prediccion = modelo.predict(nuevo_proyecto)

    #print(X.describe())
    #print(nuevo_proyecto)

    print("🔹 Probabilidad de ganar:", probabilidad_ganar[0])
    print("🔹 Predicción del modelo:", "Ganado" if prediccion[0] == 1 else "No ganado")
    return(probabilidad_ganar[0])
