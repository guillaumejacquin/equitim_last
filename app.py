
from flask import Flask
from flask import render_template, url_for, request
import sys
from main import *
from flask_cors import CORS
from flask import jsonify


sys.path.append("../")
from app import *
app = Flask(__name__)
CORS(app)




@app.route("/add", methods=["POST"])
def add_articles():
    Myclass = InformationsForm()

    data = request.json
    Myclass.template = data["template"]
    Myclass.Nom = data["Nom"]
    Myclass.Typologie = data["Typologie"]
    Myclass.Droit = data["Droit"]
    Myclass.Isin = data["Isin"]
    

    #probleme de date, je coupe pour que ca enelever la merde apres 
    emission = data["Emission"]
    Myclass.Emission = emission[0:10]
    tmp = Myclass.Emission

    Myclass.Emission = tmp[6:10] + "-" + tmp[3:5] + "-" + tmp[0:2]

    #2022/02/24
    #24/02/2022
    #8-10.5-7.04

    dci = data["DCI"]
    Myclass.DCI = dci
    Myclass.DCI = Myclass.DCI.replace("/", "-")
    

    dr1 = data["DR1"]
    Myclass.DR1 = dr1[0:10]
    tmp = Myclass.DR1
    Myclass.DR1 = tmp[6:10] + "-" + tmp[3:5] + "-" + tmp[0:2] 

    Myclass.DPR = data["DPR"]
    Myclass.DPR = Myclass.DPR[0:10]
    tmp = Myclass.DPR
    Myclass.DPR = tmp[6:10] + "-" + tmp[3:5] + "-" + tmp[0:2]

    dadr = data["DADR"]
    Myclass.DADR = dadr[0:10]
    tmp = Myclass.DADR
    Myclass.DADR = tmp[6:10] + "-" + tmp[3:5] + "-" + tmp[0:2]

    
    dcf = data["DCF"]
    Myclass.DCF = dcf[0:10]
    tmp = Myclass.DCF
    Myclass.DCF = tmp[6:10] + "-" + tmp[3:5] + "-" + tmp[0:2]

    dec = data["DEC"]
    Myclass.DEC = dec[0:10]
    tmp = Myclass.DEC
    Myclass.DEC = tmp[6:10] + "-" + tmp[3:5] + "-" + tmp[0:2]


    Myclass.ADCF = data["ADCF"]
    Myclass.ADCF = Myclass.ADCF[0:10]
    tmp = Myclass.ADCF
    Myclass.ADCF = tmp[6:10] + "-" + tmp[3:5] + "-" + tmp[0:2]
    Myclass.F0 = data["F0"]
    TSJ = data["TSJ"]
    Myclass.TSJ = list(TSJ.split(", "))


    Myclass.CPN = data["CPN"]
    Myclass.CPN = str(Myclass.CPN).replace(",", ".")

    Myclass.CPN_is_memoire = data["CPN_is_memoire"]
    Myclass.PDI = data["PDI"]
    Myclass.PDI = str(Myclass.PDI).replace(",", ".")

    Myclass.BAC = data["BAC"]
    Myclass.BAC = str(Myclass.BAC).replace(",", ".")

    Myclass.BAC_is_degressif = data["BAC_is_degressif"]
    
    Myclass.BCPN = data["BCPN"]
    Myclass.BCPN = str(Myclass.BCPN).replace(",", ".")

    if (Myclass.BCPN == ""):
        Myclass.BCPN = Myclass.BAC
    Myclass.BCPN_is_degressif = data["BCPN_is_degressif"]

    Myclass.COM = data["COM"]
    Myclass.COM = str(Myclass.COM).replace(",", ".")

    Myclass.NSD = data["NSD"]
    Myclass.NSD = str(Myclass.NSD).replace(",", ".")

    Myclass.NSM = data["NSM"]
    Myclass.NSM = str(Myclass.NSM).replace(",", ".")

    Myclass.NSF = data["NSF"]
    Myclass.NSF = str(Myclass.NSF).replace(",", ".")

    Myclass.ABDAC = data["ABDAC"]
    Myclass.ABDAC = str(Myclass.ABDAC).replace(",", ".")

    Myclass.DBAC = data["DBAC"]
    Myclass.DBAC = str(Myclass.DBAC).replace(",", ".")


    Myclass.DEG = data["DEG"]
    Myclass.DEG = str(Myclass.DEG).replace(",", ".")

    Myclass.type_strike = data["type_strike"]
    Myclass.type_bar = data["type_bar"]

    if (Myclass.type_bar == ""):
        Myclass.type_bar == "degressif"
    
    if (Myclass.type_bar == "degressif"):
        Myclass.BAC_is_degressif = "oui"
    else:
        Myclass.BAC_is_degressif = "non"

    Myclass.sous_jacent = data["sous_jacent"]
    Myclass.NJO = data["NJO"]
    ddp = data["DDP"]

    try:
        if (ddp == ""):
            Myclass.DDP = "error"

        else: 
            tmp = ddp
            Myclass.DDP = tmp[6:10] + "-" + tmp[3:5] + "-" + tmp[0:2]
    except Exception:
        Myclass.DDP = "error"
    Myclass.type_bar2 = data["BCPN_is_degressif"]

    # Myclass.DCF = "2027-07-14"
    try:
        Myclass.JDR = data["jdr"]

    except Exception:
        print("pas de jour de reference")
    print("------------------------------")
    print("Emission = ",  Myclass.Emission)
    print("Premier  constat Rappel = ",  Myclass.DPR)
    print("Premier remboursement Rappel = ",  Myclass.DR1)
    print("avant derniere date constat = ",  Myclass.ADCF)
    print("avant derniere date remboursement = ",  Myclass.DADR)
    print("derniere date constat finale = ",  Myclass.DCF)
    print("date echeance = ",  Myclass.DEC)


    print("------------------------------")
    
    resultmain = main(Myclass)  
    if resultmain == 0:
        return jsonify("True")
    else:
        return jsonify("False")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
