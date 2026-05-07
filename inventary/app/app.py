from .ui import *

app = rx.App(
    style={
        "width": "100vw",
        "max_width": "100vw",
    },
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
    ]
)

app.add_page(index, route="/", title="InventarioPro")