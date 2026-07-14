import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCreaGrafo(self, e):
        self._view._txt_result.controls.clear()
        self._model.buildGraph(self._view._ddCountry.value) #chiamo il metodo per creare grafo passando il paese selezionato
        nodi, archi = self._model.getDetails()
        self._view._txt_result.controls.append(ft.Text(f"Grafo correttamente creato.\nIl grafo ha {nodi} nodi e {archi} archi."))
        self._view.update_page()
    def handleStampaInfo(self,e):
        self._view._txt_result.controls.clear()
        nodoInfluente, archiPesanti = self._model.stampaInfo()
        self._view._txt_result.controls.append(
            ft.Text(f"Il cliente più influente è {nodoInfluente}.\nDi seguito i 5 archi più pesanti:"))
        for e in archiPesanti:
            self._view._txt_result.controls.append(e)
        self._view.update_page()

    def handleSequenza(self,e):
        pass


    #fillo il DD di country
    def fillDDCountry(self):
        self._view._ddCountry.options = list(map(lambda x: ft.dropdown.Option(x), self._model.fillDDCountry()))

