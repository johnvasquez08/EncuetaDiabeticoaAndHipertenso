import flet as ft

class EncuestaHipertenso():


    def __init__(self,page: ft.Page,navbar):
        self.page = page
        self.navBar = navbar


    def send(self,e):
        #vista = self.registroView.getRegisterView()
        #self.page.views.append(vista)
        #self.page.update()
        print("dates")
    def getEncuestaHipertensoView(self):
        
        title = ft.Text(
            value="Encuesta Hipertenso",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
            
        )

        prgunta1 = ft.TextField(
            label="pregunta1",
            helper_text="¿con que frecuencia va a playa?",
            border_radius=ft.BorderRadius(5, 5, 5, 5),
        )
        prgunta2 = ft.TextField(
            label="pregunta2",
            helper_text="¿con que frecuencia juega futbol?",
            border_radius=ft.BorderRadius(5, 5, 5, 5),
        )
        send_button = ft.ElevatedButton(
            text="Enviar",
            on_click=self.send,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                color=ft.colors.BLUE,
            ),
        )


        # Contenedor principal centrado
        contente = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                 
                title,
                ft.Container(padding=10),
                prgunta1,
                ft.Container(padding=10),
                prgunta2,
                ft.Container(padding=20),
                send_button,
              
              
            ],
            width=300,
        
            expand=1,
        
            
                
        )
        login = ft.Row(controls=[
            ft.Container(content=contente,
            padding=40,
            bgcolor='#5ce5ff',
            border_radius=80,
            
            
            width=300,
            alignment=ft.alignment.center
        )
        ])

        
        background = ft.Container(
            width=self.page.width,
            height=(1.4*self.page.height),
            bgcolor='#9ff2ff',
            alignment=ft.alignment.center,
            padding=0,
            margin=0
        )

        contenido = ft.Row(controls=[login,
        ],   
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            
        )

        # Contenedor resaltado en el centro
        return ft.View(
            route="/EncuestaDiabetico",
            controls=[
                ft.Stack(
                    [
                    background,
                    contenido,
                   
                   ]
                    ,width=self.page.width,
                    alignment=ft.alignment.center,
                    
                    )
                    ],
                    
                    padding=0,
                    scroll=ft.ScrollMode.AUTO,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    navigation_bar= self.navBar,
                    
        )
    
   
        
        title = ft.Text(
            value="Encuesta Diabeticos",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
        )

        prgunta1 = ft.TextField(
            label="pregunta1",
            helper_text="¿con que frecuencia consume azucares?",
            border_radius=ft.BorderRadius(5, 5, 5, 5),
        )
        prgunta2 = ft.TextField(
            label="pregunta2",
            helper_text="¿con que frecuencia hace ejercicio?",
            border_radius=ft.BorderRadius(5, 5, 5, 5),
        )
        send_button = ft.ElevatedButton(
            text="Enviar",
            on_click=self.send,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                color=ft.colors.BLUE,
            ),
        )


        # Contenedor principal centrado
        contente = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                 
                title,
                ft.Container(padding=10),
                prgunta1,
                ft.Container(padding=10),
                prgunta2,
                ft.Container(padding=20),
                send_button,
              
              
            ],
            width=300,
            
            
                
        )
        login = ft.Row(controls=[
            ft.Container(content=contente,
            padding=20,
            bgcolor='#5ce5ff',
            border_radius=80,
            
            
            width=300,
            
        )
        ])

        
        background = ft.Container(
            width=self.page.width,
            height=self.page.height,
            bgcolor='#9ff2ff',
            alignment=ft.alignment.center,
            padding=0,
            margin=0
        )

        contenido = ft.Row(controls=[ft.Container(expand=1),login,ft.Container(expand=1),
        ],  

            
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            
        )

        # Contenedor resaltado en el centro
        return ft.View(
            route="/EncuestaHipertenso",
            controls=[
                ft.Stack(
                    [
                    background,
                    contenido,
                    
                   ]
                    ,width=self.page.width,
                  
                    
                    )
                    ],
                    
                    padding=0,
                    scroll=ft.ScrollMode.AUTO,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    navigation_bar=self.navBar,
                    
        )