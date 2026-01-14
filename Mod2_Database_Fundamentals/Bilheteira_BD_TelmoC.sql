-- Q1) What are the titles, dates, and times of the shows registered in the database?
SELECT titulo, dia, hora FROM public.espetaculo
LIMIT 20;
-- Q2) What are the categories and titles of the shows registered in the database?
SELECT categoria, titulo FROM public.espetaculo
LIMIT 20;
-- Q3) What are the names and birth dates of the registered singers? Order the result by birth date in ascending order.
SELECT nome, d_nasc, tipo FROM public.artista
WHERE tipo = 'cantor'
ORDER BY d_nasc ASC
LIMIT 20;
-- Q4) What are the emails and names of the spectators from Porto? Order the result by email.
SELECT email, nome, cidade FROM public.espectador
WHERE cidade = 'Porto'
ORDER BY email ASC
LIMIT 20;
-- Q5) For each artist, list their name, along with the date and title of the shows where they were the main artist.
-- Order the result by name in ascending order and by date in descending order.
SELECT nome, dia, titulo FROM public.artista a
JOIN public.espetaculo s
ON a.nif=s.nif
ORDER BY nome ASC, dia DESC
LIMIT 20;
-- Q6) For each spectator, list their name, the seat, and the cost of the tickets they purchased.
-- Order the result by name in ascending order and by cost in descending order.
SELECT nome, lugar, custo FROM public.espectador e
JOIN public.bilhete b
ON e.email=b.email
ORDER BY nome ASC, custo DESC
LIMIT 20;
-- Q7) List, without duplicates, the names of the spectators who purchased tickets for the shows and the name of the corresponding artist.
SELECT DISTINCT e.nome, a.nome FROM public.espectador e
JOIN public.bilhete b
ON e.email=b.email
JOIN public.espetaculo s
ON b.id=s.id
JOIN public.artista a
ON a.nif=s.nif
LIMIT 20;
-- Q8) List the names of all people (spectators and artists), provided the spectators are from Porto and the artists are actors.
SELECT nome FROM public.espectador
WHERE cidade = 'Porto'
UNION
SELECT nome FROM public.artista
WHERE tipo = 'ator'
LIMIT 20;
-- Q9) List the names of all people who are not from Porto and do not share a name with any artist.
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
-- Q10) What is the total revenue per show? Indicate the ID, the title, and the total value of the tickets.
SELECT s.id, titulo, SUM(custo) AS valor_total FROM public.espetaculo s
JOIN public.bilhete b
ON s.id=b.id
GROUP BY s.id, titulo
LIMIT 20;
-- Q11) What is the total revenue per show category? Indicate the category and the total value of the tickets.
SELECT categoria, SUM(custo) AS valor_total FROM public.espetaculo s
JOIN public.bilhete b
ON s.id=b.id
GROUP BY categoria
LIMIT 20;
-- Q12) Who (email) attended all of Tony Carreira's shows?
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
