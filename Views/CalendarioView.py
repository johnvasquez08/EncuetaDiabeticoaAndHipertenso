import flet as ft
from DAO.Factory.ConexionManager import ConexionManager

class ViewCalendario:
    def __init__(self, page: ft.Page, navbar):
        self.page = page
        self.id = None
        self.navbar = navbar
        self.conexionManager = ConexionManager()

        # Lista de personas para mostrar en el selector
        self.personas = self.conexionManager.getPersonas()
        self.selected_calendar = ft.Text("Seleccione una persona para ver el calendario")
        self.dropdown_personas = ft.Dropdown(
            options=[ft.dropdown.Option(text=str(persona[1]), key=str(persona[0])) for persona in self.personas],
            label="Seleccione una persona",
            on_change=self.show_calendario
        )

    def show_calendario(self, e):
        
        # Obtener la persona seleccionada del dropdown
        persona_id = self.dropdown_personas.value
        persona_data = next((p for p in self.personas if str(p[0]) == persona_id), None)
        coso=ConexionManager.getCalendario(self, self.id)
        print(coso)

        # Verificar si existe el dato de calendario y mostrarlo
        if persona_data:
            calendario = persona_data[6]  # Supongo que el índice 6 es el calendario
            self.selected_calendar.value = f"Calendario: {calendario}"
            print(coso)

        else:
            self.selected_calendar.value = "Calendario no disponible"
            print(coso)

        
        self.page.update()

    def get_view_calendario(self):
        # Contenedor principal para el selector y el calendario
        contenido = ft.Column(
            controls=[
                self.dropdown_personas,
                self.selected_calendar
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        # Fondo de la ventana
        background = ft.Container(
            width=self.page.width,
            height=self.page.height,
            bgcolor="#9ff2ff",
            alignment=ft.alignment.center
        )

        # Contenedor principal
        contenedor = ft.Container(content=contenido, alignment=ft.alignment.center)

        # Retorno de la vista completa
        return ft.View(
            route="/Calendario",
            controls=[
                ft.Stack(
                    [
                        background,
                        contenedor,
                    ],
                    width=self.page.width,
                    alignment=ft.alignment.top_center,
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            padding=0,
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            navigation_bar=self.navbar,
        )
