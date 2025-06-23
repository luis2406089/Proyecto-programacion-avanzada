import reflex as rx

class NavState(rx.State):
    """Estado para manejar la navegación y dropdown"""
    show_dropdown: bool = False
    
    @rx.var
    def current_page(self) -> str:
        """Obtiene la ruta actual"""
        return self.router.page.path
    
    def toggle_dropdown(self):
        """Alternar visibilidad del dropdown"""
        self.show_dropdown = not self.show_dropdown

def navbar() -> rx.Component:
    """Barra de navegación para usuarios NO autenticados"""
    return rx.box(
        rx.hstack(
            # Icono de Home
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
            justify="end",
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

def authenticated_navbar() -> rx.Component:
    """Barra de navegación para usuarios autenticados"""
    return rx.box(
        rx.hstack(
            # Dropdown a la izquierda usando rx.popover
            rx.popover.root(
                rx.popover.trigger(
                    rx.button(
                        rx.hstack(
                            rx.avatar(size="3"),
                            rx.icon(
                                tag="menu",
                                size=20,
                                color="rgba(255,255,255,0.8)",
                                _hover={"color": "teal.400"}
                            ),
                            spacing="2"
                        ),
                        variant="ghost",
                        _hover={"bg": "rgba(255,255,255,0.1)"},
                    ),
                ),
                rx.popover.content(
                    rx.vstack(
                        rx.link(
                            rx.button("Perfil", variant="ghost", width="100%"),
                            href="/profile",
                        ),
                        rx.link(
                            rx.button("Configuración", variant="ghost", width="100%"),
                            href="/settings",
                        ),
                        rx.divider(),
                        rx.link(
                            rx.button("Cerrar sesión", variant="ghost", width="100%", color="red.500"),
                            href="/logout",
                        ),
                        spacing="1",
                        width="150px",
                        padding="0.5em",
                    ),
                    bg="rgba(21,21,21,0.95)",
                    border="1px solid #2e2e2e",
                    border_radius="8px",
                ),
                margin_left="2em",
            ),
            
            # Barra de búsqueda centrada
            rx.center(
                rx.hstack(
                    rx.input(
                        placeholder="Buscar...",
                        width=["200px", "300px", "400px"],  # Responsivo
                        bg="rgba(255,255,255,0.1)",
                        border="none",
                        _focus={"border": "1px solid teal"},
                    ),
                    rx.button(
                        rx.icon(tag="search"),
                        color_scheme="teal",
                        variant="solid",
                    ),
                    spacing="2",
                ),
                flex="1",
            ),
            
            # Iconos a la derecha
            rx.hstack(
                rx.link(
                    rx.icon(
                        tag="bell",
                        size=20,
                        color="rgba(255,255,255,0.8)",
                        _hover={"color": "teal.400"},
                    ),
                    href="/notifications",
                ),
                rx.link(
                    rx.icon(
                        tag="mail",
                        size=20,
                        color="rgba(255,255,255,0.8)",
                        _hover={"color": "teal.400"},
                        margin_right="2em",
                    ),
                    href="/messages",
                ),
                spacing="4",
            ),
            
            width="100%",
            align="center",
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