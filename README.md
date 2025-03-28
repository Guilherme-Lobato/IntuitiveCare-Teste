# Web Scraping ANS

Este projeto é um script em Python que realiza web scraping no site da ANS (Agência Nacional de Saúde Suplementar) para baixar automaticamente os Anexos I e II do Rol de Procedimentos e Eventos em Saúde.

## Funcionalidades

- Acesso automático ao site da ANS
- Download dos Anexos I e II em formato PDF
- Compactação dos arquivos em um único arquivo ZIP

## Pré-requisitos

- Python 3.x
- Chrome instalado
- Bibliotecas Python:
  - selenium
  - webdriver-manager
  - requests

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/web-scraping-ans.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como usar

Execute o script:
```bash
python WebScraping.py
```

Os arquivos serão salvos na pasta `Anexos` e compactados em um arquivo ZIP.

## Estrutura do Projeto

- `WebScraping.py`: Script principal
- `requirements.txt`: Lista de dependências
- `Anexos/`: Pasta onde os arquivos são salvos (não versionada) 