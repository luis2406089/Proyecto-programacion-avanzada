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

def authenticated_navbar():
    """Navbar para usuarios autenticados"""
    return rx.box(
        rx.hstack(
            # Dropdown a la izquierda
            rx.menu(
                rx.menu_button(
                    rx.hstack(
                        rx.avatar(size="sm"),
                        rx.icon(tag="chevron-down", size="14px"),
                        spacing="2"
                    ),
                    bg="transparent",
                    _hover={"bg": "rgba(255,255,255,0.1)"},
                ),
                rx.menu_list(
                    rx.link(
                        rx.menu_item("Perfil"),
                        href="/profile",
                    ),
                    rx.link(
                        rx.menu_item("Configuración"),
                        href="/settings",
                    ),
                    rx.menu_divider(),
                    rx.link(
                        rx.menu_item("Cerrar sesión", color="red.500"),
                        href="/logout",
                    ),
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
            align_items="center",
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