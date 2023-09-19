def mes_impot(revenu):
    p1=10225 ; p2=26070 ; p3=74545 ; p4=160336
    impot = 0
    tranche2 = (p2-p1)*(11/100)
    tranche3 = (p3-p2)*(30/100)
    tranche4 = (p4-p3)*(41/100)
    if revenu <= p1 :
        return 0
    if revenu > p4 :
        impot = (revenu-p4)*(45/100) + tranche2 + tranche3 + tranche4
    elif revenu <= p4 and revenu > p3 :
        impot = (revenu-p3)*(41/100) + tranche2 + tranche3
    if revenu <= p3 and revenu > p2 :
        impot = (revenu-p2)*(30/100) + tranche2
    elif revenu <= p2 and revenu > p1 :
        impot = (revenu-p1)*(11/100)
    return impot

print (mes_impot(50000))