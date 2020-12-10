def trouveEtud_CODE(Code) :
    for i in Te :
        if i['Code'].lower() == Code.lower() :
            return Te.index(i)
        else :
            return -1
def AjoutEtud() :
    rep = 'y'
    while rep.lower() == 'y' or rep.lower() == 'yes' :
        print('-'*80)
        Code = input('Entrez votre code : ')
        if trouveEtud_CODE(Code) == -1 or trouveEtud_CODE(Code) == None :
            Nom = input('Entrez votre nom : ')
            Age = int(input('Entrez votre age : '))
            Note = float(input('Entrez votre note : '))
            Te.append({'Code' : Code, 'Nom' : Nom, 'Age' : Age, 'Note' : Note})
        else :
            print('Votre code déja exist')
        rep = input('Entrez \'y\' pour continu ou quelque autre pour quitter : ')
def AfficheEtud() :
    y = 0
    for i in range(len(Te)) :
        y += 1
        print('Etudiant ['+str(i+1)+']')
        print('\tCode : '+Te[i]['Code'])
        print('\tNom : '+Te[i]['Nom'])
        print('\tAge : '+str(Te[i]['Age']))
        print('\tNote : '+str(Te[i]['Note']))
    if y == 0 :
        print(str(y)+' Etudiant trouvé')
def SupprimerEtud() :
    Sup_Code = input('Entrez etudiant code : ')
    y = 0
    for i in Te :
        if i['Code'].lower() == Sup_Code.lower() :
            Sup_Conf = input('Entrez y pour confirmer l\'action : ')
            if Sup_Conf.lower() == 'y' or Sup_Conf.lower() == 'yes' :
                y += 1
                Te.remove(i)
                return Affichemenu()
    if y == 0 :
        print('Votre code pas exist ou ( pas confirmer l\'action )')
def AfficheEtud_Sup_AGE() :
    Sup_AGE = int(input('Entrez la valeur d\'age : '))
    y = 0
    for i in range(len(Te)) :
        if Te[i]['Age'] >= Sup_AGE :
            y += 1
            print('Etudiant ['+str(y)+']')
            print('\tCode :'+Te[i]['Code'])
            print('\tNom :'+Te[i]['Nom'])
            print('\tAge :'+str(Te[i]['Age']))
            print('\tNote :'+str(Te[i]['Note']))
    if y == 0 :
        print(str(y)+'Etudiant trouvé')
def RechercheEtud_NOM() :
    R_NOM = input('Entrez votre nom : ')
    y = 0
    for i in range(len(Te)) :
        if Te[i]['Nom'].lower() == R_NOM.lower() :
            y += 1
            print('Etudiant ['+str(y)+']')
            print('\tCode :'+Te[i]['Code'])
            print('\tNom :'+Te[i]['Nom'])
            print('\tAge :'+str(Te[i]['Age']))
            print('\tNote :'+str(Te[i]['Note']))
    if y == 0 :
        print(str(y)+'Etudiant trouvé')
def RechercheEtud_CODE() :
    R_CODE = input('Entrez votre code : ')
    y = 0
    for i in range(len(Te)) :
        if Te[i]['Code'].lower() == R_CODE.lower() :
            y += 1
            print('Etudiant ['+str(y)+']')
            print('\tCode :'+Te[i]['Code'])
            print('\tNom :'+Te[i]['Nom'])
            print('\tAge :'+str(Te[i]['Age']))
            print('\tNote :'+str(Te[i]['Note']))
    if y == 0 :
        print(str(y)+'Etudiant trouvé')
def RechercheEtud_AGE() :
    R_AGE = int(input('Entrez votre age : '))
    y = 0
    for i in range(len(Te)) :
        if Te[i]['Age'] == R_AGE :
            y += 1
            print('Etudiant ['+str(y)+']')
            print('\tCode :'+Te[i]['Code'])
            print('\tNom :'+Te[i]['Nom'])
            print('\tAge :'+str(Te[i]['Age']))
            print('\tNote :'+str(Te[i]['Note']))
    if y == 0 :
        print(str(y)+'Etudiant trouvé')
def TriEtud_NOM() :
    def t_nom(t_nom) :
        return t_nom.get('Nom')
    C_Te = Te.copy()
    C_Te.sort(key=t_nom)
    y = 0
    for i in range(len(C_Te)) :
        y += 1
        print('Etudiant ['+str(y)+']')
        print('\tCode :'+C_Te[i]['Code'])
        print('\tNom :'+C_Te[i]['Nom'])
        print('\tAge :'+str(C_Te[i]['Age']))
        print('\tNote :'+str(C_Te[i]['Note']))
    if y == 0 :
        print(str(y)+'Etudiant trouvé')
def TriEtud_AGE() :
    def t_age(t_age) :
        return t_age.get('Age')
    C_Te = Te.copy()
    C_Te.sort(key=t_age)
    y = 0
    for i in range(len(C_Te)) :
        y += 1
        print('Etudiant ['+str(y)+']')
        print('\tCode : '+C_Te[i]['Code'])
        print('\tNom : '+C_Te[i]['Nom'])
        print('\tAge : '+str(C_Te[i]['Age']))
        print('\tNote : '+str(C_Te[i]['Note']))
    if y == 0 :
        print(str(y)+' Etudiant trouvé')
def Affichemenu() :
    le_choix = -1
    while le_choix != 0 :
        print('''
--------MENU------------------------------------
1 : [ Ajouter Etudiant ]
2 : [ Supprimer Etiduant ]
3 : [ Afficher Etudiant ]
4 : [ Afficher les Etudiant SUPERIEUR A UN AGE ]
5 : [ Recherche Etudiant par nom ]
6 : [ Recherche Etudiant par code ]
7 : [ Recherche Etudiant par age ]
8 : [ Trier Etudiant par nom ]
9 : [ Trier Etudiant par age ]
12 : [ Exit ]
''')
        le_choix = int(input('Entrez votre choix : '))
        if le_choix == 1 : AjoutEtud()
        elif le_choix == 2 : SupprimerEtud()
        elif le_choix == 3 : AfficheEtud()
        elif le_choix == 4 : AfficheEtud_Sup_AGE()
        elif le_choix == 5 : RechercheEtud_NOM()
        elif le_choix == 6 : RechercheEtud_CODE()
        elif le_choix == 7 : RechercheEtud_AGE()
        elif le_choix == 8 : TriEtud_NOM()
        elif le_choix == 9 : TriEtud_AGE()
        elif le_choix == 12 : break
        else :
            print('Erreur ( vérifier votre choix )')
Te = []
Affichemenu()
