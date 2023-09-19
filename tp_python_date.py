

def bissextile(annee):
    if annee % 100 != 0 :
        if annee % 4 == 0:
            return True
        else :
            return False
    else :
        return False


def nombre_jour(mois,annee):
    long_mois = [1,3,5,7,8,10,12]
    court_mois = [4,6,9,11]
    if mois == 2 :
        if bissextile(annee) :
            return 29
        else :
            return 28
    elif mois in long_mois:
        return 31
    if mois in court_mois:
        return 30
    
def date(jour,mois,annee):
    if mois > 12 :
        return 'date non valide'
    jour_max = nombre_jour(mois, annee)
    if jour <= jour_max :
        return 'date valide'
    else :
        return 'date non valide'
    


print (date(29,2,2024))
print (date(29,2,2021))
print (date(28,2,2021))
print (date(24,12,2023))
print (date(55,2,2024))