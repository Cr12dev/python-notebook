import reflex as rx
from .back import State
from .components.header import header

import reflex as rx


def index():
    # Bucle principal de la aplicacion
    return rx.box(
        header(),
        style={"width": "100%", "max_width": "100%"}
    )