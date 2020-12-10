#Partie_Pratique
#Exercice 1
'''S = [1,2]
def niéme(n) :
    while len(S) < n :
        S.append(S[len(S)-1]*S[len(S)-2])
        print('S[',len(S),'] = ',S[-1])
    return S[-1]
def affresult(n) :
    if n > 2 :
        niéme(n)
    else :
        print('Votre n <= 2')
n = int(input('Entrez la valeur de n : '))
affresult(n)'''
#Problème
Salle_Liste = []
def CreerSalle(idSalle,libelleSalle,Capacite) :
    return {'identificateur':idSalle,'lebellé':libelleSalle,'champ capacité':Capacite}
def SaisirInfosSalle(Salle_Liste,n) :
    for i in range(n) :
        idSalle = int(input('Entrez identificateur de salle : '))
        libelleSalle = input('Entrez lebellé de salle : ')
        Capacite = int(input('Entrez capacité de salle : '))
        Salle_Liste.append(CreerSalle(idSalle,libelleSalle,Capacite))
def AfficherSalle(i) :
    return 'Id Salle : {} Libellé Salle : {} Capacité Salle : {}'.format(i['identificateur'],i['lebellé'],i['champ capacité'])
def AfficherInfosSalles(Salle_Liste) :
    for i in Salle_Liste :
        print(AfficherSalle(i))
def RechercherSalle(idsa,Salle_Liste) :
    for i in Salle_Liste :
        if i['identificateur'] == idsa :
            return Salle_Liste.index(i)
    return 0
def SupprimerSalle(idsa,Salle_Liste) :
    r = RechercherSalle(idsa,Salle_Liste)
    if r :
        del Salle_Liste[r]
    else :
        print('la salle n\'existe pas')
def TrierSallesParLibelle(Salle_Liste) :
    new_Salle_Liste = []
    for i in range(len(Salle_Liste)) :
        new_Salle_Liste.append(Salle_Liste[i]['lebellé']+'-'+str(i))
    new_Salle_Liste.sort()
    Salle_Liste_Sorted_By_lebellé = []
    for i in new_Salle_Liste :
        Salle_Liste_Sorted_By_lebellé.append(Salle_Liste[int(i[i.index('-')+1:])])
    Salle_Liste = Salle_Liste_Sorted_By_lebellé
    AfficherInfosSalles(Salle_Liste)
def Sauvegarder() :
    file=open(':\\Salles.txt','w')
    for i in Salle_Liste :
        file.write(AfficherSalle())
    file.close()
def pour_test() :
    print('''
1- Pour SaisirInfosSalle()
2- Pour AfficherInfosSalles()
3- Pour SupprimerSalle()
4- Pour TrierSallesParLibelle()
5- Pour Sauvegarder()
''')
    le_choix = 1
    while le_choix :
        le_choix = int(input('Entrez votre choix : '))
        if le_choix == 1 :
            n = int(input('Entrez number des sales pour insérer : '))
            SaisirInfosSalle(Salle_Liste,n)
        elif le_choix == 2 :
            AfficherInfosSalles(Salle_Liste)
        elif le_choix == 3 :
            idsa = int(input('Entrez id de salle : '))
            SupprimerSalle(idsa,Salle_Liste)
        elif le_choix == 4 :
            TrierSallesParLibelle(Salle_Liste)
        elif le_choix == 5 :
            Sauvegarder()
        else :
            break
pour_test()
