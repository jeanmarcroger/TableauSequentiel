import numpy as np
import pandas as pd
import copy
# declaration variable NbreListe NbreElement
NbreListe_D = 8
NbreElement_D = 6
List_Commpteur_Chaque_Nbre = []
List_Compteur_Chaque_Element_DE_Liste = []
List_Commpteur_Chaque_Nbre = NbreElement_D*[0] #Donnera Qteme Liste
List_Compteur_Chaque_Element_DE_Liste = NbreListe_D*[0] #Donnera Qtieme Element
print("List_Commpteur_Chaque_Nbre",List_Commpteur_Chaque_Nbre)
print("List_Compteur_Chaque_Element_DE_Liste",List_Compteur_Chaque_Element_DE_Liste)


#Creation Tableau vide du début.
def CreationTableauVide(NbreListe,NbreElement):
    global TableauVide
    TableauVide = []
    TableauVide = NbreListe*[0]
    for NbrLignea in range(len(TableauVide)):
        TableauVide[NbrLignea]=NbreElement*[0]

#Creation Tableau vide de fin.
def CreationTableauVide_F(NbreListe,NbreElement):
    global TableauVide_F
    TableauVide_F = []
    TableauVide_F = NbreElement*[0]
    for NbrLignea in range(len(TableauVide_F)):
        TableauVide_F[NbrLignea]=NbreListe*[0]

#Creation tableau liste vide.
def CreationTableauListeVide(NbreListe):
    NbreListe2 = NbreListe + 1
    global TableauListeVide
    TableauListeVide = []
    for NbrLignea in range(1,NbreListe2):
        TableauListeVide.append([])

#Creation tableau liste vide_0.
def CreationTableauListeVide_0(NbreListe):
    NbreListe2 = NbreListe + 1
    global TableauListeVide_0
    TableauListeVide_0 = []
    for NbrLignea in range(1,NbreListe2):
        TableauListeVide_0.append([0])

#Creation list contenant 0.
def CreationListeAvec0(NbreListe):
    global ListeAvec0
    ListeAvec0 = []
    ListeAvec0 = NbreListe*[0]
    print("ListeAvec0",ListeAvec0)

#Creation tableau liste vide_0 F.
def CreationTableauListeVide_0_F(NbreElement):
    NbreElement2 = NbreElement + 1
    global TableauListeVide_0_F
    TableauListeVide_0_F = []
    for NbrLignea in range(1,NbreElement2):
        TableauListeVide_0_F.append([0])

#Creation liste enumeration inversée.
def CreationListeEnumerationIversee(NbreElement):
    NbreElement2 = NbreElement + 1
    global ListeEnumerationIversee
    ListeEnumerationIversee = []
    for NbrLignea in range(0,NbreElement):
        ListeEnumerationIversee.append(NbrLignea)
    ListeEnumerationIversee.reverse()

# Création tableau référence.
CreationTableauVide(NbreListe_D,NbreElement_D)
CreationTableauListeVide(NbreListe_D)
CreationTableauListeVide_0(NbreListe_D)
CreationListeAvec0(NbreListe_D)
CreationTableauVide_F(NbreListe_D,NbreElement_D)
CreationListeEnumerationIversee(NbreElement_D)
CreationTableauListeVide_0_F(NbreElement_D)

# Creation des autres tableaux.
TableauEnumeration = copy.deepcopy(TableauVide) # TableauEnumeration de début.
TableauPerma =  copy.deepcopy(TableauVide)  # TableauPerma de début.
TableauDifferent = copy.deepcopy(TableauListeVide)
TableauCptDifferent = copy.deepcopy(TableauListeVide_0)
ListeCptDifferent = copy.deepcopy(ListeAvec0)
TableauEnumeration_F = copy.deepcopy(TableauVide_F) # TableauEnumeration de début.
TableauPerma_F =  copy.deepcopy(TableauVide_F)  # TableauPerma de début.
TableauCptDifferent_F = copy.deepcopy(TableauListeVide_0_F)

#Ajout de ListeCptDifferent a TableauPerma_F dans TableauPerma_F2.
TableauPerma_F2 = []
TableauPerma_F2.append(ListeCptDifferent)
for element in TableauPerma_F:
    TableauPerma_F2.append(element)



print("TableauEnumeration",TableauEnumeration)
print("TableauPerma",TableauPerma)
print("TableauDifferent",TableauDifferent)
print("ListeEnumerationIversee",ListeEnumerationIversee)
print("TableauCptDifferent",TableauCptDifferent)
print("TableauEnumeration_F",TableauEnumeration)
print("TableauPerma_F",TableauPerma_F)


# Liste pour introduire permanence.
ListeQtieme_P = []
ListeEntrePerma = []

