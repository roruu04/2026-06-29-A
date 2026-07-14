import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._idMapClienti = {}

    #passo dati per fillare
    def fillDDCountry(self):
        return DAO.getAllCountry()

    #build grafo orientato e pesato
    def buildGraph(self, paese):
        self._graph.clear()

        #NODI clienti >=1 fattura, del paese, memorizzare fatturato totale
        nodi = DAO.getNodesClienti(paese)
        #dizionario di clienti per risalire da codice
        for n in nodi:
            self._idMapClienti[n.CustomerId] = n
        #popolo grafo
        self._graph.add_nodes_from(nodi)

        #ARCHI almeno un artista compare in fattura di entrambi
        archi = DAO.getArchi(paese, self._idMapClienti)
        for a in archi:
            self._graph.add_edge(a.c1, a.c2, weight=a.peso)

    def getDetails(self):
        return len(self._graph.nodes()), len(self._graph.edges())

    #stampa info
    def stampaInfo(self):
        # per ogni nodo associa la somma dei pesi uscenti ed entranti
        listNodesPesati = []
        for n in self._graph.nodes():
            score = 0
            for e in self._graph.out_edges(n, data=True):
                score += e[2]['weight']
            for e in self._graph.in_edges(n, data=True):
                score -= e[2]["weight"]
            listNodesPesati.append((n, score))
        listNodesPesati.sort(key=lambda x: x[1], reverse=True)
        return listNodesPesati[0], sorted(self._graph.edges(data=True), reverse=True, key=lambda x:x[2]['weight'])