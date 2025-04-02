# Testes de Nivelamento v.250321

Este projeto contém 4 testes de nivelamento para a IntuitiveCare, cada um focado em uma área específica de desenvolvimento.

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
2. Configure as credenciais do banco de dados no arquivo de configuração
3. Execute os scripts SQL na ordem:
   ```bash
   cd DadosANS
   mysql -u seu_usuario -p < queries.sql  # Para MySQL
   # ou
   psql -U seu_usuario -d seu_banco -f queries.sql  # Para PostgreSQL
   ```

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
python web_scraping.py
python transformacao.py
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
python main.py
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
- Documentação Postman disponível

## Documentação Adicional

- A documentação da API está disponível no Postman
- Os scripts SQL incluem comentários explicativos
- Os códigos Python incluem documentação inline

## Observações

- Mantenha as credenciais do banco de dados seguras
- Os arquivos grandes não estão incluídos no repositório
- Siga as instruções específicas de cada teste para execução 