import reflex as rx
from proyectoll.pages.componentes.navbar import navbar

class HomeState(rx.State):
    """State for home page interactions"""
    pass

def home() -> rx.Component:
    """Landing page with full background image and call-to-action"""
    return rx.box(
        # Background image (replace with your image path)
        rx.image(
            src="/background.png",  # Place your image in assets/ folder
            width="100vw",
            height="100vh",
            object_fit="cover",
            position="fixed",
            top="0",
            left="0",
            z_index="-1"
        ),
        
        # Content overlay
        rx.vstack(
            navbar(),  # Reusing your navbar component
            
            # Main content area
            rx.hstack(
                # Left side content (text + button)
                rx.vstack(
                    rx.heading(
                        "Proyecto Programación Avanzada Luis Lopez  - 2025", 
                        size="3",
                        color="white",
                        font_weight="bold",
                        margin_bottom="1rem"
                    ),
                    rx.text(
                        "Simulador de: “PopcornHour”: portal web para recomendar, calificar y discutir sobre películas y series. Existirán dos tipos de usuarios: moderador y estándar. Los usuarios de tipo “moderador” contarán con la posibilidad para subir películas que los usuarios de tipo estándar puedan calificar, comentar y discutir sobre ellas. Los usuarios de tipo estándar podrán calificar, comentar y discutir sobre las películas que los moderadores suban al portal web.", 
                        color="rgba(255,255,255,0.9)",
                        font_size="lg"
                    ),
                    rx.button(
                        "Get Started",
                        color_scheme="teal",
                        size="3",  # Cambiado de "lg" a "3" (valores aceptados: "1", "2", "3", "4")
                        padding="1.5em 2em",
                        margin_top="2rem",
                        on_click=rx.redirect("/register")
                    ),
                    align_items="flex-start",
                    spacing="4",
                    padding_x="2em",
                    max_width="50%"
                ),
                
                # Right side (can add more content here)
                rx.spacer(),
                
                width="100%",
                height="80vh",
                align_items="center",
                padding="4em"
            ),
            
            # Ensure full viewport coverage
            width="100%",
            height="100vh",
            position="relative"
        )
    )