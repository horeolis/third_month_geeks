import flet as ft 

def main_page(page: ft.Page):
    page.theme_mode = "dark"
    page.title = 'Мое первое приложение'

    text_hello = ft.Text(value='Hello world')

    greeting_history = []
    history_text = ft.Text(value='История приветствий:')


    def on_button_click(_):
        # print(name_input.value)

        if name_input.value:
            name = name_input.value.strip()
            text_hello.value = f'Hello {name}'
            name_input.value = None
            text_hello.color = None

            greeting_history.append(name)
            print(greeting_history)
            history_text.value = "История приветсвий:\n" + "\n".join(greeting_history)
        else: 
            text_hello.value = 'Введите имя!'
            text_hello.color = ft.Colors.RED

    name_input = ft.TextField(on_submit=on_button_click)
    button_elevated = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=on_button_click)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветсвий:"

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    def del_last(_):
        if greeting_history:
            greeting_history.pop()
        history_text.value = "История приветсвий:" if not greeting_history else "История приветсвий:\n" + "\n".join(greeting_history)

    del_last_button = ft.IconButton(icon=ft.Icons.CLEAR, on_click=del_last)

    def sort_func(_):
        greeting_history.sort()
        history_text.value = "История приветсвий:\n" + "\n".join(greeting_history)


    sort_button = ft.IconButton(icon = ft.Icons.SORT, on_click = sort_func)


    page.add(
        ft.Column(
            [
                text_hello,
                ft.Row(
                    [
                        name_input, 
                    ],
                    alignment = "center"
                ),
                button_elevated, 
                clear_button, 
                del_last_button,
                sort_button,
                history_text,
            ],
            horizontal_alignment="center"
        ),
    )

ft.run(main_page)
