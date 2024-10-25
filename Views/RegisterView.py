import flet as ft
from DAO.Entidad.Persona import Persona

class RegisterView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.nombre = None
        self.apellido = None
        self.username = None
        self.password = None
        self.condicion = None

    def registro(self, e):
        nuevo = Persona(self.nombre.value,
                        self.apellido.value,
                        self.username.value,
                        self.password.value,
                        self.condicion.value)
        nuevo.save()
        self.page.views.pop()
        self.page.update()
        # print((self.nombre.value, self.apellido.value, self.username.value, self.password.value, self.condicion.value))

    def getRegisterView(self):
        title = ft.Text(
            value="Registrate",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
        )

        self.nombre = ft.TextField(
            label="Nombre",
            helper_text="Ingrese su nombre",
            border_radius=ft.BorderRadius(5, 5, 5, 5),
        )

        self.apellido = ft.TextField(
            label="Apellido",
            helper_text="Ingrese su apellido",
            border_radius=ft.BorderRadius(5, 5, 5, 5),
        )
        self.username = ft.TextField(
            label="Usuario",
            helper_text="Ingrese su nombre de usuario",
            border_radius=ft.BorderRadius(5, 5, 5, 5),
        )
      
        self.password = ft.TextField(
            label="Contraseña",
            helper_text="Ingrese su contraseña",
            password=True,
            can_reveal_password=True,
            border_radius=ft.BorderRadius(5, 5, 5, 5),
        )
        self.condicion = ft.RadioGroup(content=ft.Row([
            ft.Radio(value="Diabetico", label="Diabetico"),
            ft.Radio(value="Hipertenso", label="Hipertenso"),
            ft.Radio(value="Ambas", label="Ambas")
        ]))

        registro_button = ft.ElevatedButton(
            text="Registrase",
            on_click=self.registro,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                color=ft.colors.BLUE,
            ),
        )

        contente = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                title,
                ft.Container(padding=10),
                ft.Row(controls=[
                    self.nombre,
                    ft.Container(padding=10),
                    self.apellido,
                    ft.Container(padding=10),
                ]),
                ft.Row(controls=[
                    self.username,
                    ft.Container(padding=10),
                    self.password,
                    ft.Container(padding=10),
                ]),  
                self.condicion,
                ft.Container(padding=20),
                registro_button,
            ],
            expand=1
        )

        login = ft.Row(controls=[
            ft.Container(
                content=contente,
                padding=20,
                bgcolor='#5ce5ff',
                border_radius=80,
                margin=ft.margin.only(top=100),
                alignment=ft.alignment.center
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

        contenido = ft.Row(controls=[
            ft.Container(expand=1),
            login,
            ft.Container(expand=1),
        ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        return ft.View(
            route="/Register",
            controls=[
                ft.Stack(
                    [
                        background,
                        contenido,
                    ],
                    width=self.page.width,
                    alignment=ft.alignment.center,
                )
            ],
            padding=0,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
