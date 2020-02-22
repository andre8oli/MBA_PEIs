def N_13__22(npag, COD):
    P = npag[0]
    P = float(P.replace(',','.'))
    M = npag[1]
    M = float(M.replace(',','.'))
    DH = npag[2]
    DH = float(DH.replace(',','.'))
    FX = npag[3]
    FX = float(FX.replace(',','.'))    
    NI = npag[4]
    NI = float(NI.replace(',','.'))
    
    data = {'AD':[P, M ,DH ,FX, NI],'ANO':5*[COD[0:4]],
                'COD':5*[COD[5:11]]}
    return data

def N_27__35(npag, COD):
    PN = npag[0]
    PN = float(PN.replace(',','.'))
    MN = npag[1]
    MN = float(MN.replace(',','.'))
    DHN = npag[2]
    DHN = float(DHN.replace(',','.'))
    FXN = npag[3]
    FXN = float(FXN.replace(',','.'))    
    NIN = npag[4]
    NIN = float(NIN.replace(',','.'))
    PT = npag[5]
    PT = float(PT.replace(',','.'))
    MT = npag[6]
    MT = float(MT.replace(',','.'))
    DHT = npag[7]
    DHT = float(DHT.replace(',','.'))
    NIT = npag[9]
    NIT = float(NIT.replace(',','.'))
    FXT = npag[8]
    FXT = float(FXT.replace(',','.'))
    
    data = {'IFN':[PN, MN ,DHN ,FXN, NIN],'IM':[PT, MT ,DHT ,FXT, NIT],
                'ANO':5*[COD[0:4]],'COD':5*[COD[5:11]]}
    return data

def Vazio(npag, COD):
    P = ''
    M = ''
    DH = ''
    FX = ''
    NI = ''
    
    data = {'AD':[P, M ,DH ,FX, NI],'ANO':5*[COD[0:4]],
                'COD':5*[COD[5:11]]}
    return data

def Monta_Depois_2013(pdf, COD):
    pag = pdf[2][0]
    pag = pag.splitlines()
    npag = []
    for x in range(0,len(pag)):
        if not (pag[x] == '' or pag[x] == ' '): npag.append(pag[x])
    if (13 <= len(npag) <= 22): data = N_13__22(npag, COD)
    elif (27 <= len(npag) <= 35): data = N_27__35(npag, COD)
    elif not (13 <= len(npag) <= 22 or 
              27 <= len(npag) <= 35): data = Vazio(npag, COD)
    return data