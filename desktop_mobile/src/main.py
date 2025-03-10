import flet as ft
from character import CharactersView
from dungeons import DungeonsView
from events import EventsView
from items import ItemsView
from places import PlacesView
from sheets import SheetsView


def main(page: ft.Page):
    page.title = "DmNotes"
    page.window.alignment = ft.alignment.top_right
    page.window.width = 400
    page.window.icon = "ico.ico"
    page.scroll = "auto"

    page.views.extend([
        SheetsView(page, route='/sheets'),
        ItemsView(page, route='/items'),
        EventsView(page, route='/events'),
        PlacesView(page, route='/places'),
        DungeonsView(page, route='/dungeons'),
        CharactersView(page, route='/characters'),
    ])

    def on_route_change(e):
        page.views.sort(key=lambda view: view.route == page.route)
        page.update()

    page.on_route_change = on_route_change
    
    page.go('/characters')

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
