from model.model import Model

mymodel = Model()
mymodel.buildGraph(60*60*1000)
print(mymodel.getGraphDeails())