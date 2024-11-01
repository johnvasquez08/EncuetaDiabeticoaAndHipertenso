import flet as ft
from Views.InicioView import InicioView


async def main(page: ft.Page):
    page.window.width = 680        # window's width is 200 px
    page.window.height = 710       # window's height is 200 px
    page.window.resizable = False  # window is not resizable
   
    
    page.bgcolor = ft.colors.BLUE_200
    page.padding=0
    page.title = "cuestionario"
    page.scroll = ft.ScrollMode.AUTO
   
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    ventanda = InicioView(page)
    page.views.append(ventanda.getInicioView())
    await page.update_async()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)