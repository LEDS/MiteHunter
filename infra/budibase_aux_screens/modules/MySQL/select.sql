SELECT *,
	Agricultor.nome as agricultor,
	Propriedade.nome as propriedade,
	Talhao.nome as talhao,
	Cultivo.nome as cultivo_nome,
	Produto.nome as produto,
	TipoCultivar.nome as cultivar
FROM Agricultor
	INNER JOIN Propriedade
		ON Propriedade.agricultor_id = Agricultor.id
	INNER JOIN Talhao
		ON Talhao.propriedade_id = Propriedade.id
	INNER JOIN Cultivo
		ON Cultivo.talhao_id = Talhao.id
	INNER JOIN Amostragem
		ON Amostragem.cultivo_id = Cultivo.id
	LEFT JOIN Decisao
		ON Decisao.amostragem_id = Amostragem.id
	LEFT JOIN Produto
		ON Decisao.produto_id = Produto.id
	LEFT JOIN TipoCultivar
		ON Cultivo.tipoCultivar_id = TipoCultivar.id
