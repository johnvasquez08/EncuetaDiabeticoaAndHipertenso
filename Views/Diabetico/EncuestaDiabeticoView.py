import flet as ft
from Views.Diabetico.Cuestions import Cuestions
class EncuestaDiabetico():


    def __init__(self,page: ft.Page,navbar):
        self.page = page
        self.id = None
        self.navBar = navbar

    def getEncuestaDiabeticoView(self, id):
        self.id = id
        self.cuestions = Cuestions(self.page, self.id)
        login = ft.Column(controls=[
            ft.Container(content=self.cuestions.getCuestion(),
            padding=20,
            bgcolor='#5ce5ff',
            border_radius=80,
            margin=ft.margin.only(top=30),
            
            width=300,
            alignment=ft.alignment.center
        )
        ])

        
        background = ft.Container(
            width=self.page.width,
            height=(1*self.page.height),
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
                    alignment=ft.alignment.center,
                    
                    )
                    ],
                    
                    padding=0,
                    scroll=ft.ScrollMode.AUTO,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    navigation_bar=self.navBar,
                    
        )
