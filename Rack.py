from Node import Node


class Rack:
    def __init__(self, max_antall_noder_per_rack):
        # hver objekt i den klassen har instansvariabel som refererer til en liste med noder
        self._noder = []

    def sett_inn_Node_i_Rack(self, node):
        self._noder.append(node)

    def getAntNoder(self):
        return len(self._noder)

    # returnerer selveste liste av noder i racken, liste som består av objekter som tilhører klasse Node
    def Liste_med_noder(self):
        return self._noder

    def antProssesorer_rack(self):
        total = 0
        for Node in self._noder:
            total += Node.antProsessorer_node()  # samling av antall prosessoser i nodene
        return total

    # for hver node som har minne > paakrevd minne, skal den tas med i tellingen
    def noder_i_rack_Med_Paakrevd_Minne(self, paakrevdMinne):
        teller = 0
        for node in self._noder:
            if node.nokMinne(paakrevdMinne) == True:
                teller += 1
        return teller


#testing underveis av klasse Rack.
"""
R1=Rack()
R2=Rack()

N1=Node(22,2)
N2=Node(6,1)
N3=Node(50,6)

R1.sett_inn_Node_i_Rack(N1)
R1.sett_inn_Node_i_Rack(N2)
R1.sett_inn_Node_i_Rack(N3)
print(R1.getAntNoder())
print()
print(R1.Liste_med_noder())
print(N1)
print(N2)

print(R1.antProssesorer_rack())
print(R1.noder_i_rack_Med_Paakrevd_Minne(20))
"""
