-- 3.3 | TABELAS

-- arquivo .csv
CREATE TABLE relatorio_cadop (
    Registro_ANS VARCHAR(20) PRIMARY KEY,
    CNPJ VARCHAR(18) NOT NULL,
    Razao_Social VARCHAR(255) NOT NULL,
    Nome_Fantasia VARCHAR(255) NOT NULL,
    Modalidade VARCHAR(255) NOT NULL,
    Logradouro VARCHAR (255) NOT NULL,
    Numero INT NOT NULL,
    Complemento VARCHAR(255),
    Bairro VARCHAR (100) NOT NULL,
    Cidade VARCHAR (100) NOT NULL,
    UF CHAR(2),
    CEP INT(8),
    DDD INT(3),
    Telefone INT(9),
    Fax INT(20),
    Endereco_eletronico VARCHAR (50),
    Representante VARCHAR (30),
    Cargo_Representante VARCHAR (30),
    Regiao_de_Comercializacao VARCHAR (30),
    Data_Registro_ANS DATE
);

-- repositório dos dois ultimos anos
CREATE TABLE dados_adm (
    DATA DATE,
    REG_ANS VARCHAR(255),
    CD_CONTA_CONTABIL VARCHAR(255),
    DESCRICAO TEXT,
    VL_SALDO_INICIAL DECIMAL(15,2),
    VL_SALDO_FINAL DECIMAL(15,2)
);

-- 3.4 
LOAD DATA INFILE 'DadosANS/Relatorio_cadop.csv'
INTO TABLE relatorio_cadop
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, @Data_Registro_ANS)
SET Data_Registro_ANS = STR_TO_DATE(@Data_Registro_ANS, '%d/%m/%Y');

-- Alterar o caminho do arquivo para carregar cada semestre
LOAD DATA INFILE 'DadosANS/4T2023/4T2023.csv'
INTO TABLE dados_adm
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @VL_SALDO_INICIAL, @VL_SALDO_FINAL)
SET 
    DATA = STR_TO_DATE(@DATA, '%d/%m/%Y'),
    VL_SALDO_INICIAL = REPLACE(@VL_SALDO_INICIAL, ',', '.'),
    VL_SALDO_FINAL = REPLACE(@VL_SALDO_FINAL, ',', '.');

-- 3.5 | QUERY'S ANALÍTICAS 

/* Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre? */
SELECT
    REG_ANS,
    SUM(VL_SALDO_FINAL - VL_SALDO_INICIAL) AS TOTAL_DESPESAS
FROM dados_adm
WHERE DESCRICAO = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"
AND DATA >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
GROUP BY REG_ANS
ORDER BY TOTAL_DESPESAS DESC
LIMIT 10;

/* Quais as 10 operadoras com maiores despesas nessa categoria no último ano? */
SELECT
    REG_ANS,
    SUM(VL_SALDO_FINAL - VL_SALDO_INICIAL) AS TOTAL_DESPESAS
FROM dados_adm
WHERE DESCRICAO = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"
AND DATA >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)
GROUP BY REG_ANS
ORDER BY TOTAL_DESPESAS DESC
LIMIT 10;