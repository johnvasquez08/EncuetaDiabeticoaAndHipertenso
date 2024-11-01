import flet as ft
from DAO.Factory.ConexionManager import ConexionManager
from Views.Diabetico.Cuestions import Cuestions

class ViewCalendario:
    def __init__(self, page: ft.Page, navbar):
        self.cuestions = Cuestions(page, id)
        self.id = id
        self.page = page
        self.navbar = navbar
        self.conexionManager = ConexionManager()
        
        # Botón para ver el calendario
        self.dropdown_personas = ft.ElevatedButton(
            text="Ver Calendario",
            on_click=self.show_calendario,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                color=ft.colors.BLUE,
            ),
            height=50,
        )
        
        # Tabla de calendario con estilo mejorado
        self.selected_calendar_table = ft.DataTable(
            columns=[
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("Día", size=16, weight=ft.FontWeight.BOLD, color="black"),
                        padding=ft.padding.all(10)
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        content=ft.Text("Actividades", size=16, weight=ft.FontWeight.BOLD, color="black"),
                        padding=ft.padding.all(10)
                    )
                )
            ],
            rows=[],
            heading_row_height=70,
            data_row_max_height=100,
            column_spacing=40,
        )

    def show_calendario(self, e):
        cal = ConexionManager.getCalendario(self.id)
        if cal in self.cuestions.Recomendaciones:
            calendario_seleccionado = self.cuestions.Recomendaciones[cal]
            rows = []
            for dia, actividades in calendario_seleccionado.items():
                actividad_texto = "\n".join(actividades)
                rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Container(
                                    content=ft.Text(dia, size=14, color="black"),
                                    padding=ft.padding.all(15),
                                    width=150,
                                )
                            ),
                            ft.DataCell(
                                ft.Container(
                                    content=ft.Text(
                                        actividad_texto,
                                        size=14,
                                        text_align=ft.TextAlign.LEFT,
                                        color="black"
                                    ),
                                    padding=ft.padding.all(15)
                                )
                            )
                        ]
                    )
                )
            self.selected_calendar_table.rows = rows
        else:
            self.selected_calendar_table.rows = [
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Container(
                                content=ft.Text("No hay calendario disponible", color="black"),
                                padding=ft.padding.all(15)
                            )
                        ),
                        ft.DataCell(ft.Text(""))
                    ]
                )
            ]
        self.page.update()

    def get_view_calendario(self, id):
        self.id = id
        
        # Contenido de la tabla y botón
        contenido = ft.Column(
            controls=[
                ft.Container(
                    content=self.dropdown_personas,
                    margin=ft.margin.only(bottom=20)
                ),
                ft.Container(
                    content=self.selected_calendar_table,
                    padding=ft.padding.all(20),
                    border_radius=10,
                    bgcolor=ft.colors.WHITE,
                    border=ft.border.all(2, ft.colors.BLUE_200)
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )

        # Contenedor expandible que contendrá todo
        main_container = ft.Container(
            content=ft.Column(
                controls=[
                    contenido
                ],
                expand=True,
            ),
            bgcolor="#9ff2ff",
            padding=ft.padding.all(20),
            expand=False,
        )

        return ft.View(
            route="/Calendario",
            controls=[main_container],
            scroll=ft.ScrollMode.AUTO,
            padding=0,
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            navigation_bar=self.navbar,
            bgcolor="#9ff2ff",  # Color de fondo de respaldo
        )