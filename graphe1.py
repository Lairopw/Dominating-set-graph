from ast import operator
from os import TMP_MAX
from pickle import FALSE
from random import randint, randrange
import random
import operator
from sqlite3 import adapt

dic={}
def graph_ini(som,arr,o:bool):
    #création des sommets du graph
    print("##########################")
    print("#  Création des sommets  #")
    print("##########################")
    for i in range(som):
        dic[str(i)]=[]
    test=0
    #implémentation arréte
    print("##########################")
    print("#  Création des arrêtes  #")
    print("##########################")
    while test!=arr:
        a=randint(0,som-1)
        tmp=randint(0,som-1)
        #vérification si le sommets d'arriver et le même que le sommet d'orgine 
        if(tmp!=a):
            #vérification si le sommet d'arriver est déjà présent
            if(tmp not in dic[str(a)]):
                #vérification si le graphe est orienté ou non
                if o:
                    #on ajoute une arrete aléatoire à un sommet aléatoire 
                    dic[str(a)].append(tmp)
                    test+=1
                else:
                    #on ajoute une arrete aléatoire à un sommet aléatoire et on le rajoute à l'autre sommet 
                    dic[str(a)].append(tmp)
                    dic[str(tmp)].append(a)
                    test+=2
    return(dic)

garp=graph_ini(1000,15000,False)

def dom(grap):
    d=0
    l=[]
    m=[]
    print("#####################")
    print("#  domminating set  #")
    print("#####################")
    for e in grap:
        a=len(grap[str(e)])
        #vérification du sommet avec le maximum d'arrêtes 
        if a>d:
            d=a
            #parcours du dictionnaire 
            for i in grap.keys():
                #vérification si des doublon existe 
                if e not in l or m or grap:
                    #recuperation de l'index du sommet avec le maximum d'arrêtes
                    if len(grap[i])==d:
                        #ajout dans la liste de résultat final 
                        l.append(i)
                        #ajout dans la liste des sommets marqués 
                        m.append(grap[i])
    print("##########")
    print("#  FINI  #")
    print("##########")
    return l
dom(garp)

s = "\nDOMINATING SET : \n" + str(dom(garp)) + "\n##################################################################################################################################################################################################################\n" +"GRAPHE : \n" + str(garp)
with open("./pipapou.txt", "w") as fichier:
    fichier.write(s)
fichier.close()