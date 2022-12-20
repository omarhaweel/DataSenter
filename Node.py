class Node:
    def __init__(self, minne, ant_pros_Node):  # to instansvariabler
        self._minne = minne
        self._ant_pros_Node = ant_pros_Node

    def antProsessorer_node(self):  # returnere instansvariabel : ant_pros_Node
        return self._ant_pros_Node

    def nokMinne(self, paakrevdMinne):  # sjekker om minnestørrelse er større enn paakrev minne
        if self._minne >= paakrevdMinne:
            return True


#Testing underveis av klasse Node, ikke kjørbar
"""
N1=Node(22,2)
N2=Node(6,1)
print(N1.antProsessorer_node())
print(N2.antProsessorer_node())
print(N1.nokMinne(20))
print(N2.nokMinne(12))
print(N1._minne)
"""
