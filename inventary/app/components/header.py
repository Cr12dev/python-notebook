import reflex as rx


def nav_item(icon: str, text: str, href: str):
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(
                text,
                class_name="hidden md:block font-medium"
            ),
            spacing="2",
            align="center",
        ),
        href=href,
        class_name="""
            px-4
            py-2.5
            rounded-2xl

            text-zinc-400
            hover:text-white
            hover:bg-gradient-to-r
            hover:from-blue-500/20
            hover:to-indigo-500/20
            hover:border-blue-500/30
            hover:shadow-lg
            hover:shadow-blue-500/10

            transition-all
            duration-300
            hover:scale-105
        """
    )


def header():
    return rx.box(
        rx.box(
            rx.flex(
                # =========================
                # LEFT SIDE
                # =========================
                rx.hstack(
                    rx.box(
                        rx.icon(
                            "package-2",
                            size=24,
                            class_name="text-white"
                        ),

                        class_name="""
                            bg-gradient-to-br
                            from-blue-500
                            via-indigo-500
                            to-purple-600

                            p-3
                            rounded-2xl

                            shadow-xl
                            shadow-blue-500/30

                            ring-2
                            ring-blue-400/20
                            ring-offset-2
                            ring-offset-zinc-950
                        """
                    ),

                    rx.vstack(
                        rx.heading(
                            "InventarioPro",
                            size="5",
                            class_name="""
                                bg-gradient-to-r
                                from-white
                                to-blue-100
                                bg-clip-text
                                text-transparent

                                font-bold
                                tracking-tight
                                leading-none
                            """
                        ),

                        rx.text(
                            "Gestión inteligente de stock",
                            class_name="""
                                text-xs
                                text-zinc-400
                                hidden sm:block
                            """
                        ),

                        spacing="1",
                        align="start",
                    ),

                    spacing="4",
                    align="center",
                ),

                # =========================
                # CENTER NAVIGATION
                # =========================
                rx.hstack(
                    nav_item(
                        "layout-dashboard",
                        "Dashboard",
                        "/"
                    ),

                    nav_item(
                        "boxes",
                        "Productos",
                        "/productos"
                    ),

                    nav_item(
                        "archive",
                        "Stock",
                        "/stock"
                    ),

                    nav_item(
                        "bar-chart-3",
                        "Reportes",
                        "/reportes"
                    ),

                    spacing="2",

                    class_name="""
                        hidden lg:flex

                        bg-gradient-to-r
                        from-white/5
                        to-white/[0.02]
                        border
                        border-white/10

                        backdrop-blur-xl

                        px-3
                        py-2

                        rounded-3xl

                        shadow-lg
                        shadow-black/20
                    """
                ),

                # =========================
                # RIGHT SIDE
                # =========================
                rx.hstack(
                    # Search button
                    rx.button(
                        rx.icon("search", size=18),

                        class_name="""
                            hidden md:flex

                            bg-gradient-to-br
                            from-white/5
                            to-white/[0.02]
                            hover:from-blue-500/20
                            hover:to-indigo-500/20

                            border
                            border-white/10
                            hover:border-blue-400/30

                            text-zinc-300
                            hover:text-white

                            rounded-2xl

                            h-11
                            w-11

                            shadow-md
                            shadow-black/10
                            hover:shadow-lg
                            hover:shadow-blue-500/10

                            transition-all
                            duration-300
                            hover:scale-105
                        """
                    ),

                    # Add product button
                    rx.button(
                        rx.hstack(
                            rx.icon("plus", size=18),

                            rx.text(
                                "Nuevo",
                                class_name="hidden sm:block"
                            ),

                            spacing="2",
                            align="center",
                        ),

                        class_name="""
                            bg-gradient-to-r
                            from-blue-600
                            via-indigo-600
                            to-purple-600

                            hover:from-blue-500
                            hover:via-indigo-500
                            hover:to-purple-500

                            text-white
                            font-semibold

                            rounded-2xl

                            px-4
                            h-11

                            shadow-xl
                            shadow-blue-500/30
                            hover:shadow-2xl
                            hover:shadow-blue-500/40

                            hover:scale-105

                            transition-all
                            duration-300

                            ring-2
                            ring-blue-400/20
                            ring-offset-2
                            ring-offset-zinc-950
                            hover:ring-blue-400/40
                        """
                    ),

                    # User card
                    rx.box(
                        rx.hstack(
                            rx.avatar(
                                fallback="C",
                                size="3",
                                class_name="""
                                    ring-2
                                    ring-blue-400/30
                                    ring-offset-2
                                    ring-offset-zinc-950
                                """
                            ),

                            rx.vstack(
                                rx.text(
                                    "",
                                    class_name="""
                                        text-sm
                                        font-semibold
                                        text-white
                                    """
                                ),

                                rx.text(
                                    "Administrador",
                                    class_name="""
                                        text-xs
                                        text-zinc-400
                                    """
                                ),

                                spacing="0",
                                align="start",
                            ),

                            spacing="3",
                            align="center",
                        ),

                        class_name="""
                            hidden md:block

                            bg-gradient-to-r
                            from-white/5
                            to-white/[0.02]
                            border
                            border-white/10
                            hover:border-blue-400/30

                            px-4
                            py-2

                            rounded-2xl

                            backdrop-blur-xl

                            shadow-md
                            shadow-black/10
                            hover:shadow-lg
                            hover:shadow-blue-500/10

                            transition-all
                            duration-300
                            hover:scale-105
                        """
                    ),

                    # Mobile menu
                    rx.button(
                        rx.icon("menu", size=22),

                        class_name="""
                            flex lg:hidden

                            bg-gradient-to-br
                            from-white/5
                            to-white/[0.02]
                            hover:from-blue-500/20
                            hover:to-indigo-500/20

                            border
                            border-white/10
                            hover:border-blue-400/30

                            rounded-2xl

                            h-11
                            w-11

                            text-zinc-300
                            hover:text-white

                            shadow-md
                            shadow-black/10
                            hover:shadow-lg
                            hover:shadow-blue-500/10

                            transition-all
                            duration-300
                            hover:scale-105
                        """
                    ),

                    spacing="3",
                    align="center",
                ),

                justify="between",
                align="center",

                width="100%",
            ),

            class_name="""
                px-4
                sm:px-6
                lg:px-8
            """
        ),

        style={
            "position": "fixed",
            "top": "0",
            "left": "0",
            "right": "0",
            "width": "100vw",
            "maxWidth": "100vw",
            "zIndex": "50",
        },

        class_name="""
            py-4

            bg-gradient-to-b
            from-zinc-950/90
            to-zinc-950/70
            backdrop-blur-2xl

            border-b
            border-white/10

            shadow-xl
            shadow-black/30
        """
    )