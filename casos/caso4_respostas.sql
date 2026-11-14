-- Q1. Por analista: quantos cenários, quantos ótimos, margem média e máxima (só os ótimos)
SELECT analista,
       COUNT(*)                                            AS cenarios,
       SUM(CASE WHEN status = 'optimal' THEN 1 ELSE 0 END) AS otimos,
       ROUND(AVG(margem))                                  AS margem_media,
       MAX(margem)                                         AS margem_maxima
  FROM cenarios
 GROUP BY analista
 ORDER BY analista;

-- Q2. Os 2 melhores cenários de cada analista (ranking dentro do grupo)
SELECT analista, id, margem, posicao
  FROM (SELECT analista, id, margem,
               RANK() OVER (PARTITION BY analista ORDER BY margem DESC) AS posicao
          FROM cenarios
         WHERE status = 'optimal') t
 WHERE posicao <= 2
 ORDER BY analista, posicao;

-- Q3. Para cada cenário ótimo: variação da margem em relação ao cenário anterior do mesmo analista
SELECT analista, criado_em, id, margem,
       margem - LAG(margem) OVER (PARTITION BY analista ORDER BY criado_em, id) AS variacao
  FROM cenarios
 WHERE status = 'optimal'
 ORDER BY analista, criado_em, id;

-- Q4. Fração dos cenários ótimos em que o produto P foi fabricado
SELECT ROUND(AVG(CASE WHEN p.cenario_id IS NOT NULL THEN 1.0 ELSE 0.0 END), 3) AS fracao_com_p
  FROM cenarios c
  LEFT JOIN producao p ON p.cenario_id = c.id AND p.produto = 'P'
 WHERE c.status = 'optimal';

-- Q5. Cenários cuja margem ficou acima da média de todos os cenários ótimos
SELECT id, analista, margem,
       ROUND(margem - AVG(margem) OVER ()) AS acima_da_media
  FROM cenarios
 WHERE status = 'optimal'
 ORDER BY margem DESC;
