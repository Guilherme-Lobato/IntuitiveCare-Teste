from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_data():
    csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'DadosANS', 'Relatorio_cadop.csv')
    df = pd.read_csv(csv_path, sep=';', encoding='utf-8')
    return df.replace({np.nan: None})

@app.get("/api/operadoras")
async def buscar_operadoras(termo: str = ""):
    df = load_data()
    
    if not termo:
        return df.to_dict('records')
    
    mask = (
        df['Razao_Social'].str.contains(termo, case=False, na=False) |
        df['Nome_Fantasia'].str.contains(termo, case=False, na=False) |
        df['Cidade'].str.contains(termo, case=False, na=False) |
        df['UF'].str.contains(termo, case=False, na=False)
    )
    
    return df[mask].to_dict('records')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 