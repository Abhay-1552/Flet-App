import flet as ft
from flet import *
from flet_core.control_event import ControlEvent


def main(page: Page) -> None:
    page.title = "Login"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = ThemeMode.DARK
    page.window_width = 400
    page.window_height = 600
    page.window_resizable = False

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Signup'), bgcolor='blue'),

                ]
            )
        )

    text_username: TextField = TextField(label='Username', text_align=TextAlign.LEFT, width=200)
    text_email: TextField = TextField(label='Email', text_align=TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password', text_align=TextAlign.LEFT, width=200, password=True)

    agree_checkbox: Checkbox = Checkbox(label='Agree to Terms and Conditions', value=False)
    submit_button: ElevatedButton = ElevatedButton(text='Signup', width=200, disabled=True)

    def validate_form(e: ControlEvent) -> None:
        if all([text_username.value, text_email.value, text_password.value, agree_checkbox.value]) and len(text_password.value) > 8:
            submit_button.disabled = False
        else:
            submit_button.disabled = True
        page.update()

    def submit_form(e: ControlEvent) -> None:
        print(f"Username: {text_username.value}")
        print(f"Email: {text_email.value}")
        print(f"Password: {text_password.value}")

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f"Welcome {text_username.value}", size=20)],
                alignment=MainAxisAlignment.CENTER
            )
        )

    agree_checkbox.on_change = validate_form
    text_username.on_change = validate_form
    text_password.on_change = validate_form
    text_email.on_change = validate_form
    submit_button.on_click = submit_form

    page.add(
        Row(
            controls=[
                Column(
                    [
                        text_username,
                        text_email,
                        text_password,
                        agree_checkbox,
                        submit_button
                    ]
                )
            ],
            alignment=MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    app(target=main)
