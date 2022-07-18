use desafio_engenheiro;

SELECT 
  nome as cliente_nome, 
  ROUND(
    SUM(
      (valor_total * percentual / 100) - (
        valor_total * (percentual / 100) * (
          IFNULL(percentual_desconto, 0) / 100
        )
      )
    ), 
    2
  ) as valor 
FROM 
  cliente cli 
  INNER JOIN contrato con ON con.cliente_id = cli.cliente_id 
  INNER JOIN transacao tc ON tc.contrato_id = con.contrato_id 
where 
  ativo = 1 
GROUP BY 
  nome;