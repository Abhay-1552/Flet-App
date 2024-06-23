from flet import *
import flet as ft


def main(page: Page):
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    def expand(e):
        if e.data == "true":
            container.content.controls[0].height = 560
            container.content.controls[0].update()
        else:
            container.content.controls[0].height = 660 * 0.40
            container.content.controls[0].update()

    def top():
        _top = Container(
            width=310,
            height=660 * 0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["lightblue600", "lightblue900"],
            ),
            border_radius=35,
            animate=animation.Animation(
                duration=450,
                curve=AnimationCurve.DECELERATE,
            ),
            on_hover=lambda e: expand(e),
            content=Column(
                alignment=MainAxisAlignment.START,
                spacing=10,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value='Signup',
                                size=32,
                                weight=FontWeight.W_500,
                            )
                        ]
                    ),
                    Container(
                        padding=padding.only(bottom=5)
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=90,
                                        height=90,
                                        image_src="./assets/login.png"
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        )

        return _top

    container = Container(
        height=660,
        width=310,
        border_radius=35,
        bgcolor='black',
        padding=10,
        content=Stack(
            width=300,
            height=550,
            controls=[
                top(),
            ]
        )
    )

    page.add(container)


ft.app(target=main)
