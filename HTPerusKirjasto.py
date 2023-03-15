

import sys

class PALAUTUS:
    aika = ""
    opiskelija = ""
    tehtava = ""

class TEHTAVA:
    nimi = ""
    maara = 0

class TULOS:
    keskiarvo = 0
    Plkm = 0
    Tlkm = 0
    Ppienin = 0
    Psuurin = 0
    Npienin = ""
    Nsuurin = ""

def LueTiedosto():
    Lista = []
    Lista.clear()
    try:
        nimi = input("Anna luettavan tiedoston nimi: ")
        tdsto = open(nimi, "r", encoding="utf-8")
        rivi = tdsto.readline()[:-1]

        while True:
            rivi = tdsto.readline()[:-1]
            if len(rivi) == 0:
                break
            else:
                olio = PALAUTUS()
                rivi = rivi.split(";")
                olio.aika = rivi[0]
                olio.opiskelija = rivi[1]
                olio.tehtava = rivi[2]
                Lista.append(olio)
        tdsto.close()
        print("Tiedostosta '", nimi, "' luettiin listaan ", len(Lista)," datarivin tiedot.", sep="")
        print()
        print("Anna uusi valinta.")
        
    except Exception:
        print("Tiedoston '", nimi, "' käsittelyssä virhe, lopetetaan.", sep="")
        sys.exit(0)
    
    return Lista

def Analysoi(Lista, Lista2, ListaVastaukset):
    Tehtava_lista = []
    lkm = 0
    Tehtava_lista.clear()
    Lista2.clear()
    for i in Lista:
        Tehtava_lista.append(i.tehtava)
    Tehtava_lista.sort()
    edellinen = Tehtava_lista[0]

    for i in Tehtava_lista:
        if i == edellinen:
            lkm = lkm + 1
        else:
            data = TEHTAVA()
            data.maara = lkm
            data.nimi = edellinen
            Lista2.append(data)
            edellinen = i
            lkm = 1
    data = TEHTAVA()
    data.maara = lkm
    data.nimi = edellinen
    Lista2.append(data)

    PalautusYht = 0
    TehtYht = 0
    PalautusKeskiarvo = 0
    PalautusMax = Lista2[0].maara
    PalautusMin = Lista2[0].maara
    TehtMax = ""
    TehtMin = ""
    for i in Lista2:
        PalautusYht += i.maara
        TehtMaara = len(Lista2)
        PalautusKeskiarvo = PalautusYht/TehtMaara
        PalautusKeskiarvo = int(PalautusKeskiarvo)

    for i in Lista2:
        if PalautusMax < i.maara:
            PalautusMax = i.maara
            TehtMax = i.nimi
        
    for i in Lista2:
        if PalautusMin > i.maara:
            PalautusMin = i.maara
            TehtMin = i.nimi

    olio = TULOS()
    olio.keskiarvo = PalautusKeskiarvo
    olio.Npienin = TehtMin
    olio.Nsuurin = TehtMax
    olio.Plkm = PalautusYht
    olio.Tlkm = TehtMaara
    olio.Psuurin = PalautusMax
    olio.Ppienin = PalautusMin
    ListaVastaukset.append(olio)

    print("Analysoitu ", len(Lista), " palautusta ", len(Lista2), " eri tehtävään.", sep="")
    print("Tilastotiedot analysoitu.")
    print()
    print("Anna uusi valinta.")
    return ListaVastaukset

def Tallenna(ListaVastaukset, Lista2):

    try:
        nimi = input("Anna kirjoitettavan tiedoston nimi: ")
        tdsto = open(nimi, "w", encoding="utf-8")
        for olio in ListaVastaukset:

            print("Palautuksia tuli yhteensä ", olio.Plkm, ", ", olio.Tlkm, " eri tehtävään.", sep="")
            print("Viikkotehtäviin tuli keskimäärin ", olio.keskiarvo, " palautusta.", sep="")
            print("Eniten palautuksia, ", olio.Psuurin, ", tuli viikkotehtävään ", olio.Nsuurin, ".", sep="")
            print("Vähiten palautuksia, ", olio.Ppienin, ", tuli viikkotehtävään ", olio.Npienin , ".", sep="")
            print()
            print("Tehtävä;Lukumäärä")
        for i in Lista2:
            print(i.nimi, ";", i.maara, sep="")
        
        for olio in ListaVastaukset:
            tdsto.write("Palautuksia tuli yhteensä " + str(olio.Plkm) + ", "  + str(olio.Tlkm) + " eri tehtävään." + "\n")
            tdsto.write("Viikkotehtäviin tuli keskimäärin " + str(olio.keskiarvo) + " palautusta." + "\n")
            tdsto.write("Eniten palautuksia, " + str(olio.Psuurin) + ", tuli viikkotehtävään " + str(olio.Nsuurin) + "." + "\n")
            tdsto.write("Vähiten palautuksia, " + str(olio.Ppienin) + ", tuli viikkotehtävään " + str(olio.Npienin) + "." + "\n\n")
            tdsto.write("Tehtävä;Lukumäärä" + "\n")
        for i in Lista2:
            tdsto.write(str(i.nimi) + ";" + str(i.maara) + "\n")
        print("Tulokset tallennettu tiedostoon '", nimi, "'.", sep="")
        print()
        print("Anna uusi valinta.")

    except Exception:
        print("Tiedoston '", nimi, "' käsitelyssä virhe, lopetetaan.", sep="")
        sys.exit(0)
    tdsto.close()
    return None

        
