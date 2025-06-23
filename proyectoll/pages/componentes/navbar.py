import reflex as rx

class NavState(rx.State):
    """Estado para manejar la navegación"""
    @rx.var
    def current_page(self) -> str:
        """Obtiene la ruta actual"""
        return self.router.page.path

def navbar():
    """Barra de navegación con icono de inicio y detección de página activa"""
    return rx.box(
        rx.hstack(
            # Icono de Home (nuevo elemento)
            rx.link(
                rx.icon(
                    tag="home",
                    size=24,
                    color="rgba(255,255,255,0.9)",
                    _hover={"color": "teal.400"},
                    margin_left="2em"
                ),
                href="/",
            ),
            
            rx.spacer(),  # Empuja los botones a la derecha
            
            # Botón de Login
            rx.link(
                rx.button(
                    "Login",
                    variant=rx.cond(
                        NavState.current_page == "/login",
                        "solid",
                        "ghost"
                    ),
                    color_scheme="teal",
                    border_radius="8px",
                    _hover={"bg": "rgba(74, 222, 128, 0.1)"}
                ),
                href="/login",
            ),
            
            # Botón de Register
            rx.link(
                rx.button(
                    "Register",
                    variant=rx.cond(
                        NavState.current_page == "/register",
                        "solid",
                        "ghost"
                    ),
                    color_scheme="teal",
                    border_radius="8px",
                    _hover={"bg": "rgba(74, 222, 128, 0.1)"}
                ),
                href="/register",
            ),
            
            spacing="4",
            padding_right="2em",
            justify_content="flex-end",
            width="100%",
        ),
        position="fixed",
        top="0",
        width="100%",
        bg="rgba(21,21,21,0.9)",
        backdrop_filter="blur(10px)",
        z_index="999",
        padding="1em 0",
        border_bottom="1px solid #2e2e2e",
    )