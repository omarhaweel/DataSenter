from Node import Node
from Rack import Rack
from Regneklynge import Regneklynge
from Datasenter import Datasenter


def hovedprogram():

    DS = Datasenter()  # DS variabel som refererer til objekt av klassen Datasenter
    DS.les_inn_fil("abel.txt")  # innlesing
    DS.les_inn_fil("saga.txt")  # innlesing

    print()  # spacing-estetisk maal
    DS.Skriv_Ut("abel.txt")
    print()
    print()
    print()
    DS.Skriv_Ut("saga")
    print()
    DS.Skriv_Ut_alle()


hovedprogram()
