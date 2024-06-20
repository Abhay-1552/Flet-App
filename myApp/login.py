import flet as ft
from flet import *
from flet_core.control_event import ControlEvent


def main(page: Page):
    page.title = "Login"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = ThemeMode.DARK
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    def show_login(e: ControlEvent):
        page.clean()
        page.add(login_view)

    def show_signup(e: ControlEvent):
        page.clean()
        page.add(signup_view)

    def login(e: ControlEvent):
        email = text_email.value
        password = text_password.value
        # Here, add your authentication logic
        if email == "test@example.com" and password == "password":
            page.clean()
            page.add(ft.Text("Login Successful!"))
        else:
            page.clean()
            page.add(ft.Text("Login Failed!"), login_view)

    def signup(e: ControlEvent):
        email = text_email.value
        password = text_password.value
        confirm_password = text_confirm_password.value
        # Here, add your registration logic
        if password == confirm_password:
            page.clean()
            page.add(ft.Text("Signup Successful! Please Login"), ElevatedButton(text="Login", on_click=show_login))
        else:
            page.clean()
            page.add(ft.Text("Passwords do not match!"), signup_view)

    def validate_form(e: ControlEvent) -> None:
        if all([text_username.value, text_email.value, text_password.value, text_confirm_password.value, agree_checkbox.value]):
            submit_button.disabled = False
        else:
            submit_button.disabled = True

        if len(text_password.value) < 8:
            text_password.color = 'red'
        else:
            text_password.color = 'white'

        if text_password.value != text_confirm_password.value:
            text_confirm_password.color = 'red'
        else:
            text_confirm_password.color = 'white'
            
        page.update()

    # Login view
    text_username: TextField = TextField(label='Username', text_align=TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password', text_align=TextAlign.LEFT, width=200, password=True)

    agree_checkbox: Checkbox = Checkbox(label='Agree to Terms and Conditions', value=False)
    submit_button: ElevatedButton = ElevatedButton(text='Signup', width=200, disabled=True, on_click=login)

    signup_link = ft.TextButton(text="Don't have an account? Signup", on_click=show_signup)
    login_view = Row(
        controls=[
            Column(
                [
                    text_username,
                    text_password,
                    agree_checkbox,
                    signup_link,
                    submit_button
                ]
            )
        ],
        alignment=MainAxisAlignment.CENTER
    )

    # Signup view
    text_username: TextField = TextField(label='Username', text_align=TextAlign.LEFT, width=200)
    text_email: TextField = TextField(label='Email', text_align=TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password', text_align=TextAlign.LEFT, width=200, password=True)
    text_confirm_password: TextField = TextField(label='Confirm Password', text_align=TextAlign.LEFT, width=200, password=True)

    agree_checkbox: Checkbox = Checkbox(label='Agree to Terms and Conditions', value=False)
    submit_button: ElevatedButton = ElevatedButton(text='Signup', width=200, disabled=True, on_click=signup)

    login_link = ft.TextButton(text="Already have an account? Login", on_click=show_login)
    signup_view = Row(
        controls=[
            Column(
                [
                    text_username,
                    text_email,
                    text_password,
                    text_confirm_password,
                    agree_checkbox,
                    login_link,
                    submit_button
                ]
            )
        ],
        alignment=MainAxisAlignment.CENTER
    )

    agree_checkbox.on_change = validate_form
    text_username.on_change = validate_form
    text_email.on_change = validate_form
    text_password.on_change = validate_form
    text_confirm_password.on_change = validate_form

    # Initial view
    show_login(None)

    page.update()


ft.app(target=main, view=FLET_APP)
