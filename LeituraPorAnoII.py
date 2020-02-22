def N_20_22(npag, COD):
    P = float(npag[0])
    M = float(npag[1])
    DH = float(npag[2])
    FX = float(npag[3])
    NI = float(npag[4])
    
    data = {'AD':[P, M ,DH ,FX, NI],'ANO':5*[COD[0:4]],
                'COD':5*[COD[5:11]]}
    return data

def N_34_35(npag, COD):
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
def N_44_48(npag, COD):
    PQ = npag[0]
    PQ = float(PQ.replace(',','.'))
    MQ = npag[1]
    MQ = float(MQ.replace(',','.'))
    DHQ = npag[2]
    DHQ = float(DHQ.replace(',','.'))
    FXQ = npag[3]
    FXQ = float(FXQ.replace(',','.'))    
    NIQ = npag[4]
    NIQ = float(NIQ.replace(',','.'))
    
    PN = npag[5]
    PN = float(PN.replace(',','.'))
    MN = npag[6]
    MN = float(MN.replace(',','.'))
    DHN = npag[7]
    DHN = float(DHN.replace(',','.'))
    FXN = npag[8]
    FXN = float(FXN.replace(',','.'))    
    NIN = npag[9]
    NIN = float(NIN.replace(',','.'))
    
    PT = npag[10]
    PT = float(PT.replace(',','.'))
    MT = npag[11]
    MT = float(MT.replace(',','.'))
    DHT = npag[12]
    DHT = float(DHT.replace(',','.'))
    NIT = npag[14]
    NIT = float(NIT.replace(',','.'))
    FXT = npag[13]
    FXT = float(FXT.replace(',','.'))
    
    data = {'IFQ':[PQ, MQ ,DHQ ,FXQ, NIQ],'IFN':[PN, MN ,DHN ,FXN, NIN],
            'IM':[PT, MT ,DHT ,FXT, NIT], 'ANO':5*[COD[0:4]],'COD':5*[COD[5:11]]}
    return data

def dados_2013(pdf, COD):
    pag = pdf[2][0]
    pag = pag.splitlines()
    npag = []
    for x in range(0,len(pag)):
        if not (pag[x] == '' or pag[x] == ' '): npag.append(pag[x])
        if (16 <= len(npag) <= 22): data = N_20_22(npag, COD)
        elif (33 <= len(npag) <= 35): data = N_34_35(npag, COD)
        elif (len(npag) == 44 or len(npag) == 48): data = N_44_48(npag, COD)
    return data