print(
"Tapez [1] Pour : Forme carrée ou rectangulaire\n"
"Tapez [2] Pour : Forme d'un triangle\n"
"Tapez [3] Pour : Forme d'un parallélogramme\n"
)
dnc, dnl, dvc, dvc2, ct, et, esn , es, sorc = "Donner Le number de colonnes : ", "Donner Le number de lignes : ", "Donner La valeur de caractére : ", "Donner Le number de colonnes / 2 : ", "Tapez le numéro de la figure que vous voulez : ", "La valeur ne correspond pas aux données", '', ' ', ''

while (sorc != 's') and (sorc != 'S') :
    
    lc = int(input(ct))
    
    if lc > 0 and lc < 4 :
        
        if lc == 1 :
            
            c = int(input(dnc))
            l = int(input(dnl))
            s = input(dvc)
            for i in range(0,l) :
                r = esn
                for x in range(0,c+1) :
                    if x < c :
                        r += s
                        if x != (c-1) :
                            r += es
                    elif x == c :
                        print(r)

        elif lc == 2 :
            
            print(
            "Tapez [1] Pour : Forme d'un triangle rectangle\n"
            "Tapez [2] Pour : Forme d'un triangle équilatéral\n"
            "Tapez [3] Pour : Forme d'un deux triangles équilatéral (haut-gauche) et (haut-droite)\n"
            "Tapez [4] Pour : Forme d'un losange\n"
            )
            lc = int(input(ct))
            
            if lc > 0 and lc < 5 :
                
                if lc == 1 :
                    
                    print(
                    "Tapez [1] Pour : Forme d'un triangle rectangle (haut-gauche)\n"
                    "Tapez [2] Pour : Forme d'un triangle rectangle (haut-droite)\n"
                    "Tapez [3] Pour : Forme d'un triangle rectangle (bas-gauche)\n"
                    "Tapez [4] Pour : Forme d'un triangle rectangle (bas-droite)\n"
                    )
                    lc = int(input(ct))
                    
                    if lc > 0 and lc < 5 :
                        
                        c = int(input(dnc))
                        s = input(dvc)
                        
                        if lc == 1 :

                            for i in range(0,c) :
                                r = esn
                                for x in range(0,c+1) :
                                    if x < c :
                                        r += s
                                        if x != (c-1) :
                                            r += es
                                    elif x == c :
                                        print(r)
                                c -= 1
                                
                        elif lc == 2 :

                            for i in range(0,c) :
                                r = e = esn
                                for y in range(0,i+1) :
                                    if y < i :
                                        e += es
                                for x in range(0,c+1) :
                                    if x < c :
                                        r += s
                                        if x != (c-1) :
                                            r += es
                                    elif x == c :
                                        print(e*2+r)
                                c -= 1
                                
                        elif lc == 3 :

                            for i in range(1,c+1) :
                                r = esn
                                for x in range(0,i+1) :
                                    if x < i :
                                        r += s
                                        if x != (i-1) :
                                            r += es
                                    elif x == i :
                                        print(r)

                        elif lc == 4 :

                            tr = c
                            for i in range(1,c+1) :
                                r = e = esn
                                tr -= 1
                                for y in range(0,tr) :
                                        e += es
                                for x in range(0,i+1) :
                                    if x < i :
                                        r += s
                                        if x != (i-1) :
                                            r += es
                                    elif x == i :
                                        print(e*2+r)

                    else :
                        print(et)
                    
                elif lc == 2 :

                    c = int(input(dnc))
                    s = input(dvc)
                    tr = c
                    for i in range(1,c+1) :
                        r = e = esn
                        tr -= 1
                        for y in range(0,tr) :
                            e += es
                        for x in range(0,i+1) :
                            if x < i :
                                if x < (i-1) :
                                    r += s + es
                                elif x == (i-1) :
                                    r += s
                            elif x == i :
                                print(e+r)

                elif lc == 3 :

                    c = int(input(dvc2))
                    s = input(dvc)
                    for i in range(0,c) :
                        r = e = esn
                        for y in range(0,i+1) :
                            if y < i :
                                e += es
                        for x in range(0,c+1) :
                            if x < c :
                                r += s
                                if x != (c-1) :
                                    r += es
                            elif x == c :
                                print(r+(e*2)+es+(e*2)+r)
                        c -= 1

                elif lc == 4 :
                        
                        print(
                        "Tapez [1] Pour : Forme d'un losange est vide\n"
                        "Tapez [2] Pour : Forme d'un losange est plein\n"
                        )
                        lc = int(input(ct))

                        if lc > 0 and lc < 3 :
                            
                            if lc == 1 :
                                c = int(input(dvc2))
                                s = input(dvc)
                                esx, esw = es, s
                            
                            elif lc == 2 :
                                c = int(input("Donner Le number de colonnes + 1 / 2 : "))
                                s = input(dvc)
                                esx, esw = s, es

                            q = (c-1)
                                
                            for i in range(0,c) :
                                r = el = er = esn
                                for y in range(0,i+1) :
                                    if y < i :
                                        el += esx + es
                                        er += es + esx
                                for x in range(0,c+1) :
                                    if x < c :
                                        r += esw
                                        if x != (c-1) :
                                            r += es
                                    elif x == c :
                                        print(r+(el)+esx+(er)+r)
                                c -= 1
                                if i == q :
                                    for w in range(2,q+2) :
                                        r = el = er = esn
                                        for y in range(0,q-1) :
                                            el += esx + es
                                            er += es + esx
                                        for x in range(0,w+1) :
                                            if x < w :
                                                r += esw
                                                if x != (w-1) :
                                                    r += es
                                            elif x == w :
                                                print(r+(el)+esx+(er)+r)
                                        q -= 1

                        else :
                            print(et)
                            
            else :
                print(et)
                
        elif lc == 3 :

            c = int(input(dnc))
            l = int(input(dnl))
            s = input(dvc)
            tr = l
            for i in range(0,l) :
                r = e = esn
                tr -= 1
                for y in range(0,tr) :
                        e += es
                for x in range(0,c+1) :
                    if x < c :
                        r += s
                        if x != (c-1) :
                            r += es
                    elif x == c :
                        print(e+r)
                        

    else :
        print(et)
    sorc = input("Appuyez sur n'importe quelle touche pour continuer ou sur 's' pour fermer : ")
