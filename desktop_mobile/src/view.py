import flet as ft


SNACK_BAR_COLORS = {
    'success': ft.Colors.GREEN,
    'error': ft.Colors.ERROR,
    'neutral': ft.Colors.SURFACE,
}


class View(ft.View):

    def __init__(self, page: ft.Page,  **kwargs):
        super().__init__(**kwargs)

        self._page = page

        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.Icons.MENU_BOOK),
            title=ft.Text(f"DmNotes - {self.title}"),
            center_title=False,
            actions=[
                #ft.PopupMenuButton(
                #    items=[ft.PopupMenuItem(text="Item 1")]
                #),
            ],
        )

        views_data = {
            '/characters': ft.Icons.PERSON,
            '/places': ft.Icons.PLACE,
            '/events': ft.Icons.EVENT,
            '/items': ft.Icons.CATEGORY,
            '/sheets': ft.Icons.DESCRIPTION,
            '/dungeons': ft.Icons.CASTLE,
        }

        self.bottom_appbar = ft.BottomAppBar(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                controls=[
                    ft.IconButton(
                        expand=1,
                        icon=icon,
                        icon_color=ft.Colors.PRIMARY if route == self.route else ft.Colors.WHITE,
                        on_click=lambda _, r=route: self._page.go(r)
                    ) for route, icon in views_data.items()
                ]
            ),
        )

        self.snack_bar = ft.SnackBar(content=ft.Text(
            color=ft.Colors.WHITE
        ))

        self.render()

    def message(self, message, type='success'):
        self.snack_bar.content.value = message
        self.snack_bar.open = True
        self.snack_bar.bgcolor = SNACK_BAR_COLORS[type]
        self._page.add(self.snack_bar)

    def render(self):
        pass
