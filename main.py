
import flet as ft
import datetime 


def main_page(page: ft.Page):
    page.theme_mode = "dark"
    page.title = "Угар"
    name = "Эламан"
    
    # print(name_flet)
    # print(name_flet.value)
    # print(name_flet.color)

    # name_input = ft.TextField(max_length= 10)
    # text_button = ft.TextButton('text_button')
    # icon_button = ft.IconButton(icon = ft.Icons.TELEGRAM)
    
    text_hello = ft.Text(value='Hello World', color=ft.Colors.RED)

    def button_click(e):
        if name_input.value:
            name = name_input.value.strip()
            text_hello.value = f'Hello {name}'
            name_input.value = None
            text_hello.color = None
        else:
            text_hello.value = "Ошибка"
            text_hello.color = ft.Colors.RED

    name_input = ft.TextField(on_submit=button_click)
    button_elevate = ft.ElevatedButton('send', icon = ft.Icons.SEND, on_click = button_click)


    page.add(

        text_hello,
        name_input,
        button_elevate
            

    )

ft.run(main_page)











