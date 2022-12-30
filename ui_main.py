import flet as ft
import os
from flet.text import TextAlign
from download import download

file = f'C:/Users/{os.getlogin()}/Downloads'

cont1 = ft.Container(
    alignment=ft.alignment.center,
    height=25,
    border_radius=ft.border_radius.all(10),
    bgcolor=ft.colors.BLUE_GREY_800,
    content=ft.Text(f'Path: {file}', size=15, font_family="Verdana", text_align=TextAlign.CENTER),
)

cont = ft.Container(
    content=ft.Dropdown(
        width=300,
        label="Quality",
        hint_text="Choose the quality of the video*",
        options=[
            ft.dropdown.Option("144p"),
            ft.dropdown.Option("240p"),
            ft.dropdown.Option("360p"),
            ft.dropdown.Option("480p"),
            ft.dropdown.Option("720p"),
            ft.dropdown.Option("1080p"),
            ft.dropdown.Option("1440p"),
            ft.dropdown.Option("2160p"),
        ],
        alignment=ft.alignment.bottom_center,
    ),
)

dd = ft.Dropdown(
    label="Type*",
    border_color=ft.colors.BLUE_GREY,
    options=[
        ft.dropdown.Option("Audio"),
        ft.dropdown.Option("Video"),
        ft.dropdown.Option("Both"),
    ],
    alignment=ft.alignment.bottom_center,
)

linkfield = ft.TextField(
    width=500,
    label="Link*",
    hint_text="Insert the link here",
)

filenamefield = ft.TextField(
    width= 300,
    label="Filename",
    hint_text="Insert a filename"
)

checkbx = ft.Checkbox(
    label="Is this a members only/private video?",
    value=False,
    label_position=ft.LabelPosition.LEFT,
    fill_color=ft.colors.BLUE_GREY,
)

elevbtn = ft.ElevatedButton(
    content=ft.Text("Download", size=18, font_family="Verdana"),
    on_click=lambda _:download(dd.value, linkfield.value, cont.content.value, file, filenamefield.value),
    style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=10),
        padding=ft.padding.symmetric(horizontal=30, vertical=15),
    ),
)

def main(page: ft.Page):

    sel_folder_dialog = ft.FilePicker(on_result=openDial)
    page.overlay.append(sel_folder_dialog)


    page.title = "Youtube Downloader"
    page.window_height = 700
    page.window_width = 1000
    page.window_resizable = False
    page.window_maximizable = False
    page.add(
        ft.Row(
            controls=[
                ft.Container(
                padding=ft.padding.all(30),
                width=200,
                height=640,
                border=ft.border.all(2, ft.colors.BLUE_GREY),
                border_radius=ft.border_radius.all(10),
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.START,
                    spacing=50,
                    controls=[
                        ft.Text("What do you want to download?", size=15, font_family="Verdana", text_align=TextAlign.CENTER),
                        dd,
                        ft.Container(
                            padding=ft.padding.only(top=300),
                            content=ft.Dropdown(
                                label="Theme",
                                border_color=ft.colors.BLUE_GREY,
                                options=[
                                    ft.dropdown.Option("LIGHT"),
                                    ft.dropdown.Option("DARK"),
                                ],
                                alignment=ft.alignment.bottom_center,
                            ),
                        )
                        
                    ]
                ),
            ),
            ft.Container(
                padding=ft.padding.all(30),
                width=780,
                height=640,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.START,
                    spacing=70,
                    controls=[
                        ft.Text("Insert the link of the video you want to download", size=15, font_family="Verdana"),
                        linkfield, 
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.ElevatedButton(
                                    text="Choose the path*",
                                    on_click=lambda _: sel_folder_dialog.get_directory_path(initial_directory=file, dialog_title="Choose a folder"),
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    )
                                ),
                                checkbx
                            ],
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                filenamefield,
                                cont
                            ]
                        ),
                        elevbtn,
                        cont1
                    ]
                ),
            )
            ]
        )
    )

def openDial(e: ft.FilePickerResultEvent):
    global file
    file = e.path
    cont1.content = ft.Text(f'Path: {file}', size=15, font_family="Verdana")
    cont1.update()
    elevbtn.update()




ft.app(target=main)