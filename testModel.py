from model.model import Model
#from model.album import ALbum

mymodel = Model()
mymodel.build_grafo(120)
print(mymodel.get_dettagli_grafo())

print(mymodel.get_nodi())
print(type(mymodel.get_nodi()[0]))
# album = Album()
connessa, dim_connessa = mymodel.get_connessa("Unplugged")
durata = mymodel.get_durata_connessa(connessa)
print(dim_connessa)
print(durata)