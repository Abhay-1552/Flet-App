import flet as ft
from flet import (Page, MainAxisAlignment, ThemeMode, TextField, TextAlign, Checkbox, ElevatedButton, TextButton,
                  Row, Column, Text)


def main(page: Page):
    page.title = "Login"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = ThemeMode.DARK
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    def show_view(view):
        page.clean()
        page.add(view)

    def login(e):
        email = text_email.value
        password = text_password.value
        if email == "test@example.com" and password == "password":
            show_view(Text("Login Successful!"))
        else:
            show_view(ft.Column([Text("Login Failed!"), login_view]))

    def signup(e):
        email = text_email.value
        password = text_password.value
        confirm_password = text_confirm_password.value
        if password == confirm_password:
            show_view(ft.Column([Text("Signup Successful! Please Login"), ElevatedButton(text="Login", on_click=lambda _: show_view(login_view))]))
        else:
            show_view(ft.Column([Text("Passwords do not match!"), signup_view]))

    def validate_form(e):
        valid = all([text_username.value, text_email.value, text_password.value, text_confirm_password.value, agree_checkbox.value])
        submit_button.disabled = not valid

        text_password.color = 'red' if len(text_password.value) < 8 else 'white'
        text_confirm_password.color = 'red' if len(text_confirm_password.value) < 8 or text_password.value != text_confirm_password.value else 'white'

        page.update()

    text_username = TextField(label='Username', text_align=TextAlign.LEFT, width=200)
    text_email = TextField(label='Email', text_align=TextAlign.LEFT, width=200)
    text_password = TextField(label='Password', text_align=TextAlign.LEFT, width=200, password=True)
    text_confirm_password = TextField(label='Confirm Password', text_align=TextAlign.LEFT, width=200, password=True)
    agree_checkbox = Checkbox(label='Agree to Terms and Conditions', value=False)
    submit_button = ElevatedButton(text='Signup', width=200, disabled=True, on_click=signup)

    login_view = Row(
        controls=[
            Column(
                [
                    TextField(label='Email', text_align=TextAlign.LEFT, width=200),
                    text_password,
                    TextButton(text="Don't have an account? Signup", on_click=lambda _: show_view(signup_view)),
                    ElevatedButton(text='Login', width=200, on_click=login)
                ],
                alignment=MainAxisAlignment.CENTER
            )
        ]
    )

    signup_view = Row(
        controls=[
            Column(
                [
                    text_username,
                    text_email,
                    text_password,
                    text_confirm_password,
                    agree_checkbox,
                    TextButton(text="Already have an account? Login", on_click=lambda _: show_view(login_view)),
                    submit_button
                ],
                alignment=MainAxisAlignment.CENTER
            )
        ]
    )

    agree_checkbox.on_change = validate_form
    text_username.on_change = validate_form
    text_email.on_change = validate_form
    text_password.on_change = validate_form
    text_confirm_password.on_change = validate_form

    show_view(login_view)
    page.update()


ft.app(target=main, view=ft.FLET_APP)
