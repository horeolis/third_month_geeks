
import flet as ft
import datetime 

def main_page(page: ft.Page):
    page.theme_mode = "dark"
    page.title = "Приветствие"
        
    text_hello = ft.Text(value= None, color = None)
    text_field = ft.TextField()
    warn_text = ft.Text(value = None)

    

    def button_click(e):
        
        hello_date = datetime.datetime.now()
        formatted_date = hello_date.strftime("%Y:%m:%d - %H:%M:%S")

        if not text_field.value:
            text_hello.value = "Впишите свое имя ниже!"
            return

        text_hello.value = f"{formatted_date} - Привет, {text_field.value}!".upper()
        


        

    hello_button = ft.IconButton(icon = ft.Icons.EMOJI_EMOTIONS, on_click=button_click)

    page.add(
        ft.Column(
            [
                text_hello,
                ft.Row(
                    [
                        text_field,
                        hello_button,
                        warn_text,
                    ],
                    alignment="center"
                ),
            ],
            horizontal_alignment="center"
        )
    )



    # - Добавить время когда ввели имя. В формате - год:месяц:день - час:минута:секунда
    # - Выводить сообщение: “2025:12:02 - 18:23:22 - Привет, {имя}! ”
  
        


ft.run(main_page)











