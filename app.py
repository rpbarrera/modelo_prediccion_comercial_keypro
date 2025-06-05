from flask import Flask, render_template, request
from funciones.funcion_modelo_con_inputs import resultados_modelo
from funciones.funcion_modelo_con_inputs import resultados_modelo2
from funciones.funcion_modelo_con_inputs import resultados_modelo3
from funciones.funcion_modelo_con_inputs import resultados_modelo4


import joblib


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = {}

    if request.method == "POST":
        data["cliente"] = request.form.get("cliente", "")
        data["proveedores"] = request.form.get("proveedores", "")
        data["HH"] = request.form.get("HH", "")
        data["entregables"] = request.form.get("entregables", "")
        data["precio_propuesta"] = request.form.get("precio_propuesta", "")
        data["precio_keypro"] = request.form.get("precio_keypro", "")
        data["disciplinas"] = request.form.get("disciplinas", "").split(',')

       
        data["hh_jefe_proyecto"] = [
            request.form.get("hh_disciplina1_jefe_proyecto", ""),
            request.form.get("hh_disciplina2_jefe_proyecto", ""),
            request.form.get("hh_disciplina3_jefe_proyecto", ""),
            request.form.get("hh_disciplina4_jefe_proyecto", ""),
            request.form.get("hh_disciplina5_jefe_proyecto", "")
        ]

        print("Datos recibidos:", data)
        print("ESTE ES EL CLIENTE")
        print(data["cliente"])
        print(data["HH"])
        modelo = joblib.load("modelo_simple.pkl")
        resultado = resultados_modelo2(modelo, int(data["precio_propuesta"]), int(data["precio_keypro"]), int(data["entregables"]), 1,int(data["HH"]) )
        # resultados_modelo(modelo, precio_total_propuesta, precio_keypro, uf_keypro, hh_keypro, ips, instrumentacion, estudios_disciplinarios,
        # estructural, hidraulica, estudios_y_general, piping, hormigones, mecanica, civil, terreno,  general, electricidad)
        return render_template("resultado.html", resultado=resultado)

    return render_template("index.html", data=data)


@app.route("/modelo_tipos_disciplinas", methods=["GET", "POST"])
def info():
    data = {}

    if request.method == "POST":
        data["cliente"] = request.form.get("cliente", "")
        data["proveedores"] = request.form.get("proveedores", "")
        data["HH"] = request.form.get("HH", "")
        data["entregables"] = request.form.get("entregables", "")
        data["precio_propuesta"] = request.form.get("precio_propuesta", "")
        data["precio_keypro"] = request.form.get("precio_keypro", "")
        data["disciplinas"] = request.form.get("disciplinas", "").split(',')
        print("Datos recibidos:", data)
        modelo = joblib.load("modelo_hh_sintarifas.pkl")
        print(int(data["disciplinas"][0]))
        resultado = resultados_modelo3(modelo, int(data["precio_propuesta"]), int(data["precio_keypro"]), int(data["entregables"]), 1,int(data["HH"]),
                                       int(data["disciplinas"][0]), int(data["disciplinas"][1]), int(data["disciplinas"][2]), int(data["disciplinas"][3]),
                                         int(data["disciplinas"][4]),int(data["disciplinas"][5]), int(data["disciplinas"][6]), int(data["disciplinas"][7]),
                                           int(data["disciplinas"][8]), int(data["disciplinas"][9]), int(data["disciplinas"][10]), int(data["disciplinas"][11]),
                                             int(data["disciplinas"][12]))
        return render_template("resultado.html", resultado=resultado)
       

    return render_template("modelo_tipos_disciplinas.html")

