import os
import requests as rt
from pathlib import Path

"""
Recebe ano como inteiro e COD_ESC como string para determinar o  endereço do 
arquivo e definição do nome para ser salvo. Retorna o nome do arquivo.
"""
def download_pdf(ano, COD_ESC):

    ano = str(ano)  
    url = 'http://idesp.edunet.sp.gov.br/arquivos'+ano + '/'+COD_ESC+'.pdf'
    end_pdf = ano + '_' + COD_ESC + '.pdf'

    response = rt.get(url)
    filename = Path(end_pdf)
    filename.write_bytes(response.content)
    return end_pdf
"""
Faz o download de todos os aquivos do ano informado, verifica a se há erro na 
escrita de cada arquivo e exclui os arquivos errados.
"""

def download_pdf_ano(ano, COD):

    end_V = []
    end_F = []
    COD_V = []
    i = 0
    for x in COD:
        y = ano[i]
        while (y < 2019): 
            end_pdf = download_pdf(y, x)
            prop = os.stat(end_pdf)
            if prop.st_size == 1245:
                end_F.append(end_pdf)
                os.remove(end_pdf)
            else:
                end_V.append(end_pdf)
                COD_V.append(COD)
            y += 1
        i += 1
    
    for x in range(len(end_F),len(end_V)):
        end_F.append('')
    data = {'END_TRUE': end_V, 'END_FALSE': end_F}
    frame = pd.DataFrame(data)
    csv = frame.to_csv('NOME_ARQUIVOS.csv')
    return end_V