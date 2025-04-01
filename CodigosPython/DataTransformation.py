import tabula
import pandas as pd
import os
import zipfile
from datetime import datetime

ARQUIVO = r"C:\Users\guilh\OneDrive\Documents\Teste IntuitiveCare\Anexos\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
PASTA = r"C:\Users\guilh\OneDrive\Documents\Teste IntuitiveCare\Tabela"

def lerTabelas():
    try:
        if not os.path.exists(PASTA):
            os.makedirs(PASTA)
            
        TabelasDoPDF = tabula.read_pdf(
            ARQUIVO,
            pages='3-181',  
            multiple_tables=False,  
            lattice=True
        )

        if TabelasDoPDF:
            tabelaCompletaCSV = TabelasDoPDF[0]
            tabelaCompletaCSV = tabelaCompletaCSV[~tabelaCompletaCSV.eq(tabelaCompletaCSV.iloc[0]).all(axis=1)]
            
            substituiNomeColunas = {
                'OD': 'Seg. Odontológica',
                'AMB': 'Seg. Ambulatorial'
            }
            
            for coluna in tabelaCompletaCSV.columns:
                tabelaCompletaCSV[coluna] = tabelaCompletaCSV[coluna].replace(substituiNomeColunas)
            
            nomeArquivoCSV = os.path.join(PASTA, "Teste_GuilhermeLobato.csv")
            tabelaCompletaCSV.to_csv(nomeArquivoCSV, index=False, encoding='utf-8-sig')
            
            nomeArquivoZIP = os.path.join(PASTA, f"Teste_GuilhermeLobato.zip")
            with zipfile.ZipFile(nomeArquivoZIP, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(nomeArquivoCSV, os.path.basename(nomeArquivoCSV))

        print(f"Arquivo CSV compactado!")
            
    except Exception as e:
        print(f"Erro ao ler o PDF: {str(e)}")
        

if __name__ == "__main__":
    lerTabelas()


