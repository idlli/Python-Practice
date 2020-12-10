def conver_numbres(c,n) :
    if c in 'dD' :
        n = int(n)
        def binaire(n) :
            l = ''
            while n != 0 :
                l += str(n%2)
                n //= 2
            return l[::-1]
        def octal(n) :
            l = ''
            while n != 0 :
                l += str(n%8)
                n //= 8
            return l[::-1]
        def hexa(n) :
            l = ''
            alphab = ['A','B','C','D','E','F']
            num = [10,11,12,13,14,15]
            while n != 0 :
                if n%16 in num :
                    l += str(alphab[num.index(n%16)])
                else :
                    l += str(n%16)
                n //= 16
            return l[::-1]
        return "Binaire = "+str(binaire(n))+" et octal = "+str(octal(n))+", hexadécimal = "+str(hexa(n))
    elif c in 'bB' :
        def décimal(n) :
            l = 0
            i = 0
            length = len(n)
            while length != 0 :
                length -= 1
                l += int(n[i])*2**length
                i += 1
            return l
        return "Décimal = "+str(décimal(n))
    elif c in 'oO' :
        def décimal(n) :
            l = 0
            i = 0
            length = len(n)
            while length != 0 :
                length -= 1
                l += int(n[i])*8**length
                i += 1
            return l
        return "Décimal = "+str(décimal(n))
    elif c in 'hH' :
        def décimal(n) :
            l = 0
            i = 0
            n = n.upper()
            length = len(n)
            alphab = ['A','B','C','D','E','F']
            num = [10,11,12,13,14,15]
            while length != 0 :
                length -= 1
                if n[i] in alphab :
                    l += int(num[alphab.index(n[i])])*16**length
                else :
                    l += int(n[i])*16**length
                i += 1
            return l
        return "Décimal = "+str(décimal(n))
    else :
        return "Erreur dans le choix"
print("-"*80)
print('''
['d' ou 'D'] Pour => Converter Décimal numbre à (binaire,octal,hex)
['b' ou 'B'] Pour => Converter Binaire numbre à Décimal
['o' ou 'O'] Pour => Converter Octal numbre à Décimal
['h' ou 'H'] Pour => Converter Hexadécimal numbre à Décimal
''')
print("-"*80)
le_choix = input('Entrez Votre Choix pour Converter une numbre : ')
numbre = input('Entrez une numbre : ')
print(conver_numbres(le_choix,numbre))
