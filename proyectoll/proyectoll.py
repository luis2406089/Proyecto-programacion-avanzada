import reflex as rx
from proyectoll.pages.auth.login import login
from proyectoll.pages.auth.register import register
from sqlmodel import SQLModel
from proyectoll.modelos.usuarios import Usuario
from proyectoll.pages.home import home

class State(rx.State):
    """Estado compartido entre páginas"""
    pass


app = rx.App()

# Registrar páginas principales
app.add_page(home, route="/")
app.add_page(login, route="/login")
app.add_page(register, route="/register")