import flet as ft


def app(page: ft.Page) -> None:
    counter = ft.Text("0", size=50)
    counter_data = 0

    def increment_click(e):
        nonlocal counter_data
        counter_data += 1
        counter.value = str(counter_data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )
