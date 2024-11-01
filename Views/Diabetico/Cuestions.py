import flet as ft
import json
from DAO.Factory.ConexionManager import ConexionManager


class Cuestions():

    def __init__(self, page:ft.Page, id):
        self.id = id
        self.page = page
        self.conexion = ConexionManager()
        self.title = ft.Text(
            value="Encuesta Diabeticos",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
        )
        self.radios = [
            #2
            ft.Radio(value="Si", label="Si"),
            ft.Radio(value="No", label="No"),
            #5
            ft.Radio(value="Tipo 1", label="Tipo 1",visible=False),
            ft.Radio(value="Tipo 2", label="Tipo 2",visible=False),
            ft.Radio(value="No estoy seguro", label="No estoy seguro",visible=False),
            #7
            ft.Radio(value="Si2", label="Si",visible=False),
            ft.Radio(value="No2", label="No",visible=False),
            #12
            ft.Radio(value="Fatiga", label="Fatiga",visible=False),
            ft.Radio(value="Orinar con frecuencia", label="Orinar con frecuencia",visible=False),
            ft.Radio(value="Sed excesiva", label="Sed excesiva",visible=False),
            ft.Radio(value="Vision borrosa", label="Vision borrosa",visible=False),
            ft.Radio(value="No he tenido ninguno", label="No he tenido ninguno",visible=False),
 
            #16
            ft.Radio(value="Insulina", label="Insulina",visible=False),
            ft.Radio(value="Medicamentos orales", label="Medicamentos orales",visible=False),
            ft.Radio(value="Dieta especial", label="Dieta especial",visible=False),
            ft.Radio(value="Ejercicio regular", label="Ejercicio regular",visible=False),
            #20
            ft.Radio(value="No lo creo necesario", label="No lo creo necesario",visible=False),
            ft.Radio(value="No puedo contestarlo", label="No puedo contestarlo",visible=False),
            ft.Radio(value="No tengo acceso a medicamentos", label="No tengo acceso a medicamentos",visible=False),
            ft.Radio(value="Otro motivo", label="Otro motivo",visible=False),
            
            #23
            ft.Radio(value="Diario", label="Diario",visible=False),
            ft.Radio(value="A veces", label="A veces",visible=False),
            ft.Radio(value="Raramente", label="Raramente",visible=False),
           #25
            ft.Radio(value="Si3", label="Si",visible=False),
            ft.Radio(value="No3", label="No",visible=False),
            #27
            ft.Radio(value="Si4", label="Si",visible=False),
            ft.Radio(value="No4", label="No",visible=False),
            #30
            ft.Radio(value="Menos de 100mg/dL", label="Menos de 100mg/dL",visible=False),
            ft.Radio(value="Entre 100mg/dL y 125mg/dL", label="Entre 100mg/dL y 125mg/dL",visible=False),
            ft.Radio(value="Mas de 126mg/dL", label="Mas de 126mg/dL",visible=False),
            #32
            ft.Radio(value="Si5", label="Si",visible=False),
            ft.Radio(value="No5", label="No",visible=False),
            #33
            ft.Radio(value="Seleccione", label="Seleccione",visible=False),
            ]
        self.calendarioupdated = ''
        self.combinaciones = {
            ('Si', 'Tipo 1', 'Si2', 'Insulina'): "Estas manejando adecuadamente, pero se recomienda un monitoreo constante",
            ('Si', 'Tipo 1', 'Si2', 'Medicamentos orales'): "Estas manejando adecuadamente, pero se recomienda un monitoreo constante",
            ('Si', 'Tipo 1', 'Si2', 'Dieta especial'): "Estas manejando adecuadamente, pero se recomienda un monitoreo constante",
            ('Si', 'Tipo 1', 'Si2', 'Ejercicio regular'): "Estas manejando adecuadamente, pero se recomienda un monitoreo constante",
            ('Si', 'Tipo 1', 'Si2', 'Ninguno'): "es urgente empezar tu tratamiento para manejar tu diabetes",
            ('Si', 'Tipo 1', 'No', 'No lo creo necesario'): "es urgente empezar tu tratamiento para manejar tu diabetes",
            ('Si', 'Tipo 1', 'No', 'No puedo contestarlo'): "es urgente empezar tu tratamiento para manejar tu diabetes",

            ('Si', 'Tipo 1', 'No', 'No tengo acceso a medicamentos'): "es urgente empezar tu tratamiento para manejar tu diabetes",

            ('Si', 'Tipo 1', 'No', 'Otro motivo'): "es urgente empezar tu tratamiento para manejar tu diabetes",

            ('Si', 'Tipo 2', 'Si2', 'Insulina'): "estas manejando adecuadamente, pero se recomienda un monitoreo constante",

            ('Si', 'Tipo 2', 'Si2', 'Medicamentos orales'): "estas manejando adecuadamente, pero se recomienda un monitoreo constante",

            ('Si', 'Tipo 2', 'Si2', 'Dieta especial'): "estas manejando adecuadamente, pero se recomienda un monitoreo constante",

            ('Si', 'Tipo 2', 'Si2', 'Ejercicio regular'): "estas manejando adecuadamente, pero se recomienda un monitoreo constante",

            ('Si', 'Tipo 2', 'Si2', 'Ninguno'): "es urgente empezar tu tratamiento para manejar tu diabetes",

            ('Si', 'Tipo 2', 'No2', 'No lo creo necesario'): "es urgente empezar tu tratamiento para manejar tu diabetes",

            ('Si', 'Tipo 2', 'No2', 'No puedo contestarlo'): "es urgente empezar tu tratamiento para manejar tu diabetes",

            ('Si', 'Tipo 2', 'No', 'No tengo acceso a medicamentos'): "es urgente empezar tu tratamiento para manejar tu diabetes",

            ('Si', 'Tipo 2', 'No2', 'Otro motivo'): "es urgente empezar tu tratamiento para manejar tu diabetes",

            ('Si', 'No estoy seguro', 'Si2', 'Insulina'): "estas manejando adecuadamente, pero se recomienda un monitoreo constante",

            ('Si', 'No estoy seguro', 'Si2', 'Medicamentos orales'): "estas manejando adecuadamente, pero se recomienda un monitoreo constante",

            ('Si', 'No estoy seguro', 'Si2', 'Dieta especial'): "estas manejando adecuadamente, pero se recomienda un monitoreo constante",

            ('Si', 'No estoy seguro', 'Si2', 'Ejercicio regular'): "estas manejando adecuadamente, pero se recomienda un monitoreo constante",

            ('Si', 'No estoy seguro', 'Si2', 'Ninguno'): "es urgente empezar tu tratamiento para manejar tu diabetes",

            ('Si', 'No estoy seguro', 'No', 'No lo creo necesario'): "es urgente empezar tu tratamiento para manejar tu diabetes",

            ('Si', 'No estoy seguro', 'No', 'No puedo contestarlo'): "es urgente empezar tu tratamiento para manejar tu diabetes",

            ('Si', 'No estoy seguro', 'No', 'No tengo acceso a medicamentos'): "es urgente empezar tu tratamiento para manejar tu diabetes",

            ('Si', 'No estoy seguro', 'No', 'Otro motivo'): "es urgente empezar tu tratamiento para manejar tu diabetes",
            
        }
        self.SaveVar = ""
        self.recomendacion = ""
        self.Respuestas = []
        self.resultados = ""
        self.calendario = ""
        self.verificar = ("",)*4
        self.cg=ft.RadioGroup(content=ft.Column(self.radios))
        self.preguntas=[
            "¿Ha sido diagnosticado recientemente?",
            "¿Que tipo tiene?",
            "¿Estas siguiendo un tratamiento Actualmente?",
            "¿Ha tenido alguno de los siguientes sintomas(seleccion multiple)?",
            "¿Que tratamiento sigue(Seleccion multiple)?",
            "¿Porque no sigue un tratamiento?",
            "¿con que frecuencia presenta los sintomas?",
            "¿Conoces tu nivel de glucosa en ayuna?",
            "¿Haz visitado al medico por esto?",
            "¿Nivel de glucosa en ayunas?",
            "¿Tiene acceso a un glucometro?",
            "Felicidades Haz completado la Encuesta"

        ]
        self.Recomendaciones = {
    "calendario1": {"Lunes" : ["Cardio 30 min","Desayuno alto en fibra","Meditación 10 min"],
                    "Martes" : ["Fuerza 45 minutos","Proteinas magras   ","Lectura relajante"],
                    "Miércoles": ["Yoga 60 min", "Grasas saludables", "Baño caliente"],
                    "Jueves": ["Cardio 30 min", "Frutas y vegetales", "Masaje"],
                    "Viernes": ["Fuerza 45 min", "Carbohidratos complejos", "Meditación 15 min"],
                    "Sábado": ["Caminata 30 min", "Proteínas y grasas saludables", "Tiempo con la familia"],
                    "Domingo": ["Descanso", "Libre", "Libre"]
    },
    
    "calendario2": {"Lunes": ["Caminata 30 min", "Proteínas magras", "Baño caliente"],
                "Martes": ["Pilates 45 min", "Grasas saludables", "Lectura relajante"],
                "Miércoles": ["Natación 60 min", "Frutas y vegetales", "Masaje"],
                "Jueves": ["Caminata 30 min", "Carbohidratos complejos", "Meditación 10 min"],
                "Viernes": ["Pilates 45 min", "Desayuno alto en fibra", "Tiempo con la familia"],
                "Sábado": ["Descanso", "Proteínas y grasas saludables", "Libre"],
                "Domingo": ["Libre", "Libre", "Libre"]
},
"calendario3": {"Lunes": ["Bicicleta 30 min", "Carbohidratos complejos", "Meditación 10 min"],
                "Martes": ["Yoga 45 min", "Proteínas magras", "Baño caliente"],
                "Miércoles": ["Natación 60 min", "Grasas saludables", "Tiempo con la familia"],
                "Jueves": ["Bicicleta 30 min", "Frutas y vegetales", "Lectura relajante"],
                "Viernes": ["Yoga 45 min", "Desayuno alto en fibra", "Meditación 15 min"],
                "Sábado": ["Caminata 30 min", "Proteínas y grasas saludables", "Masaje"],
                "Domingo": ["Descanso", "Libre", "Libre"]
},

"calendario4" : {"Lunes": ["Fuerza 30 min", "Grasas saludables", "Masaje"],
                "Martes": ["Cardio 45 min", "Desayuno alto en fibra", "Meditación 10 min"],
                "Miércoles": ["Yoga 60 min", "Frutas y vegetales", "Lectura relajante"],
                "Jueves": ["Fuerza 30 min", "Proteínas magras", "Baño caliente"],
                "Viernes": ["Cardio 45 min", "Carbohidratos complejos", "Meditación 15 min"],
                "Sábado": ["Caminata 30 min", "Proteínas y grasas saludables", "Tiempo con la familia"],
                "Domingo": ["Descanso", "Libre", "Libre"]
},

"calendario5" : {"Lunes": ["Caminata 30 min", "Proteínas magras", "Baño caliente"],
                "Martes": ["Yoga 45 min", "Grasas saludables", "Lectura relajante"],
                "Miércoles": ["Natación 60 min", "Frutas y vegetales", "Masaje"],
                "Jueves": ["Caminata 30 min", "Carbohidratos complejos", "Meditación 10 min"],
                "Viernes": ["Pilates 45 min", "Desayuno alto en fibra", "Tiempo con la familia"],
                "Sábado": ["Descanso", "Proteínas y grasas saludables", "Libre"],
                "Domingo": ["Libre", "Libre", "Libre"]
}

, "calendario6": {"Lunes": ["Cardio 30 min", "Desayuno alto en fibra", "Meditación 10 min"],
                "Martes": ["Fuerza 45 min", "Proteínas magras", "Lectura relajante"],
                "Miércoles": ["Yoga 60 min", "Grasas saludables", "Baño caliente"],
                "Jueves": ["Cardio 30 min", "Frutas y vegetales", "Masaje"],
                "Viernes": ["Fuerza 45 min", "Carbohidratos complejos", "Meditación 15 min"],
                "Sábado": ["Caminata 30 min", "Proteínas y grasas saludables", "Tiempo con la familia"],
                "Domingo": ["Descanso", "Libre", "Libre"]
}
,"calendario7": {"Lunes": ["Bicicleta 30 min", "Carbohidratos complejos", "Meditación 10 min"],
                "Martes": ["Yoga 45 min", "Proteínas magras", "Baño caliente"],
                "Miércoles": ["Natación 60 min", "Grasas saludables", "Tiempo con la familia"],
                "Jueves": ["Bicicleta 30 min", "Frutas y vegetales", "Lectura relajante"],
                "Viernes": ["Yoga 45 min", "Desayuno alto en fibra", "Meditación 15 min"],
                "Sábado": ["Caminata 30 min", "Proteínas y grasas saludables", "Masaje"],
                "Domingo": ["Descanso", "Libre", "Libre"]
}

,"calendario8" : {"Lunes": ["Caminata 30 min", "Proteínas magras", "Baño caliente"],
                "Martes": ["Pilates 45 min", "Grasas saludables", "Lectura relajante"],
                "Miércoles": ["Natación 60 min", "Frutas y vegetales", "Masaje"],
                "Jueves": ["Caminata 30 min", "Carbohidratos complejos", "Meditación 10 min"],
                "Viernes": ["Pilates 45 min", "Desayuno alto en fibra", "Tiempo con la familia"],
                "Sábado": ["Descanso", "Proteínas y grasas saludables", "Libre"],
                "Domingo": ["Libre", "Libre", "Libre"]
}

,"calendario9" : {"Lunes": ["Cardio 30 min", "Desayuno alto en fibra", "Meditación 10 min"],
                "Martes": ["Fuerza 45 min", "Proteínas magras", "Lectura relajante"],
                "Miércoles": ["Yoga 60 min", "Grasas saludables", "Baño caliente"],
                "Jueves": ["Cardio 30 min", "Frutas y vegetales", "Masaje"],
                "Viernes": ["Fuerza 45 min", "Carbohidratos complejos", "Meditación 15 min"],
                "Sábado": ["Caminata 30 min", "Proteínas y grasas saludables", "Tiempo con la familia"],
                "Domingo": ["Descanso", "Libre", "Libre"]
}

,"calendario10": {"Lunes": ["Fuerza 30 min", "Grasas saludables", "Masaje"],
                "Martes": ["Cardio 45 min", "Desayuno alto en fibra", "Meditación 10 min"],
                "Miércoles": ["Yoga 60 min", "Frutas y vegetales", "Lectura relajante"],
                "Jueves": ["Fuerza 30 min", "Proteínas magras", "Baño caliente"],
                "Viernes": ["Cardio 45 min", "Carbohidratos complejos", "Meditación 15 min"],
                "Sábado": ["Caminata 30 min", "Proteínas y grasas saludables", "Tiempo con la familia"],
                "Domingo": ["Descanso", "Libre", "Libre"]
}
}
        self.pregunta = ft.Text()
        self.button = ft.ElevatedButton(
            visible=False,
            text="volver a hacer",
            on_click=self.cargarData,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                color=ft.colors.BLUE,
            ),
        )
        self.send_button = None
   
    def cargarData(self,e: ft.ControlEvent):
        self.pregunta.value = self.preguntas[0]
        self.radios[0].visible= True
        self.radios[1].visible= True
        self.send_button.visible=True
        self.button.visible=False
        print(self.Respuestas[0:5])
        self.Respuestas.clear()
        self.page.update()
    
    def send(self,e: ft.ControlEvent):
        #vista = self.registroView.getRegisterView()
        #self.page.views.append(vista)
        #self.page.update()
        
        print(self.cg.value)
        for x in self.radios:
            x.visible= False

        if(self.cg.value == "Si"):    
            self.pregunta.value = self.preguntas[1]
            self.radios[2].visible= True
            self.radios[3].visible= True
            self.radios[4].visible= True
            
        elif(self.cg.value == "No"):
            self.pregunta.value = self.preguntas[3]
            self.radios[7].visible= True
            self.radios[8].visible= True
            self.radios[9].visible= True
            self.radios[10].visible= True
            self.radios[11].visible= True
        
        elif(self.cg.value == "Tipo 1" or self.cg.value == "Tipo 2" or self.cg.value == "No estoy seguro" ):
            self.pregunta.value = self.preguntas[2]
            self.radios[5].visible= True
            self.radios[6].visible= True
            
        elif(self.cg.value == "Fatiga" or 
             self.cg.value == "Orinar con frecuencia" or
             self.cg.value == "Sed excesiva" or
             self.cg.value == "Vision borrosa" ):
            
            self.pregunta.value = self.preguntas[6]
            self.radios[20].visible= True
            self.radios[21].visible= True
            self.radios[22].visible= True

        elif(self.cg.value == "No he tenido ninguno"):
            self.pregunta.value = self.preguntas[7]
            self.radios[23].visible= True
            self.radios[24].visible= True
        elif(self.cg.value == "Si2"):
            self.pregunta.value = self.preguntas[4]
            self.radios[12].visible= True
            self.radios[13].visible= True
            self.radios[14].visible= True
            self.radios[15].visible= True

        elif(self.cg.value == "No2"):
            self.pregunta.value = self.preguntas[5]
            self.radios[16].visible= True
            self.radios[17].visible= True
            self.radios[18].visible= True
            self.radios[19].visible= True

        elif(self.cg.value == "Insulina" or
             self.cg.value == "Medicamentos orales" or
             self.cg.value == "Ejercicio regular" or
             self.cg.value == "Dieta especial" ):
            self.pregunta.value = self.preguntas[7]
            self.radios[24].visible= True
            self.radios[23].visible= True

        elif(self.cg.value == "Si3"):
            self.pregunta.value = self.preguntas[9]
            
            self.radios[27].visible= True
            self.radios[28].visible= True
            self.radios[29].visible= True

        elif(self.cg.value == "No3"):
            self.pregunta.value = self.preguntas[10]
            self.radios[30].visible= True
            self.radios[31].visible= True
        elif(self.cg.value == "Diario"):
            self.pregunta.value = self.preguntas[8]
            self.radios[25].visible= True
            self.radios[26].visible= True
        elif(self.cg.value == "No lo creo necesario" or
            self.cg.value == "No puedo contestarlo" or
            self.cg.value == "No tengo acceso a medicamentos" or
            self.cg.value == "Otro motivo" ):
                self.send_button.visible=False
                self.button.visible=True
                self.pregunta.value = "Click en el boton"
                self.calendario = self.Recomendaciones.get('calendario3')
                self.resultados = ""  # Inicializar la variable
                for dia, actividades_dia in self.calendario.items():
                    actividades_str = ', '.join(actividades_dia)
                    self.resultados += f"{dia}: {actividades_str}\n"  # Agregar el resultado al string
                    self.SaveVar = self.resultados
                self.calendarioupdated = "calendario10"
                self.conexion.updatedCalendar(self.id, self.calendarioupdated)
                self.pregunta.value = f"Es urgente empezar tu tratamiento para manejar tu diabetes\nCalendario recomendado:\n{self.SaveVar}"
                self.recomendacion=""
                self.SaveVar=""
                self.calendario=""
                self.calendarioupdated=""
                 # Comentado: self.pregunta.value = "Click en el botón"
        # self.radios[32].visible = True
                


        else:
            
            self.send_button.visible=False
            self.button.visible=True
            for x in self.Respuestas[0:4]:
                if(x=='Si2' or x=='Si3' or x=='Si4' or x=='Si5'):
                    self.Respuestas[self.Respuestas.index(x)] = 'Si'
                if(x=='No2' or x=='No3' or x=='No4' or x=='No5'):
                    self.Respuestas[self.Respuestas.index(x)] = 'No'
            
            try:
                if self.recomendacion=="" or self.SaveVar=="":
                    self.calendario = self.Recomendaciones.get('calendario10')
                    for dia, actividades_dia in self.calendario.items():
                        actividades_str = ', '.join(actividades_dia)
                        self.resultados += f"{dia}: {actividades_str}\n"  # Agregar el resultado al string
                        self.SaveVar = self.resultados
                    self.calendarioupdated = "calendario10"
                    self.conexion.updatedCalendar(self.id, self.calendarioupdated)
                    self.pregunta.value = f"Es recomendable un chequeo y consulta medica para determinar el estado de tu salud\nCalendario recomendado:\n{self.SaveVar}"
                    self.recomendacion=""
                    self.SaveVar=""
                    self.calendario=""
                    self.calendarioupdated=""
                    
                else:
                    self.pregunta.value = f"{self.recomendacion}\nCalendario recomendado:\n{self.SaveVar}"
                    self.conexion.updatedCalendar(self.id, self.calendarioupdated)
                    self.recomendacion=""
                    self.SaveVar=""
                    self.calendario=""
                
                #self.pregunta.value = self.SaveVar
            except:
                self.pregunta.value = "Es recomendable un chequeo y consulta medica para determinar el estado de tu salud"
        
        self.listedanswers = list(self.combinaciones.keys())
        self.Respuestas.append(self.cg.value)
        try:
            if len(self.Respuestas) == 4:
                self.resultados = ""
                self.SaveVar = ""
                self.recomendacion = ""
                print("Llegaste aqui")
                self.verificar = tuple(self.Respuestas)
                print("se convirtio?",self.verificar)
                if self.verificar == self.listedanswers[0] or self.verificar == self.listedanswers[1] :
                    self.calendario = (self.Recomendaciones.get('calendario1'))
                    self.calendarioupdated = "calendario1"
                elif self.verificar == self.listedanswers[2] or self.verificar == self.listedanswers[3] :
                    self.calendario = (self.Recomendaciones.get('calendario2'))
                    self.calendarioupdated = "calendario2"
                elif self.verificar == self.listedanswers[4] or self.verificar == self.listedanswers[5] :
                    self.calendario = (self.Recomendaciones.get('calendario3'))
                    self.calendarioupdated = "calendario3"
                elif self.verificar == self.listedanswers[6] or self.verificar == self.listedanswers[7] :
                    self.calendario = (self.Recomendaciones.get('calendario4'))
                    self.calendarioupdated = "calendario4"
                elif self.verificar == self.listedanswers[8] or self.verificar == self.listedanswers[9] :
                    self.calendario = (self.Recomendaciones.get('calendario5'))
                    self.calendarioupdated = "calendario5"
                elif self.verificar == self.listedanswers[10] or self.verificar == self.listedanswers[11] :
                    self.calendario = (self.Recomendaciones.get('calendario6'))
                    self.calendarioupdated = "calendario6"
                elif self.verificar == self.listedanswers[12] or self.verificar == self.listedanswers[13] :
                    self.calendario = (self.Recomendaciones.get('calendario7'))
                    self.calendarioupdated = "calendario7"
                elif self.verificar == self.listedanswers[14] or self.verificar == self.listedanswers[15] :
                    self.calendario = (self.Recomendaciones.get('calendario8'))
                    self.calendarioupdated = "calendario8"
                elif self.verificar == self.listedanswers[16] or self.verificar == self.listedanswers[17] :
                    self.calendario = (self.Recomendaciones.get('calendario9'))
                    self.calendarioupdated = "calendario9"
                elif self.verificar == self.listedanswers[18] or self.verificar == self.listedanswers[19] :
                    self.calendario = self.Recomendaciones.get('calendario10')
                    self.calendarioupdated = "calendario10"
                
                if self.verificar == tuple(self.Respuestas):
                    for dia, actividades_dia in self.calendario.items():
                        actividades_str = ', '.join(actividades_dia)
                        self.resultados += f"{dia}: {actividades_str}\n"  # Agregar el resultado al string
                        self.SaveVar = self.resultados
                
                if self.verificar in self.combinaciones:
                    self.recomendacion = self.combinaciones[self.verificar]
        except:
            pass
        print(self.Respuestas)
        print(self.calendario)        
        print("Variable final", self.SaveVar)       
        self.page.update()
   
            

    def getCuestion(self):
        self.pregunta.value = self.preguntas[0]
        pregunta1=ft.Column(controls=[
            self.pregunta,
            self.cg,
        ])
        
        self.send_button = ft.ElevatedButton(
            text="Enviar",
            on_click=self.send,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                color=ft.colors.BLUE,
            ),
        )

        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                 
                self.title,
                ft.Container(padding=10),
                pregunta1,
                
                ft.Container(padding=20),
                self.send_button,
                self.button,
              
              
            ],
            width=300,
            expand=1
            
                
        )

 

    