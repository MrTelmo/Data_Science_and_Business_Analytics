-- P1) Quais os títulos, dias e horas dos espetáculos registados na BD?
SELECT titulo, dia, hora FROM public.espetaculo
LIMIT 20;
-- P2) Quais as categorias e os títulos dos espetáculos registados na BD?
SELECT categoria, titulo FROM public.espetaculo
LIMIT 20;
-- P3) Quais os nomes e datas de nascimento dos cantores registados? Ordene o resultado por data de nascimento crescente.
SELECT nome, d_nasc, tipo FROM public.artista
WHERE tipo = 'cantor'
ORDER BY d_nasc ASC
LIMIT 20;
-- P4) Quais os emails e os nomes dos espectadores do Porto? Ordene o resultado por email.
SELECT email, nome, cidade FROM public.espectador
WHERE cidade = 'Porto'
ORDER BY email ASC
LIMIT 20;
-- P5) Relativamente a cada artista, liste o seu nome e o dia e o título dos espetáculos em que foi o artista principal.
-- Ordene o resultado por nome crescente e por data decrescente
SELECT nome, dia, titulo FROM public.artista a
JOIN public.espetaculo s
ON a.nif=s.nif
ORDER BY nome ASC, dia DESC
LIMIT 20;
-- P6) Relativamente a cada espetador, liste o seu nome e o lugar e o custo dos bilhetes que adquiriu.
-- Ordene o resultado por nome crescente e por custo decrescente.
SELECT nome, lugar, custo FROM public.espectador e
JOIN public.bilhete b
ON e.email=b.email
ORDER BY nome ASC, custo DESC
LIMIT 20;
-- P7) Indique, sem repetições, o nome dos espectadores que compraram bilhetes para os espetáculos e o nome do artista.
SELECT DISTINCT e.nome, a.nome FROM public.espectador e
JOIN public.bilhete b
ON e.email=b.email
JOIN public.espetaculo s
ON b.id=s.id
JOIN public.artista a
ON a.nif=s.nif
LIMIT 20;
-- P8) Liste os nomes de todas as pessoas, espectadores e artistas, desde que os espectadores sejam do Porto e os artistas sejam atores.
SELECT nome FROM public.espectador
WHERE cidade = 'Porto'
UNION
SELECT nome FROM public.artista
WHERE tipo = 'ator'
LIMIT 20;
-- P9) Liste os nomes de todas as pessoas que não são do Porto e que não têm nomes de artistas.
SELECT e.nome FROM public.espectador e
LEFT JOIN public.artista a 
ON SPLIT_PART(e.nome, ' ', 1) = SPLIT_PART(a.nome, ' ', 1)
WHERE e.cidade != 'Porto' AND a.nif IS NULL
LIMIT 20;
-- OR
SELECT nome FROM public.espectador
WHERE cidade != 'Porto'
AND NOT EXISTS (
    SELECT 1
    FROM public.artista
    WHERE SPLIT_PART(espectador.nome, ' ', 1) = SPLIT_PART(artista.nome, ' ', 1) )
LIMIT 20;
-- P10) Qual a receita total por espetáculo? Indique o id, o título e o valor total dos bilhetes.
SELECT s.id, titulo, SUM(custo) AS valor_total FROM public.espetaculo s
JOIN public.bilhete b
ON s.id=b.id
GROUP BY s.id, titulo
LIMIT 20;
-- P11) Qual a receita total por categoria de espetáculo? Indique a categoria e o valor total dos bilhetes.
SELECT categoria, SUM(custo) AS valor_total FROM public.espetaculo s
JOIN public.bilhete b
ON s.id=b.id
GROUP BY categoria
LIMIT 20;
-- P12) Quem (email) foi a todos os espetáculos do Tony Carreira?
SELECT b.email FROM public.bilhete b
JOIN public.espetaculo s
ON b.id = s.id
JOIN public.artista a
ON s.nif = a.nif
WHERE a.nome = 'Tony Carreira'
GROUP BY b.email
HAVING COUNT(DISTINCT s.id) = (
-- Subquery to calculate total number of shows - Tony Carreira
    SELECT COUNT(*)
    FROM public.espetaculo s2
    JOIN public.artista a2
	ON s2.nif = a2.nif
    WHERE a2.nome = 'Tony Carreira')
LIMIT 20;