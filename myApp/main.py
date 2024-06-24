from flet import *
import flet as ft


def main(page: Page):
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    page.fonts = {"Google Sans": "https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&display=swap"}

    def expand(e):
        if e.data == "true":
            container.content.controls[1].height = 560
            container.content.controls[1].content = Column(
                alignment=MainAxisAlignment.START,
                spacing=10,
                controls=[
                    Container(
                        padding=padding.only(bottom=5)
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Text(
                                        value="Welcome",
                                        size=42,
                                        weight=FontWeight.W_500
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        else:
            container.content.controls[1].height = 480 * 0.40
            container.content.controls[1].content = _top_content

        container.content.controls[1].update()

    text_username = TextField(label='Username', text_align=TextAlign.LEFT, width=200)
    text_email = TextField(label='Email', text_align=TextAlign.LEFT, width=200)
    text_password = TextField(label='Password', text_align=TextAlign.LEFT, width=200, password=True)
    text_confirm_password = TextField(label='Confirm Password', text_align=TextAlign.LEFT, width=200, password=True)
    agree_checkbox = Checkbox(label='Agree to Terms and Conditions', value=False)
    submit_button = ElevatedButton(text='Signup', width=200, disabled=True)

    login_view = Row(
        controls=[
            Column(
                [
                    text_email,
                    text_password,
                    TextButton(text="Don't have an account? Signup"),
                    ElevatedButton(text='Login', width=200)
                ],
                alignment=MainAxisAlignment.CENTER
            )
        ]
    )

    _top_content = Column(
        alignment=MainAxisAlignment.START,
        spacing=10,
        controls=[
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
                                width=140,
                                height=140,
                                image_src="./assets/login.png"
                            )
                        ]
                    )
                ]
            ),
            Container(
                alignment=ft.Alignment(0.75, 0.5),
                content=Text(
                    value="Hover for Signup!",
                    size=12,
                )
            )
        ]
    )

    def top():
        _top = Container(
            width=310,
            height=480 * 0.40,
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
            content=_top_content,
        )

        return _top

    def bottom():
        _bottom = Container(
            padding=padding.only(top=280, left=20, right=20, bottom=20),
            content=login_view,
        )

        return _bottom

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
                bottom(),
                top(),
            ]
        )
    )

    page.add(container)


ft.app(target=main)