@app.route("/modelo_con_todo", methods=["GET", "POST"])
def ayuda():

    data = {}
    if request.method == "POST":
        data["cliente"] = request.form.get("cliente", "")
        data["proveedores"] = request.form.get("proveedores", "")
        data["HH"] = request.form.get("HH", "")
        data["entregables"] = request.form.get("entregables", "")
        data["precio_propuesta"] = request.form.get("precio_propuesta", "")
        data["precio_keypro"] = request.form.get("precio_keypro", "")
        data["disciplinas"] = request.form.get("disciplinas", "").split(',')

        data["tarifa_jefeproyecto"] = request.form.get("tarifa_jefeproyecto", "")
        data["tarifa_consultor"] = request.form.get("tarifa_consultor", "")
        data["tarifa_ingsenior"] = request.form.get("tarifa_ingsenior", "")
        data["tarifa_jefedisciplina"] = request.form.get("tarifa_jefedisciplina", "")
        data["tarifa_ingenieroA"] = request.form.get("tarifa_ingenieroA", "")
        data["tarifa_ingenieroB"] = request.form.get("tarifa_ingenieroB", "")
        data["tarifa_proyectista"] = request.form.get("tarifa_proyectista", "")
        data["tarifa_dibujante"] = request.form.get("tarifa_dibujante", "")
        data["tarifa_controldocumentos"] = request.form.get("tarifa_controldocumentos", "")
        data["tarifa_controlproyectos"] = request.form.get("tarifa_controlproyectos", "")
        data["tarifa_calidad"] = request.form.get("tarifa_calidad", "")

    
        data["hh_jefeproyecto"] = request.form.get("hh_jefeproyecto", "")
        data["hh_ingenierosenior"] = request.form.get("hh_ingenierosenior", "")
        data["hh_liderdisciplina"] = request.form.get("hh_liderdisciplina", "")
        data["hh_ingenieroA"] = request.form.get("hh_ingenieroA", "")
        data["hh_proyectistaA"] = request.form.get("hh_proyectistaA", "")
        data["hh_controldocumentos"] = request.form.get("hh_controldocumentos", "")
        data["hh_controlproyecto"] = request.form.get("hh_controlproyecto", "")
    

        data["disciplinas"] = [
                request.form.get("hh_mecanica", ""),
                request.form.get("hh_piping", ""),
                request.form.get("hh_electricidad", ""),
                request.form.get("hh_estructural", ""),
                request.form.get("hh_estudiosygeneral", ""),
                request.form.get("hh_instrumentacion", ""),
                request.form.get("hh_hormigones", ""),
                request.form.get("hh_general", ""),
                request.form.get("hh_hidraulica", ""),
                request.form.get("hh_estudiosdisciplinarios", ""),

                request.form.get("hh_civil", ""),
                request.form.get("hh_ips", ""),
                request.form.get("hh_terreno", "")
                
                ]
        
        modelo = joblib.load("modelo_tarifa_hh_disciplinas.pkl")
        """modelo, precio_total_propuesta, precio_keypro, entr, cliente, hh, mecanica,piping, electricidad, estrutural,
                        estudiosygeneral, instrumentacion, hormigones, general, hidraulica, estudiosdisciplinarios, civil, ips, terreno,
                            tfa_jefeproyecto, tfa_consultor, tfa_ingsenior, tfa_jefedisciplina, tfa_ingA, tfa_ingB, tfa_proyectista,
                            tfa_dibujante, tfa_controldctos, tfa_controlproyectos, tfa_calidad, hh_jefeproyecto, hh_ingsenior,
                            hh_liderdisciplina, hh_ingA, hh_proyectistaA, hh_controldoc, hh_controlproyecto"""
        print("MECANICA")
        print(data)
        


        resultado = resultados_modelo4(modelo, int(data["precio_propuesta"]), int(data["precio_keypro"]), int(data["entregables"]), 1,int(data["HH"]),
                                        int(data["disciplinas"][0]), int(data["disciplinas"][1]), int(data["disciplinas"][2]), int(data["disciplinas"][3]),
                                            int(data["disciplinas"][4]),int(data["disciplinas"][5]), int(data["disciplinas"][6]), int(data["disciplinas"][7]),
                                            int(data["disciplinas"][8]), int(data["disciplinas"][9]), int(data["disciplinas"][10]), int(data["disciplinas"][11]),
                                                int(data["disciplinas"][12]), int(data["tarifa_jefeproyecto"]), int(data["tarifa_consultor"]),
                                                int(data["tarifa_ingsenior"]), int(data["tarifa_jefedisciplina"]), int(data["tarifa_ingenieroA"]),
                                                int(data["tarifa_ingenieroB"]), int(data["tarifa_proyectista"]), int(data["tarifa_dibujante"]), int(data["tarifa_controldocumentos"]),
                                                int(data["tarifa_controlproyectos"]), int(data["tarifa_calidad"]), int(data["hh_jefeproyecto"]),int(data["hh_ingenierosenior"]), 
                                                int(data["hh_liderdisciplina"]), int(data["hh_ingenieroA"]),int(data["hh_proyectistaA"]), int(data["hh_controldocumentos"]),
                                                int(data["hh_controlproyecto"]) )
        return render_template("resultado.html", resultado=resultado)
     #"UF/HH", "UF/Entr.","UF", "Entr.", "Contrato Marco_x","Cliente_x","Total\n$;UF/USD", "HH","$;UF;USD", "UF3", "TIPO DE INGENIERÍA",
         #         "tarifa jefe proyecto CLP","tarifa consultor CLP","tarifa ingeniero senior CLP",	"tarifa jefe disciplina CLP",	
          #        "tarifa ingeniero A CLP",	"tarifa ingeniero B CLP","tarifa proyectista CLP","tarifa dibujante CLP","tarifa control documentos CLP",
           #             	"tarifa control de proyectos CLP",	"tarifa calidad CLP", "HH totales jefe proyecto",	"HH totales ingeniero senior",	"HH totales lider de disciplina", 	
            #                "HH totales ingeniero A", "HH totales proyectista A", "HH totales control documentos", "HH totales control proyecto",
             #               "Total HH mecanica", "Total HH piping", "Total HH electricidad","Total HH estructural", "Total HH estudios y general",	
              #               "Total HH instrumentacion", "Total HH hormigones",	"Total HH general",	"Total HH hidraulica",	"Total HH estudios disciplinarios",
               #                  	"Total HH civil",	"Total HH IPS",	"Total HH terreno"

    return render_template("modelo_con_todo.html")
    

if __name__ == "__main__":
    app.run(debug=True)
