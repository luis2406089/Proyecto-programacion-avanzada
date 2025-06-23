import reflex as rx
from proyectoll.pages.componentes.navbar import authenticated_navbar  # Importamos el navbar para autenticados

class DashboardState(rx.State):
    """Estado para la página de dashboard"""
    # Datos del carrusel (pueden venir de una base de datos)
    carousel_items: list[dict] = [
        {"id": 1, "image": "/icono_peliculas.png", "title": "Test1ng Carrusel"},
        {"id": 2, "image": "/icono_peliculas.png", "title": "Testing Carrusel 2"},
        {"id": 3, "image": "/icono_peliculas.png", "title": "Testing Carrusel 3"},
    ]
    
    # Productos para el grid
    products: list[dict] = [
        {"id": i, "name": f"Producto {i}", "price": f"${i*9.99:.2f}"} 
        for i in range(1, 13)
    ]

def carousel_item(item: dict) -> rx.Component:
    """Componente para cada ítem del carrusel"""
    return rx.box(
        rx.image(
            src=item["image"],
            width="100%",
            height="300px",
            object_fit="cover",
            border_radius="12px"
        ),
        rx.box(
            rx.heading(item["title"], size="3", color="white"),
            bg="rgba(0,0,0,0.6)",
            width="100%",
            padding="1em",
            border_bottom_radius="12px"
        ),
        position="relative"
    )

def product_card(product: dict) -> rx.Component:
    """Componente para cada producto en el grid"""
    return rx.box(
        rx.vstack(
            rx.image(
                src=f"/product{product['id']}.jpg",
                width="100%",
                height="150px",
                object_fit="cover",
                border_radius="8px"
            ),
            bg="rgba(21,21,21,0.55)",
            border="0.75px solid #2e2e2e",
            border_radius="8px",
            _hover={
                "border": "0.75px solid teal.400",
                "transform": "translateY(-5px)",
                "transition": "all 0.3s ease"
            }
        ),
        width="100%"
    )

def dashboard() -> rx.Component:
    """Página de dashboard para usuarios autenticados"""
    return rx.box(
        authenticated_navbar(),  # Navbar para usuarios autenticados
        
        # Contenido principal
        rx.center(
            rx.vstack(
                # Carrusel de imágenes
                rx.box(
                    rx.text("Carrusel de Imágenes", size="6", margin_bottom="1em",color="white"),
                    rx.hstack(
                        rx.foreach(
                            DashboardState.carousel_items,
                            lambda item: carousel_item(item)
                        ),
                        spacing="6",
                        overflow_x="auto",
                        width="100%",
                        padding_bottom="0.5em"
                    ),
                    width="100%",
                    margin_bottom="2em"
                ),
                
                # Sección de productos
                rx.heading("Productos Recomendados", size="6", margin_bottom="1em"),
                rx.grid(
                    rx.foreach(
                        DashboardState.products,
                        lambda product: product_card(product)
                    ),
                    columns="3",
                    spacing="6",
                    width="100%"
                ),
                
                width="100%",
                max_width="600px",
                padding="1em",
                padding_top="80px"  # Para que no quede detrás del navbar fijo
            ),
            width="100%",
            bg="#121212",
            min_height="100vh"
        )
    )