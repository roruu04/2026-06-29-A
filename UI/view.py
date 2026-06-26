import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "TdP  - Esame del 29 Giugno 2026"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("TdP  - Esame del 29 Giugno 2026", color="blue", size=24)
        self._page.controls.append(self._title)


        self._ddCountry = ft.Dropdown(label="Country")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea grafo clienti",
                                               on_click=self._controller.handleCreaGrafo)

        row1 = ft.Row([ft.Container(self._ddCountry, width=250),
                                    ft.Container(self._btnCreaGrafo, width=250)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._btnStampaInfo = ft.ElevatedButton(text="Stampa Info",
                                                on_click=self._controller.handleStampaInfo, width=200)
        self._btnStampaDettagli = ft.ElevatedButton(text="Stampa dettagli artisti",
                                                    on_click=self._controller.handleStampaDettagli, width=200)

        row2 = ft.Row([ft.Container(self._btnStampaInfo, width=250),
                                ft.Container(self._btnStampaDettagli, width=250), ],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row2)

        self._ddClienti = ft.Dropdown(label="Clienti")
        self._btnSequenza = ft.ElevatedButton(text="Trova sequenza clienti",
                                              on_click=self._controller.handleSequenza, width=200)

        row3 = ft.Row([ft.Container(self._ddClienti, width=250),
                       ft.Container(self._btnSequenza, width=250)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()