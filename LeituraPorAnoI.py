    #P -> Português       Q -> Quinto ano
    #M -> Matemática      N -> Nono ano
    #DH -> Desempenho     T -> terceiro ano
    #FX -> Fluxo
    #NI -> Nota IDESP
import pandas as pd

def P_NonoTerceito(pag, COD):
    x = 22
    PN = pag[0:6]
    PN = float(PN.replace(',','.'))
    MN = pag[6:12]
    MN = float(MN.replace(',','.'))
    DHN = pag[12:16]
    DHN = float(DHN.replace(',','.'))
    FXN = pag[16:22]
    FXN = float(FXN.replace(',','.'))
        
    while (pag[x].isdigit()): x += 1
    while not (pag[x].isdigit()): x += 1
        
    NIN = pag[x:x+4]        
    NIN = float(NIN.replace(',','.'))
    PT = pag[x+18:x+24]
    PT = float(PT.replace(',','.'))
    MT = pag[x+24:x+30]
    MT = float(MT.replace(',','.'))
    DHT = pag[x+8:x+12]
    DHT = float(DHT.replace(',','.'))
    NIT = pag[x+4:x+8]        
    NIT = float(NIT.replace(',','.'))
    FXT = pag[x+12:x+18]
    FXT = float(FXT.replace(',','.'))
        
    data = {'IFN':[PN, MN ,DHN ,FXN, NIN],'IM':[PT, MT ,DHT ,FXT, NIT],
                'ANO':5*[COD[0:4]],'COD':5*[COD[5:11]]}
    return data

def P_Quinto(pag, COD):
    x = 10
    FX = pag[0:6]
    FX = float(FX.replace(',','.'))
    NI = pag[6:10]        
    NI = float(NI.replace(',','.'))
    
    while (pag[x].isdigit()): x += 1
    while not (pag[x].isdigit()): x += 1
        
    P = pag[x:x+6]
    P = float(P.replace(',','.'))
    M = pag[x+6:x+12]
    M = float(M.replace(',','.'))
    DH = pag[x+12:x+16]
    DH = float(DH.replace(',','.'))
       
    data = {'IFQ':[P, M ,DH ,FX, NI],'ANO':5*[COD[0:4]],
                'COD':5*[COD[5:11]]}
    return data

def P_QuintoNono(pag, COD):
    x = 32
    FXQ = pag[0:6]
    FXQ = float(FXQ.replace(',','.'))
    NIQ = pag[6:10]        
    NIQ = float(NIQ.replace(',','.'))
    PN = pag[10:16]
    PN = float(PN.replace(',','.'))
    MN = pag[16:22]
    MN = float(MN.replace(',','.'))
    DHN = pag[22:26]
    DHN = float(DHN.replace(',','.'))
    FXN = pag[26:32]
    FXN = float(FXN.replace(',','.'))
       
    while (pag[x].isdigit()): x += 1
    while not (pag[x].isdigit()): x += 1
       
    PQ = pag[x:x+6]        
    PQ = float(PQ.replace(',','.'))
    MQ = pag[x+6:x+12]
    MQ = float(MQ.replace(',','.'))
    DHQ = pag[x+12:x+16]
    DHQ = float(DHQ.replace(',','.'))
    NIN = pag[x+16:x+20]        
    NIN = float(NIN.replace(',','.'))
       
    data = {'IFQ':[PQ, MQ ,DHQ ,FXQ, NIQ],'IFN':[PN, MN ,DHN ,FXN, NIN],
                'ANO':5*[COD[0:4]],'COD':5*[COD[5:11]]}
    return data

def P_Nono(pag, COD):
    x = 10
    P = pag[0:6]
    P = float(P.replace(',','.'))
    M = pag[6:12]
    M = float(M.replace(',','.'))
    DH = pag[12:16]
    DH = float(DH.replace(',','.'))
    FX = pag[16:22]
    FX = float(FX.replace(',','.'))
    
    while (pag[x].isdigit()): x += 1
    while not (pag[x].isdigit()): x += 1
        
    NI = pag[x:x+4]        
    NI = float(NI.replace(',','.'))
       
    data = {'IFQ':[P, M ,DH ,FX, NI],'ANO':5*[COD[0:4]],
                'COD':5*[COD[5:11]]}
    return data

def P_Terceiro(pag, COD):
    x = 6       
    while not (pag[x].isdigit()): x += 1
    P = pag[x+14:x+20]
    P = float(P.replace(',','.'))
    M = pag[x+20:x+26]
    M = float(M.replace(',','.'))
    DH = pag[x+26:x+30]
    DH = float(DH.replace(',','.'))
    FX = pag[x+8:x+14]
    FX = float(FX.replace(',','.'))    
    NI = pag[x+4:x+8]        
    NI = float(NI.replace(',','.'))
           
    data = {'IM':[P, M ,DH ,FX, NI],'ANO':5*[COD[0:4]],
                'COD':5*[COD[5:11]]}
    return data

def dados_2011_2012(pdf, COD):   
    pag = pdf[2][0]
    
    #quinto ano -> 10
    if (pag.find(COD[5:11]) == 10):
        data = P_Quinto(pag, COD)
    #nono e terceiro anos -> 22
    elif (len(pag) > 147 and pag.find(COD[5:11]) == 22):    
        data = P_NonoTerceito(pag, COD)
    #quinto e nonos anos -> 32
    elif (pag.find(COD[5:11]) == 32):
        data = P_QuintoNono(pag, COD)
    #Nono ano -> 22
    elif (len(pag) <= 147 and pag.find(COD[5:11]) == 22):
        data  = P_Nono(pag, COD)
    #terceiro ano -> 0
    elif (pag.find(COD[5:11]) == 0):
        data = P_Terceiro(pag, COD)
        
    frame = pd.DataFrame(data, columns = ['IFQ','IFN','IM','ANO','COD'], 
                             index = ['P','M','DH','FX','NI'])
    return frame