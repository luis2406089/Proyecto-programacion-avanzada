import reflex as rx
from proyectoll.pages.componentes.navbar import navbar #importamos el componente navbar de la carpeta componentes

class state(rx.State): #la clase state se usa para manejar el estado de la aplicación
    pass


def entrada_de_usuarios(title: str, is_password: bool = False) -> rx.Component: #entrada_de_usuarios es una función que devuelve un componente de entrada de usuario
    return rx.vstack(
        rx.text(title, color="gray", font_size="11px", weight="bold",width="100%"), #rx.text es para mostrar texto, se puede usar para mostrar el título de la entrada de usuario
        rx.input(background_color="black", color="white",type="text" if not is_password else "password",width="100%"), #rx.input es para crear un campo de entrada de usuario, se puede usar para crear un campo de entrada de texto o contraseña),
        width="100%", #width es el ancho del elemento
        )

def crear_evento_de_entrada():
    return rx.badge(rx.text("Login",
                            text_align="center",
                            width="100%"), #text_align es para alinear el texto dentro del badge), 
                    color_scheme="teal", 
                    variant="outline",
                    size="2",
                    width="100%",
                    padding="1em 0em") #rx.badge es para mostrar una etiqueta, se puede usar para mostrar el estado de la entrada de usuario
    

def componente_principal():
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="lock",size=28,color="rgba(127,127,127,1)"),
            width="100%", #width es el ancho del elemento
            height="55px", #height es la altura del elemento
            bg="#181818", #bg es el color de fondo del elemento
            border_radius="10px 10px 0px 0px", #border_radius es el radio del borde del elemento, se usa para redondear los bordes
            display="flex", #display es el tipo de visualización del elemento, se usa para definir cómo se muestra el elemento
            justify_content="center", #justify_content es para alinear los elementos horizontalmente
            align_items="center", #align_items es para alinear los elementos verticalmente

            ), #hstack es para apilar los elementos horizontalmente
        rx.vstack(
            entrada_de_usuarios("Email"), #entrada_de_usuarios es una función que devuelve un componente de entrada de usuario
            entrada_de_usuarios(title="Password", is_password=True),#entrada_de_usuarios es una función que devuelve un componente de entrada de usuario
            rx.spacer(),
            crear_evento_de_entrada(), #crear_evento_de_entrada es una función que devuelve un componente de etiqueta
            width="100%", #width es el ancho del elemento
            padding="2em 2em 4em 2em", #padding es el espacio interno del elemento, se usa para separar el contenido del borde
            spacing="6",
        ),
        width=["100%", "100%","65%","50%","35%"], #width es el ancho del elemento, se puede usar una lista para definir el ancho en diferentes pantallas
        bg="rgba(21,21,21,0.55)", #bg es el color de fondo del elemento, se puede usar rgba para definir el color con transparencia
        border="0.75px solid #2e2e2e", #border es el borde del elemento, se puede usar rgba para definir el color con transparencia
        border_radius="10px", #border_radius es el radio del borde del elemento, se usa para redondear los bordes
        box_shadow="0px 8px 16px 6px rgba(0, 0, 0, 0.25)", #box_shadow es la sombra del elemento, se usa para darle profundidad al elemento
        ) #vstack es para apilar los elementos verticalmente

def login()->rx.Component: #rx.component es un componente de reflex, el componente se usa para crear la interfaz de usuario
    return rx.box( #src es la ruta de la imagen de fondo)
        navbar(),  # <-- Usas el mismo navbar en ambas páginas
        rx.center(#rx.center es para centrar los elementos en la pantalla
        componente_principal(),             
        width="100%", #width es el ancho de la pantalla
        height="100vh", #height es la altura de la pantalla
        bg="#121212", #bg es el color de fondo de la pantalla
        padding_top="6em"
    )
)
        