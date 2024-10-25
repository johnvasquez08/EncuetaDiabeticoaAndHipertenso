import flet as ft
from DAO.Factory.ConexionManager import ConexionManager
class ViewVisualizar():
    def __init__(self,page:ft.Page,navbar):
        self.page = page
        self.navbar = navbar
        self.conexionManager = ConexionManager()
        self.tablaPersonas = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("id"),),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Apellido")),
            ft.DataColumn(ft.Text("username"),),
            ft.DataColumn(ft.Text("Condicion"),),
        ],
        rows=[],
        )
    
    
    def getViewVisualizar(self):
        datos = self.conexionManager.getPersonas()
        if(len(datos) > 0):
                self.tablaPersonas.rows.clear()
                for x in datos:
                    addRow = ft.DataRow(
                    cells=[
                            ft.DataCell(ft.Text(str(x[0]))),
                            ft.DataCell(ft.Text(str(x[1]))),
                            ft.DataCell(ft.Text(str(x[2]))),
                            ft.DataCell(ft.Text(str(x[3]))),
                            ft.DataCell(ft.Text(str(x[5]))),
                            
                            
                        ],) 
                    self.tablaPersonas.rows.append(addRow)
                self.page.update()     
       
        
        
        contenido = ft.Column(controls=[
           
            self.tablaPersonas,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ) 
       
        background = ft.Container(
            width=self.page.width,
            height=self.page.height*100,
            bgcolor='#9ff2ff',
            alignment=ft.alignment.center,
            padding=0,
            margin=0
        )
        
             
        contenedor = ft.Container(content=contenido,alignment=ft.alignment.center)
        return ft.View(
            route="/Visualizar",
            controls=[
                ft.Stack(
                    [
                    background,
                    contenedor,
                    ]
                    ,width=self.page.width,
                    alignment=ft.alignment.top_center,
                    
                    )
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    padding=0,
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    navigation_bar= self.navbar,
                    
        )
