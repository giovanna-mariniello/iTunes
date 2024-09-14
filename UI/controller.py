import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()

        durata_min = self._view._txtInDurata.value

        try:
            int_durata_min = int(durata_min)
        except ValueError:
            self._view.create_alert("Per favore inserisci un valore intero")

        self._model.build_grafo(int_durata_min)
        num_nodi, num_archi = self._model.get_dettagli_grafo()
        self._view.txt_result.controls.append(ft.Text("Grafo creato!"))
        self._view.txt_result.controls.append(ft.Text(f"# nodi: {num_nodi}"))
        self._view.txt_result.controls.append(ft.Text(f"# vertici: {num_archi}"))

        nodi = self._model.get_nodi()
        nodi.sort(key=lambda x:x.Title)
        print(nodi)
        for n in nodi:
            self._view._ddAlbum.options.append(ft.dropdown.Option(data=n, text=n.Title, on_click=self.getSelectedAlbum))

        self._view.update_page()


    def getSelectedAlbum(self, e):
        if e.control.data is None:
            self._album_scelto = None
        else:
            self._album_scelto = e.control.data
        print(self._album_scelto, type(self._album_scelto))


    def handleAnalisiComp(self, e):
        self._view.txt_result.controls.clear()

        if self._album_scelto is None:
            self._view.create_alert("Per favore seleziona un album")
            return

        dim_conn, durata_conn = self._model.get_connessa(self._album_scelto)
        self._view.txt_result.controls.append(ft.Text(f"Componente connessa - {album}"))
        self._view.txt_result.controls.append(ft.Text(f"Dimensione della componente connessa: {dim_conn}"))
        self._view.txt_result.controls.append(ft.Text(f"Durata della connessa: {durata_conn}"))
        self._view.update_page()

    def handleGetSetAlbum(self, e):
        pass