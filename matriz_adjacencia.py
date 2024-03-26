class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo =[[0]*self.vertices for i in range(self.vertices)]
    def adiciona_aresta(self, v1, v2):
        self.grafo[v1-1][v2-1] = 1 
        self.grafo[v2-1][v1-1] = 1
    def matriz(self):
        print('Matriz de adjacências: ')
        for i in range(self.vertices):
            print(self.grafo[i])

"""1 Acre 2 Alagoas 3 Amapá 4 Amazonas 5 Bahia 6 Ceará 7 Espírito Santo 8  Goiás 9  Maranhão
 10  Mato Grosso 11  Mato Grosso do Sul 12  Minas Gerais 13 Pará 14  Paraíba 15  Paraná 
 16 Pernambuco 17  Piauí 18  Rio de Janeiro 19  Rio Grande do Norte
 20  Rio Grande do Sul 21  Rondônia 22  Roraima 23  Santa Catarina 24  São Paulo 25  Sergipe 26
Tocantins 27  Distrito Federal"""
g = Grafo(27)
g.adiciona_aresta(1,4)
g.adiciona_aresta(2,16)
g.adiciona_aresta(2,25)
g.adiciona_aresta(2,5)
g.adiciona_aresta(3,13)
g.adiciona_aresta(4,22)
g.adiciona_aresta(4,21)
g.adiciona_aresta(4,10)
g.adiciona_aresta(4,13)
g.adiciona_aresta(5,17)
g.adiciona_aresta(5,16)
g.adiciona_aresta(5,25)
g.adiciona_aresta(5,12)
g.adiciona_aresta(5,7)
g.adiciona_aresta(6,17)
g.adiciona_aresta(6,16)
g.adiciona_aresta(6,19)
g.adiciona_aresta(6,14)
g.adiciona_aresta(27,8)
g.adiciona_aresta(27,12)
g.adiciona_aresta(7,12)
g.adiciona_aresta(7,18)
g.adiciona_aresta(8,26)
g.adiciona_aresta(8,10)
g.adiciona_aresta(8,11)
g.adiciona_aresta(8,12)
g.adiciona_aresta(9,13)
g.adiciona_aresta(9,26)
g.adiciona_aresta(9,17)
g.adiciona_aresta(10,21)
g.adiciona_aresta(10,26)
g.adiciona_aresta(10,11)
g.adiciona_aresta(11,12)
g.adiciona_aresta(11,24)
g.adiciona_aresta(11,15)
g.adiciona_aresta(12,18)
g.adiciona_aresta(12,24)
g.adiciona_aresta(13,22)
g.adiciona_aresta(13,26)
g.adiciona_aresta(14,16)
g.adiciona_aresta(14,19)
g.adiciona_aresta(15,23)
g.adiciona_aresta(15,24)
g.adiciona_aresta(16,17)
g.adiciona_aresta(17,26)
g.adiciona_aresta(18,24)
g.adiciona_aresta(20,23)

g.matriz()
     