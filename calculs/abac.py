def abac(Class):
    if (Class.BAC_is_degressif == "oui"):
        Class.ABAC = "la barrière dégressive de remboursement anticipé automatique \u00281\u0029"
    else:
        mystring = str(Class.BAC) + "% de son <NDR>"
        Class.ABAC = mystring

def abac2(Class):
    if Class.type_bar2 == "degressif" and Class.BCPN_is_degressif == "oui":
        Class.ABAC2 = "la barrière dégressive de versement du coupon"

    else:
        Class.ABAC2 = "<BCPN> de son <NDR>"