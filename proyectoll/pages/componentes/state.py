import reflex as rx

class AuthState(rx.State):
    """Maneja el estado de autenticación"""
    token: str = ""  # Para almacenar el token de sesión
    is_authenticated: bool = False
    
    def login(self, token: str):
        """Método para establecer el estado como autenticado"""
        self.token = token
        self.is_authenticated = True
        return rx.redirect("/dashboard")  # Redirige al área privada
    
    def logout(self):
        """Método para cerrar sesión"""
        self.token = ""
        self.is_authenticated = False
        return rx.redirect("/")  # Redirige al home