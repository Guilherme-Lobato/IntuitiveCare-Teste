## Estrutura do Projeto

```
.
├── CodigosPython/           # Testes 1 e 2 - Web Scraping e Transformação de Dados
│   ├── web_scraping.py     # Script para download dos PDFs
│   └── transformacao.py    # Script para extração e transformação dos dados
├── DadosANS/               # Teste 3 - Banco de Dados
│   ├── queries.sql        # Scripts SQL para criação e manipulação do banco
│   └── dados/             # Pasta para armazenamento dos dados baixados
└── TesteAPI/              # Teste 4 - API e Interface Web
    ├── backend/           # Servidor Python
    └── interface/         # Frontend Vue.js
```

## Requisitos do Sistema

- Python 3.8 ou superior
- Node.js 14 ou superior
- MySQL 8.0 ou PostgreSQL 10.0 ou superior
- Git

## Instalação e Configuração

### 1. Teste de Web Scraping e Transformação de Dados

```bash
cd CodigosPython
pip install -r requirements.txt
```

### 2. Teste de Banco de Dados

1. Instale o MySQL 8.0 ou PostgreSQL 10.0
2. Configure a conexão com o banco de dados
3. Execute as queries

### 3. Teste de API e Interface Web

1. Backend (Python):
```bash
cd TesteAPI/backend
pip install -r requirements.txt
```

2. Frontend (Vue.js):
```bash
cd TesteAPI/interface
npm install
```

## Executando os Testes

### 1. Web Scraping e Transformação de Dados

```bash
cd CodigosPython
py web_scraping.py
py transformacao.py
```

### 2. Banco de Dados

1. Baixe os dados necessários:
   - Demonstrações contábeis dos últimos 2 anos
   - Dados cadastrais das operadoras ativas
2. Execute as queries SQL para importação dos dados
3. Execute as queries analíticas para obter as informações solicitadas

### 3. API e Interface Web

1. Inicie o servidor backend:
```bash
cd TesteAPI/backend
py main.py
```

2. Em outro terminal, inicie o frontend:
```bash
cd TesteAPI/interface
npm run serve
```

3. Acesse a aplicação em `http://localhost:8080`

## Detalhes dos Testes

### 1. Teste de Web Scraping
- Acesso ao site da ANS
- Download dos Anexos I e II em PDF
- Compactação dos anexos em ZIP

### 2. Teste de Transformação de Dados
- Extração de dados do PDF do Anexo I
- Conversão para CSV
- Substituição de abreviações
- Compactação do resultado

### 3. Teste de Banco de Dados
- Estruturação de tabelas
- Importação de dados
- Queries analíticas para:
  - Top 10 operadoras por despesas no último trimestre
  - Top 10 operadoras por despesas no último ano

### 4. Teste de API
- Servidor Python com rota de busca
- Interface Vue.js para interação

