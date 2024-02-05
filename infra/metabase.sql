-- Localização das Propriedades (pin map)
SELECT 
    Agricultor.nome,
    ST_X( Propriedade.ponto) AS latitude,
    ST_Y( Propriedade.ponto) AS longitude,
    Propriedade.id
FROM Propriedade 
    INNER JOIN Agricultor
        ON Propriedade.agricultor_id = Agricultor.id

WHERE {{agricultor}}

-- Situação da Infestação por ácaro rajado no polo do morango (HeatMap)
WITH Tabela AS (
    SELECT
        Foliolo.qntRajado, 
        
        Amostragem.data_Amos,
        
        Propriedade.municipio,
        Propriedade.id AS propriedade_id
    
    FROM Foliolo
        INNER JOIN Amostragem
            ON Foliolo.amostragem_id = Amostragem.id
        INNER JOIN Cultivo
            ON Amostragem.cultivo_id = Cultivo.id
        INNER JOIN Talhao
            ON Cultivo.talhao_id = Talhao.id
        INNER JOIN Propriedade
            ON Talhao.propriedade_id = Propriedade.id
    
    WHERE {{TEMPO}}
    )

SELECT 
    SUM(qntRajado),
    data_Amos,
    municipio,
    propriedade_id
    
FROM Tabela
GROUP BY propriedade_id, data_Amos


-- main Map (line map)
WITH Tabela AS
(
SELECT
    Foliolo.qntRajado,
    Foliolo.qntMacropilis,
    Foliolo.qntCalifornicus,
    Foliolo.amostragem_id,
    
    Amostragem.data_Amos,
    
    Agricultor.nome AS agricultornome,
    
    Propriedade.nome AS propriedadenome,
    Cultivo.nome AS cultivonome,
    Cultivo.dataIni,
    Talhao.nome AS talhaonome,
    
    Decisao.data_Deci
    
FROM Foliolo
    INNER JOIN Amostragem
        ON Foliolo.amostragem_id = Amostragem.id
    INNER JOIN Decisao
        ON Decisao.amostragem_id = Amostragem.id
    INNER JOIN Cultivo
        ON Amostragem.cultivo_id = Cultivo.id
    INNER JOIN Talhao
        ON Cultivo.talhao_id = Talhao.id
    INNER JOIN Propriedade
        ON Talhao.propriedade_id = Propriedade.id 
    INNER JOIN Agricultor
        ON Propriedade.agricultor_id = Agricultor.id
WHERE {{Agricultor}} AND {{Propriedade}} AND {{Cultivo}} AND {{Talhao}} AND {{Data}}
)

SELECT 
    SUM(qntRajado) as qntRajado,
    SUM(qntMacropilis) as qntMacropilis,
    SUM(qntCalifornicus) as qntCalifornicus,
    amostragem_id,
    data_Amos,
    data_Deci

FROM Tabela
GROUP BY data_Amos, data_Deci, amostragem_id