
import HTPerusKirjasto
import sys

def valikko():
    try:
        print("Mitä haluat tehdä:")
        print("1) Lue tiedosto")
        print("2) Analysoi palautukset")
        print("3) Tallenna tulokset")
        print("0) Lopeta")
        valinta = int(input("Valintasi: "))
        return valinta
    except Exception:
        print("Tuntematon valinta.")
        sys.exit(0)

def paaohjelma():
    Lista = []
    Lista2 = []
    ListaVastaukset = []

    while True:
        valinta = valikko()
        
        if valinta == 1:
            Lista = HTPerusKirjasto.LueTiedosto()
        
        elif valinta == 2:
            if len(Lista) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
                print()
                print("Anna uusi valinta.")
                continue
            ListaVastaukset = HTPerusKirjasto.Analysoi(Lista, Lista2, ListaVastaukset)

        elif valinta == 3:
            if len(ListaVastaukset) == 0:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
                print()
                print("Anna uusi valinta.")
                continue
            HTPerusKirjasto.Tallenna(ListaVastaukset, Lista2)
        
        elif valinta == 0:
            print("Kiitos ohjelman käytöstä.")
            break

        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()
            print("Anna uusi valinta.")
    return None

paaohjelma()
