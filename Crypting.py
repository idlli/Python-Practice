def lire(c) :
    if c.find(' ') != -1 and c[-1] == '.' :
        return 'Crypter Phrase = ' + crypter_phrase(c)
    else :
        return 'Crypter Mot = ' + crypter_mot(c)
def crypter_mot(c) :
    new_s = ''
    for car in c :
        get_car = alphab.find(car)
        if get_car != -1 :
            new_s += alphab[-(len(alphab)-get_car)+4]
        else :
            new_s += car
    return new_s
def crypter_phrase(c) :
    new_s = ''
    for car in c :
        get_car = alphab.find(car)
        if get_car != -1 :
            new_s += alphab[-(len(alphab)-get_car)+4]
        else :
            new_s += car
    return new_s
alphab = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
c = input('Entrez un chaine de caractère : ')
print(lire(c))
