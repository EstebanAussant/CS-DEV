

def bissextile(annee):
    if annee % 100 != 0 :
        if annee % 4 == 0:
            return True
        else :
            return False
    else :
        return False


def nombrejour(mois,annee):
    longmois = [1,3,5,7,8,10,12]
    courtmois = [4,6,9,11]
    if mois == 2 :
        if bissextile(annee) == True :
            return 29
        else :
            return 28
    elif mois in longmois:
        return 31
    if mois in courtmois:
        return 30
    
def date(jour,mois,annee):
    if mois > 12 :
        return 'date non valide'
    jour_max = nombre_jour(mois, annee)
    if jour <= jour_max :
        return 'date valide'
    else :
        return 'date non valide'
    


print (bissextile(400))
print (bissextile(2024))
print (bissextile(401))
print (nombrejour(2,2024))
print (nombrejour(2,2021))
print (nombrejour(12,2024))
print (nombrejour(4,2024))