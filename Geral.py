import pandas as pd
import numpy as np
import PyPDF2 as p2
import LeituraPorAnoI as LPAI
import LeituraPorAnoII as LPAII
import LeituraPorAnoIII as LPAIII
import collections as cts

"""
Recebe o caminho do arquivo csv com os dados das escolas e retorna uma list 
do tipo string que cada posição contem o código da escola com seis digitos. 
Transforma a coluna COD_ESC em uma unica list do tipo string.
"""
def trans_csv(path):
    data = pd.read_csv(path)
    cod_n = np.array(data['COD_ESC'])
    cod_s = []
    for x in cod_n:
        x = str(x)
        if len(x) < 6: 
            cod_s.append('0'*(6-len(x)) + str(x))
        else:
            cod_s.append(x)
    return cod_s

"""
Recebe o caminho do arquivo pdf e retorna um 
dict(key=Nº, value=conteúdo da página).
"""
def le_pdf(path):
    arq = open(path, "rb")
    pdf = p2.PdfFileReader(arq)
    pg_pdf = {}
    for i in range(0, pdf.getNumPages()):        
        pg_pdf[i+1] = [pdf.getPage(i).extractText()]
        
    arq.close()
    return pg_pdf

"""
recebe um dict com a leitura primaria do pdf e retorna uma array somente com os
 valores na forma de strings.
"""
def nome():
    NOME = pd.read_csv('NOME_ARQUIVOS.csv')
    NOME = list(NOME['END_TRUE'])
    return NOME
    
def Monta_2011_2012(NOME):
    NOME11_12 = []
    for x in NOME:
        if (x[0:4] == '2011' or x[0:4] == '2012'): NOME11_12.append(x)
    
    pdf =  le_pdf(NOME11_12[0])
    
    data = LPAI.dados_2011_2012(pdf, NOME11_12[0])
    frame = pd.DataFrame(data, columns = ['AD','IFQ','IFN','IM','ANO','COD'], 
                             index = ['P','M','DH','FX','NI'])
    NOME = NOME11_12.pop(0)

    for x in NOME11_12:
        pdf =  le_pdf(x)
        data = LPAI.dados_2011_2012(pdf, x)
        temp = pd.DataFrame(data, columns = ['AD','IFQ','IFN','IM','ANO','COD'], 
                             index = ['P','M','DH','FX','NI'])
        frame = pd.concat([frame, temp])
    return frame

def Monta_2013(NOME):
    NOME13 = []
    for x in NOME:
        if (x[0:4] == '2013'): NOME13.append(x)
        
    pdf = le_pdf(NOME13[0])
    data = LPAII.dados_2013(pdf, NOME13[0])
    frame = pd.DataFrame(data, columns = ['AD','IFQ','IFN','IM','ANO','COD'], 
                             index = ['P','M','DH','FX','NI'])
    
    NOME = NOME13.pop(0)
    
    for x in NOME13:
        pdf =  le_pdf(x)
        data = LPAII.dados_2013(pdf, x)
        temp = pd.DataFrame(data, columns = ['AD','IFQ','IFN','IM','ANO','COD'], 
                             index = ['P','M','DH','FX','NI'])
        frame = pd.concat([frame, temp])
    return frame

def Monta_Depois_2013(NOME):
    NOMEDP = []
    for x in NOME:
        if not (x[0:4] == '2013' or x[0:4] == '2012' or 
                x[0:4] == '2011'): NOMEDP.append(x)
        
    pdf = le_pdf(NOMEDP[0])
    data = LPAIII.Monta_Depois_2013(pdf, NOMEDP[0])
    frame = pd.DataFrame(data, columns = ['AD','IFQ','IFN','IM','ANO','COD'], 
                             index = ['P','M','DH','FX','NI'])
    
    NOME = NOMEDP.pop(0)
    
    for x in NOMEDP:
        pdf =  le_pdf(x)
        data = LPAIII.Monta_Depois_2013(pdf, x)
        temp = pd.DataFrame(data, columns = ['AD','IFQ','IFN','IM','ANO','COD'], 
                             index = ['P','M','DH','FX','NI'])
        frame = pd.concat([frame, temp])
    return frame

def Monta_Tudo():
    NOME = nome()
    frameA = Monta_2011_2012(NOME)
    frameB = Monta_2013(NOME)
    frameC = Monta_Depois_2013(NOME)
    frame = pd.concat([frameA, frameB, frameC])
    return frame
