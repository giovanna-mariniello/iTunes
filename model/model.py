import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._id_map_album = {}

    def build_grafo(self, durata):
        self._grafo.clear()
        self._grafo.add_nodes_from(DAO.get_albums(durata))

        self._id_map_album = {}
        for nodo in self._grafo.nodes:
            self._id_map_album[nodo.AlbumId] = nodo

        self._grafo.add_edges_from(DAO.get_archi(self._id_map_album))


    def get_dettagli_grafo(self):
        return self._grafo.number_of_nodes(), self._grafo.number_of_edges()

    def get_nodi(self):
        return list(self._grafo.nodes)

    def get_connessa(self, album):
        connessa = nx.node_connected_component(self._grafo, album)
        tot_durata = 0
        for album in connessa:
            tot_durata += album.DurataTot

        return len(connessa), tot_durata/60/1000