# Tableau initial commence par liste
TableauInitial_P = []
TableauInitial_E = []




for Qtieme_P in range(1,40):
    EntreePerma = int(input('Numero ? '))
    D_EntreePerma = EntreePerma - 1

    # Conserver permanence dans liste
    ListeEntrePerma.append(EntreePerma)
    ListeQtieme_P.append(Qtieme_P)

    # Contient valeur indispensable au premier tour de boucle soit 0 par défault, et après ancienne valeur.
    Rpr_Rslt_L = List_Commpteur_Chaque_Nbre[D_EntreePerma]
    Rpr_Rslt_E = List_Compteur_Chaque_Element_DE_Liste[Rpr_Rslt_L]

    # Placement au bon endroit.
    # Tableau début.
    TableauEnumeration[Rpr_Rslt_L][Rpr_Rslt_E] = Qtieme_P
    TableauPerma[Rpr_Rslt_L][Rpr_Rslt_E] = EntreePerma

    # Different des colonnes tableaux debut.
    TableauDifferent[Rpr_Rslt_L].append(EntreePerma) #Ajoute dans la liste en cours.
    print("TableauCptDifferent[Rpr_Rslt_L]",TableauCptDifferent[Rpr_Rslt_L])
    TableauCptDifferent[Rpr_Rslt_L][0] = TableauCptDifferent[Rpr_Rslt_L][0] + 1 #Compte les éléments mis dans des listes
    ListeCptDifferent[Rpr_Rslt_L] = ListeCptDifferent[Rpr_Rslt_L] + 1 #Compte les éléments mis dans une liste
    print("Rpr_Rslt_L",Rpr_Rslt_L)
    print("TableauCptDifferent",TableauCptDifferent,"ListeCptDifferent",ListeCptDifferent)
    if Rpr_Rslt_L >0:
        DecaleArriere = Rpr_Rslt_L - 1
        TableauDifferent[DecaleArriere].remove(EntreePerma) #Enlève liste précédente.
        print("TableauCptDifferent[DecaleArriere][0]",TableauCptDifferent[DecaleArriere][0])
        TableauCptDifferent[DecaleArriere][0] = TableauCptDifferent[DecaleArriere][0] - 1 #Compte les éléments
        ListeCptDifferent[DecaleArriere] = ListeCptDifferent[DecaleArriere] - 1 #Compte les éléments mis dans une liste
    TableauDifferent[Rpr_Rslt_L].sort()

    # Placement au bon endroit.
    # Tableau Fin.
    #Lgne = ListeEnumerationIversee[Rpr_Rslt_E] #Pour commencer en bas du tableau.
    Lgne = Rpr_Rslt_E
    Clne = Rpr_Rslt_L
    TableauEnumeration_F[Lgne][Clne] = Qtieme_P
    TableauPerma_F[Lgne][Clne] = EntreePerma

    # CPT Different des colonnes tableaux fin.
    TableauCptDifferent_F[Lgne][0] = TableauCptDifferent_F[Lgne][0] + 1
    if Lgne > 0:
        DecaleArriere_L = Lgne - 1
        TableauCptDifferent_F[DecaleArriere_L][0] = TableauCptDifferent_F[DecaleArriere_L][0] - 1

    # Compteur.
    List_Commpteur_Chaque_Nbre[D_EntreePerma] = List_Commpteur_Chaque_Nbre[D_EntreePerma] + 1
    List_Compteur_Chaque_Element_DE_Liste[Rpr_Rslt_L] = List_Compteur_Chaque_Element_DE_Liste[Rpr_Rslt_L] + 1

    # Prend valeur pour tour suivant, car devait commencer a 0 premier tour de boucle.
    Rpr_Rslt_L = List_Commpteur_Chaque_Nbre[D_EntreePerma]
    Rpr_Rslt_E = List_Compteur_Chaque_Element_DE_Liste[Rpr_Rslt_L]

    # Affichage tableau.

    print("TableauPerma",TableauPerma)
    print("TableauDifferent",TableauDifferent)
    print("ListeCptDifferent",ListeCptDifferent)

    print("TableauCptDifferent",TableauCptDifferent)
    print("TableauPerma_F",TableauPerma_F)
    print("TableauPerma_F2",TableauPerma_F2)
    TblP = np.array(TableauPerma_F)
    TableauPerma_N = pd.DataFrame(TblP, index = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6'], columns = ['A', 'B', 'C', 'D','E','F','G', 'H'])
    CptDCln = np.array([ListeCptDifferent])
    ListeCptDifferent_N = pd.DataFrame(CptDCln, index = ['CT'], columns = ['A', 'B', 'C', 'D','E','F','G', 'H'])

    #print(ListeCptDifferent_N)
    #print(CptDCln)
    #print(TableauPerma_N)


