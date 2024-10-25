import flet as ft
from Views.RegisterView import RegisterView
from Views.Diabetico.EncuestaDiabeticoView import EncuestaDiabetico
from Views.Hipertenso.EncuestaHipertensoView import EncuestaHipertenso
from DAO.Factory.ConexionManager import ConexionManager
from Views.VisualizarView import ViewVisualizar
class InicioView():
    def __init__(self,page: ft.Page,):
        self.page = page
        self.navBar= self.getNavigation_bar()
        self.username = ft.TextField(
            value="lulumz",
            label="Usuario",
            helper_text="Ingrese su nombre de usuario",
            border_radius=ft.BorderRadius(5, 5, 5, 5),
        )

        # Campo de contraseña
        self.password = ft.TextField(
            value="Dinorey",
            label="Contraseña",
            helper_text="Ingrese su contraseña",
            password=True,
            can_reveal_password=True,
            border_radius=ft.BorderRadius(5, 5, 5, 5),
        )

        self.registroView = RegisterView(page)
        self.encuestaDiabetico = EncuestaDiabetico(page,self.navBar).getEncuestaDiabeticoView()
        self.encuestaHipertenso = EncuestaHipertenso(page,self.navBar).getEncuestaHipertensoView()
        self.visualizar = ViewVisualizar(page,self.navBar)
        self.data = None

    
    
    def navigate(self,destination: ft.ControlEvent):
  
        if destination.data == "0" and (self.data == 'Diabetico'):
            self.page.views.pop()
            self.page.views.append(self.encuestaDiabetico)
        elif destination.data == "0" and (self.data == 'Hipertenso'):
            self.page.views.pop()
            self.page.views.append(self.encuestaHipertenso)
        if destination.data == "1":
            self.page.views.pop()
            self.page.views.append(self.visualizar.getViewVisualizar())
        self.page.update()
    def getNavigation_bar(self):
        return ft.NavigationBar(
        selected_index=0, bgcolor='#5ce5ff',
        destinations=[
            ft.NavigationDestination(icon=ft.icons.QUESTION_ANSWER_OUTLINED, label="Encuesta",data="0"),
            ft.NavigationDestination(icon=ft.icons.BACKUP_TABLE_ROUNDED, label="Datos", data="1"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                label="Inicio",
                data="2"
            ),
        ],
        on_change=self.navigate
    )
    def registrarse(self,e):
        vista = self.registroView.getRegisterView()
        self.page.views.append(vista)
        self.page.update()
    def iniciarSesion(self,e):
        condi,data = ConexionManager().verificarUsuario(self.username.value,self.password.value)
        self.data=data[0][-1]
        if(condi):
            print(data)
            self.page.views.pop()
            if(self.data == 'Hipertenso'):
                self.page.views.append(self.encuestaHipertenso)
            
            elif(self.data == 'Diabetico'):
                self.page.views.append(self.encuestaDiabetico)
            
            else:
                pass
            
            self.page.update()
        else:
            print("usted no se encuetra registrado")


    def getInicioView(self):
        title = ft.Text(
            value="Iniciar Sesión",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
        )

        # Campo de usuario
        

        # Botón de iniciar sesión
        login_button = ft.ElevatedButton(
            text="Iniciar Sesión",
            on_click=self.iniciarSesion,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                color=ft.colors.BLUE,
            ),
        )

        register_button = ft.ElevatedButton(
            text="Registrarte",
            on_click=self.registrarse,
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
                self.username,
                ft.Container(padding=10),
                self.password,
                ft.Container(padding=20),
                login_button,
                ft.Container(padding=5),
                register_button,
            ],
            width=300,
            expand=1
            
                
        )
        login = ft.Row(controls=[
            ft.Container(content=contente,
            padding=20,
            bgcolor='#5ce5ff',
            border_radius=80,
            margin=ft.margin.only(top=100),
            
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
            route="/Login",
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
                    
        )
            