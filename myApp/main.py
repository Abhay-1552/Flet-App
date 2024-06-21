from flet import *


def main(page: Page):
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    container = Container(
        height=660,
        width=310,
        border_radius=35,
        bgcolor='blue',
        padding=10
    )

    page.add(container)


app(target=main)
