import reflex as rx
from proyectoll.pages.componentes.navbar import navbar


class HomeState(rx.State):
    """State for home page interactions"""
    dialog_open: bool = False
    
    def toggle_dialog(self):
        """Toggle the dialog open/close state"""
        self.dialog_open = not self.dialog_open

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
                        'Simulador de: "PopcornHour": portal web para recomendar, calificar y discutir sobre películas y series. Existirán dos tipos de usuarios: moderador y estándar. Los usuarios de tipo "moderador" contarán con la posibilidad para subir películas que los usuarios de tipo estándar puedan calificar, comentar y discutir sobre ellas. Los usuarios de tipo estándar podrán calificar, comentar y discutir sobre las películas que los moderadores suban al portal web.', 
                        color="rgba(255,255,255,0.9)",
                        font_size="lg"
                    ),
                    
                    # Dialog component
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.button(
                                "Get Started",
                                color_scheme="teal",
                                size="3",
                                padding="1.5em 2em",
                                margin_top="2rem",
                            )
                        ),
                        rx.dialog.content(
                            rx.dialog.title(
                                "Bienvenido a PopcornHour",
                                margin_bottom="1rem"
                            ),
                            rx.dialog.description(
                                "Tu portal de películas y series favorito"
                            ),
                            
                            # Contenido del dialog: imagen y texto
                            rx.vstack(
                                # Imagen
                                rx.image(
                                    src="/icono_peliculas.png",  # Reemplaza con tu imagen
                                    width="200px",
                                    height="150px",
                                    object_fit="contain",
                                    margin="1rem 0"
                                ),
                                
                                # Texto descriptivo
                                rx.text(
                                    "PopcornHour es el lugar perfecto para descubrir nuevas películas y series, "
                                    "compartir tus opiniones y conectar con otros cinéfilos. "
                                    "Únete a nuestra comunidad y comienza tu experiencia cinematográfica.",
                                    text_align="center",
                                    color="gray.600",
                                    margin="1rem 0"
                                ),
                                
                                # Botones de acción
                                rx.hstack(
                                    rx.dialog.close(
                                        rx.button(
                                            "Cancelar",
                                            variant="outline",
                                            color_scheme="gray"
                                        )
                                    ),
                                    rx.dialog.close(
                                        rx.button(
                                            "Ir a Registro",
                                            color_scheme="teal",
                                            on_click=rx.redirect("/register")
                                        )
                                    ),
                                    spacing="3",
                                    margin_top="1rem"
                                ),
                                
                                spacing="3",
                                align_items="center"
                            ),
                            
                            max_width="500px",
                            padding="2rem"
                        )
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