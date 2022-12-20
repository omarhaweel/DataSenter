from Node import Node
from Rack import Rack


class Regneklynge:
    def __init__(self, Max_noder_per_rack):
        self._Max_noder_per_rack = Max_noder_per_rack
        self._Racks = []

	## Plasserer en node inn i et rack med ledig plass, eller i et nytt
	# @param node referanse til noden som skal settes inn i datastrukturen

    def sett_Inn_Node_i_regneklynge(self, node):
        for rack in self._Racks:
            if rack.getAntNoder() < int(self._Max_noder_per_rack):
                # sette inn node i rack hvis det er plass
                rack.sett_inn_Node_i_Rack(node)
                return self._Racks
                break  # her for å sikre at loopen kjøres kun en gang for å hindre å sette samme node i flere racks hvor det er plass
        for rack in self._Racks:
            if rack.getAntNoder() >= int(self._Max_noder_per_rack):
                ny = Rack(self._Max_noder_per_rack)  # oppretting av en ny rack
                self._Racks.append(ny)  # sette inn racken i liste av racks
                ny._noder.append(node)  # sette inn noden i den nye Racken
                break  # for aa lage kun en rack

    def settInnRack(self, rack):
        self._Racks.append(rack)

	## Beregner totalt antall prosessorer i hele regneklyngen
	# @return totalt antall prosessorer

    def ant_Prosessorer_Regneklynge(self):
        collect = 0  # samling av antall prossesorer i hele Regneklyngen
        for rack in self._Racks:

            collect += rack.antProssesorer_rack()
        return collect

	## Beregner antall noder i regneklyngen med minne over angitt grense
	# @param paakrevdMinne hvor mye minne skal noder som telles med ha
	# @return antall noder med tilstrekkelig minne

    def noderMedNokMinne(self, paakrevdMinne):
        self._noder_i_regneklynge_med_tilstrekkelig_minne = 0

        for rack in self._Racks:
            self._noder_i_regneklynge_med_tilstrekkelig_minne += rack.noder_i_rack_Med_Paakrevd_Minne(
                paakrevdMinne)
        return(self._noder_i_regneklynge_med_tilstrekkelig_minne)

	## Henter antall racks i regneklyngen
	# @return antall racks

    def antRacks(self):  # antall racks ved å returnere lengden på liste av racks som hører til objektet i klassen regneklynge
        return len(self._Racks)
