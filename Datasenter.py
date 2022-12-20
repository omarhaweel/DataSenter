from Regneklynge import Regneklynge
from Rack import Rack
from Node import Node


class Datasenter:
    def __init__(self):

        self._regneklynger = {}  # klasse datasenter tar vare paa en ordbok av regneklynger

    def les_inn_fil(self, filnavn):
        fil = open(filnavn)  # aapning av fil
        # innlesing av forste linje, max_noder tar vare paa verdien i den
        max_noder = fil.readline()
        y = fil.readline()  # innlesning av andre linje i filen
        # lage liste av elementer i andre linje, hver element separert fra den andre av (" ")
        biter_smaa_noder = y.strip().split(" ")

        # forste element i den linjen definerer antall smaa noder(de med lite minne)
        Ant_sma_noder = int(biter_smaa_noder[0])
        # andre element definerer minnestoorrelse
        minne_per_smaa_node = int(biter_smaa_noder[1])
        # tredje element definerer antall prossesorer i de smaa nodene
        Ant_pros_per_smaa_node = int(biter_smaa_noder[2])

        z = fil.readline()  # innlesing av neste(tredje linje)
        biter_store_noder = z.strip().split(" ")  # liste av elementer i tredje linje

        Ant_store_noder = int(biter_store_noder[0])  # ant store noder
        # minne stoorrelse per stor node(node med stor minne)
        minne_per_stor_node = int(biter_store_noder[1])
        # antall prossesorer per stor node
        Ant_pros_per_stor_node = int(biter_store_noder[2])

        x = Regneklynge(max_noder)

        Sm_Node = Node(minne_per_smaa_node, Ant_pros_per_smaa_node)
        St_Node = Node(minne_per_stor_node, Ant_pros_per_stor_node)
        R1 = Rack(max_noder)
        R1.sett_inn_Node_i_Rack(Sm_Node)
        # dette gjøres for å sette inn foorste rack (manuelt) som innholder foorste node for aa begynne med
        x.settInnRack(R1)

        # fordi forste node ble satt inn i forste rack som ble satt inn for aa begynne med
        for i in range(Ant_sma_noder-1):
            x.sett_Inn_Node_i_regneklynge(Sm_Node)
        # de settes inn paa samme maate, i samme type rack som de smaa nodene
        for i in range(Ant_store_noder):
            x.sett_Inn_Node_i_regneklynge(St_Node)
        pieces = filnavn.split(".")
        navn = pieces[0]

        self._regneklynger[navn] = x

    def Skriv_Ut(self, filnavn):  # metode for aa skrive ut en spesifikk regneklynge ved aa angi filnavn
        #pieces = filnavn.split(".")
        #navn = pieces[0]
        print("navnet på regneklynge:", filnavn.split(".")[0])
        print("antall prossesorer:", self._regneklynger[filnavn.split(".")
              [0]].ant_Prosessorer_Regneklynge())
        print("anatll racks:",
              self._regneklynger[filnavn.split(".")[0]].antRacks())
        print("noder med minne over 128:",
              self._regneklynger[filnavn.split(".")[0]].noderMedNokMinne(128))
        print("antall noder med minne over 32:",
              self._regneklynger[filnavn.split(".")[0]].noderMedNokMinne(32))
        print("antall noder med minne over 16GB:",
              self._regneklynger[filnavn.split(".")[0]].noderMedNokMinne(16))

        print()

    def Skriv_Ut_alle(self):  # metoden for aa skrive ut alle regneklynger
        print("Info om alle regneklynger i Datasenteret:")
        print()
        for key in self._regneklynger.keys():
            self.Skriv_Ut(key)
