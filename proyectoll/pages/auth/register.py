import reflex as rx
import hashlib
from typing import Optional
from sqlmodel import Field, SQLModel, select
from proyectoll.pages.componentes.navbar import navbar  # Importamos el componente navbar

# Modelo de Usuario
class Usuario(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    apellido: str
    email: str = Field(unique=True)
    password: str

class RegisterState(rx.State):
    """Estado para manejar el registro de usuarios"""
    nombre: str = ""
    apellido: str = ""
    email: str = ""
    password: str = ""
    confirm_password: str = ""
    error_message: str = ""
    success: bool = False

    def registrar_usuario(self):
        """Registra un nuevo usuario en la base de datos"""
        # Validaciones básicas
        if not all([self.nombre, self.apellido, self.email, self.password, self.confirm_password]):
            self.error_message = "Todos los campos son obligatorios"
            return
            
        if self.password != self.confirm_password:
            self.error_message = "Las contraseñas no coinciden"
            return
            
        if len(self.password) < 8:
            self.error_message = "La contraseña debe tener al menos 8 caracteres"
            return

        try:
            # Hashear la contraseña
            hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
            
            # Crear nuevo usuario
            nuevo_usuario = Usuario(
                nombre=self.nombre,
                apellido=self.apellido,
                email=self.email,
                password=hashed_password
            )
            
            # Guardar en la base de datos
            with rx.session() as session:
                # Verificar si el email ya existe
                existing_user = session.exec(select(Usuario).where(Usuario.email == self.email)).first()
                if existing_user:
                    self.error_message = "Este email ya está registrado"
                    return
                
                session.add(nuevo_usuario)
                session.commit()
                self.success = True
                self.error_message = ""
                self.reset_fields()
                
                # Redirigir inmediatamente (sin delay)
                return rx.redirect("/login")
                
        except Exception as e:
            self.error_message = f"Error al registrar: {str(e)}"
            print(f"Error completo: {e}")

    def reset_fields(self):
        """Reinicia los campos del formulario"""
        self.nombre = ""
        self.apellido = ""
        self.email = ""
        self.password = ""
        self.confirm_password = ""

def entrada_de_usuarios(title: str, field: str, is_password: bool = False) -> rx.Component:
    """Componente reutilizable para campos de entrada vinculados al estado"""
    return rx.vstack(
        rx.text(
            title, 
            color="gray", 
            font_size="11px", 
            weight="bold",
            width="100%"
        ),
        rx.input(
            background_color="black", 
            color="white",
            type="password" if is_password else "text",
            width="100%",
            border="1px solid #444",
            border_radius="6px",
            padding="10px",
            on_change=getattr(RegisterState, f"set_{field}"),
            value=getattr(RegisterState, field)
        ),
        width="100%",
        spacing="1"
    )

def crear_boton_registro():
    """Botón de registro con acción"""
    return rx.button(
        "Registrarse",
        color_scheme="teal",
        variant="outline",
        size="3",
        width="100%",
        padding="1em 0em",
        cursor="pointer",
        on_click=RegisterState.registrar_usuario
    )

def mensajes_estado():
    """Muestra mensajes de error o éxito"""
    return rx.box(
        rx.cond(
            RegisterState.error_message,
            rx.text(
                RegisterState.error_message,
                color="red.500",
                text_align="center"
            ),
        ),
        rx.cond(
            RegisterState.success,
            rx.text(
                "¡Registro exitoso! Redirigiendo...",
                color="green.500",
                text_align="center"
            ),
        )
    )

def componente_principal() -> rx.Component:
    """Contenedor principal del formulario de registro"""
    return rx.vstack(
        # Encabezado con icono
        rx.hstack(
            rx.icon(tag="user", size=28, color="rgba(127,127,127,1)"),
            width="100%",
            height="55px",
            bg="#181818",
            border_radius="10px 10px 0px 0px",
            display="flex",
            justify_content="center",
            align_items="center",
        ),
        
        # Formulario de registro
        rx.vstack(
            rx.hstack(
                entrada_de_usuarios("Nombre", "nombre"),
                entrada_de_usuarios("Apellido", "apellido"),
                width="100%",
                spacing="4"
            ),
            entrada_de_usuarios("Email", "email"),
            entrada_de_usuarios("Contraseña", "password", is_password=True),
            entrada_de_usuarios("Confirmar Contraseña", "confirm_password", is_password=True),
            mensajes_estado(),
            rx.spacer(),
            crear_boton_registro(),
            rx.text(
                "¿Ya tienes cuenta? ",
                rx.link("Inicia sesión", href="/login", color="teal.400"),
                color="gray",
                font_size="sm"
            ),
            width="100%",
            padding="2em 2em 4em 2em",
            spacing="6",
            align_items="stretch"
        ),
        
        # Estilos del contenedor
        width=["100%", "100%", "65%", "50%", "35%"],
        max_width="400px",
        bg="rgba(21,21,21,0.55)",
        border="0.75px solid #2e2e2e",
        border_radius="10px",
        box_shadow="0px 8px 16px 6px rgba(0, 0, 0, 0.25)",
    )

def register() -> rx.Component:
    """Página de registro completa"""
    return rx.center(
        navbar(),
        componente_principal(),
        width="100%",
        height="100vh",
        bg="linear-gradient(135deg, #121212 0%, #1a1a1a 100%)",
        padding="2em"
    )