-- Queries Exercises Class 3

-- Quick table visualisation
SELECT * FROM actor
LIMIT 10;


-- Using SELECT --
-- A.1 Select only the first name
SELECT first_name FROM public.actor
LIMIT 10;

-- A.2  Select only first and last names
SELECT first_name, last_name FROM public.actor
LIMIT 10;

-- A.3 Select only distinct first name.
SELECT DISTINCT first_name FROM public.actor
LIMIT 10;

-- A.4 Select only distinct first names that are different from Nick
SELECT DISTINCT first_name FROM public.actor
WHERE first_name != 'Nick'
LIMIT 10;
/* OR other way
SELECT DISTINCT first_name FROM public.actor
WHERE first_name <> 'Nick';
SELECT DISTINCT first_name FROM public.actor
WHERE first_name NOT LIKE 'Nick'; */

	
-- Using ORDER BY --
-- B.1 Select all actor’s data sorted by last_name
SELECT * FROM public.actor
ORDER BY last_name ASC
LIMIT 10;

-- B. 2  Select all actor’s data sorted by last name but by descending order
SELECT * FROM actor
ORDER BY last_name DESC
LIMIT 10;

-- B.3 Select first and last names, sorted by last name by ascending order, from actors whose first name starts with a ‘B’
SELECT first_name, last_name FROM actor
WHERE first_name LIKE 'B%'
ORDER BY last_name ASC
LIMIT 10;


-- Using GROUP BY --
-- C. 1 Number of records of the actor’s table.
SELECT COUNT(*) FROM public.actor;

-- C. 2 How many actors have the same first name, sorted by first name but descending
SELECT first_name, COUNT(*) FROM public.actor
GROUP BY first_name
HAVING COUNT(*) > '1'
ORDER BY first_name DESC;

-- C.3 Create an alias for the count column named ‘howmany’.
SELECT first_name, COUNT(*) howmany FROM public.actor
GROUP BY first_name
ORDER BY first_name DESC; -- Z to A
--(ORDER BY howmany ASC to see the differences)
SELECT first_name, COUNT(*) howmany FROM public.actor
GROUP BY first_name
ORDER BY howmany DESC;
--(showcase only actors with repreated names to appear)
SELECT first_name, COUNT(*) howmany FROM public.actor
GROUP BY first_name
HAVING COUNT (*)>1
ORDER BY howmany ASC;

-- C. 4 Reuse the previous query and sort it by ‘howmany’ in descending order and by ‘first_name’ ascending
SELECT first_name, COUNT(*) howmany FROM public.actor
GROUP BY first_name
ORDER BY howmany DESC, first_name ASC;


-- Using LIMIT, OFFSET & FETCH --
-- D. 1  Select the first 6 rows of actor’s table
SELECT * FROM public.actor
LIMIT 6;

-- D. 2 Select 4 rows (from the 3rd until the 6th) from actor’s table
SELECT * FROM public.actor
OFFSET 2 ROWS
LIMIT 4;

-- D. 3 Same as before but using FETCH
SELECT * FROM public.actor
OFFSET 2 ROWS
FETCH FIRST 4 ROWS ONLY;


-- USING HAVING --
-- E. 1 For each ‘customer_id’ in payment’s table, show the total of the amounts paid
SELECT customer_id, SUM(amount) FROM public.payment
GROUP BY customer_id;

-- E. 2 Same as before, filtering the customers that spent more than 200€
SELECT customer_id, SUM(amount) FROM public.payment
GROUP BY customer_id
HAVING SUM(amount) > 200;


-- USING UNION & UNION ALL --
-- F. 1 Count the number of customers
SELECT COUNT(*) FROM public.customer;

-- F. 2 Count the number of actors
SELECT COUNT(*) FROM public.actor;

-- F. 3 List the distinct first names of actors and customers in the same column.
SELECT first_name FROM public.actor a
UNION
SELECT first_name FROM public.customer c;
/* UNION remove duplicates */

-- F. 4 List the first names of actors and customers in the same column
SELECT first_name FROM public.actor a
UNION ALL
SELECT public.first_name FROM customer c;
/* UNION ALL include duplicates */


-- USING INTERSECT & EXCEPT --
-- G. 1 Select actors and customer with the same first_name
SELECT first_name FROM public.actor a
INTERSECT
SELECT first_name FROM public.customer c;

-- G. 2 Select customers and actors with different first_name
SELECT first_name FROM public.customer c
EXCEPT
SELECT first_name FROM public.actor a;


-- USING BETWEEN, IN, IS NULL --
-- H. 1 Select customers that have ID between 9-15
SELECT * FROM public.customer
WHERE customer_id BETWEEN 9 and 15;

-- H. 2 Select customers whose first name are Lisa or Marion
SELECT * FROM public.customer
WHERE first_name IN ('Lisa', 'Marion');

-- H. 3 Select staff information where picture is NULL
SELECT * FROM public.staff
WHERE picture IS NULL;

-- H. 4 Select staff information where picture is not NULL
SELECT * FROM public.staff
WHERE picture IS NOT NULL;


-- Mix Exercises --
-- I. 1 For each customer in customer table, show first and last names and the corresponding address, from address table.
SELECT first_name, last_name, address FROM public.customer AS c
JOIN public.address AS a
ON c.address_id = a.address_id;
/* NOTE: 'AS' is not mandatory, could be hiden, code will follow the same tasks */

-- I. 2 Identify the existing ‘address_id’s on table address which have no corresponding customer - without using JOIN
SELECT address_id FROM public.address
EXCEPT
SELECT address_id FROM public.customer
ORDER BY 1;
/* OR other way using JOIN
SELECT c.first_name, c.last_name, a.address, a.address_id FROM public.customer c
right JOIN public.address a 
ON c.address_id=a.address_id
ORDER Y address_id asc; */

-- I. 3  List ‘address_id’, ‘address’, ‘first_name’ for customers with ‘address_id’<=7, sorted by ‘address_id’.
SELECT a.address_id, address, first_name FROM public.customer c
INNER JOIN public.address a 
ON c.address_id = a.address_id
WHERE a.address_id <= 7
ORDER BY a.address_id;
/* OR other way
SELECT c.first_name, c.last_name, a.address FROM public.customer c, public.address a
WHERE c.address_id=a.address_id
AND c.address_id<=7
ORDER BY c.address_id;  */

-- I. 4. List ‘address_id’, ‘address’, ‘first_name’ for customers with ‘address_id’<=7, sorted by ‘address_id’ - using LEFT JOIN
SELECT c.address_id, a.address, c.first_name FROM public.customer c
LEFT JOIN public.address a 
ON c.address_id = a.address_id
WHERE a.address_id <= 7
ORDER BY a.address_id;
-- Now using RIGTH JOIN
SELECT a.address_id, a.address, c.first_name FROM public.customer c
RIGHT JOIN public.address a 
ON a.address_id=c.address_id
WHERE a.address_id<=7
ORDER BY address_id;

---I.5 Select the unique last names of all customers, the title, the language name, and the rental rate of every film they have rented that costs at least 2.99.
SELECT DISTINCT a.last_name AS name,
	d.title AS titulo,
	e.name AS language_name,
	d.rental_rate
FROM public.customer a
JOIN public.rental b 
ON a.customer_id = b.customer_id
JOIN public.inventory c 
ON c.inventory_id = b.inventory_id
JOIN public.film d 
ON d.film_id = c.film_id
JOIN public.language e 
ON d.language_id = e.language_id
WHERE d.rental_rate >= 2.99