-- Queries Exercises Class 2

-- Exercise 1: Showcase all data from clients table
select * from clients;

-- Exercise 2: List all clients id and names, where id number < 6000
select id, name from clients 
where id < '6000';

-- Exercise 3.1: List all clients id and name where name starts with 'R'
select * from public.clients
where name like 'R%';
-- Exercise 3.2: List all clients id and name where name ends with 'a'
select * from public.clients
where name like '%a';
-- Exercise 3.3: List all clients id and name where name starts with 'R', or id number is between 4000 and 5000
select id, name from public.clients 
where name like 'R%' 
or id between '4000' and '5000';

-- Exercise 4: Select codes that have clients
select code from public.clients_subs
select distinct code from public.clients_subs;

-- Exercise 5: Which salary would be above 40€ if we raise salaries by 20%?
select id, code, salary*1.2 as new_salary from public.pts_work
where salary*1.2 > '40';

-- Exercise 6: List ids of clients that practise aerobic - 'AE' and swimming - 'NT'
select id, code
from public.clients_subs 
where code IN ('AE','NT');
-- OR could do this way
select id, code
from public.clients_subs
where code = 'AE' or code ='NT';

-- Exercise 7: Obtain the list of sports codes and clients ids, order accordingly - codes ascending and ids descending 
select code, id
from public.clients_subs
order by code, id desc;

-- Exercise 8: Obtain average salary, number and total of salaries, as well as min and max salaries
SELECT 
    ROUND(AVG(salary), 2) AS mean,  
    COUNT(*) AS number, 
    SUM(salary) AS total, 
    MAX(salary) AS max,
    MIN(salary) AS min
FROM public.pts_work

-- Exercise 9: Calculate the total payment per client - id and amount
select id, sum(payment) from public.clients_subs
group by id
order by sum(payment) desc

-- Exercise 10: Calculate total amount paid by the clients, where the total payment is above 40€
select id, sum(payment) from public.clients_subs
group by id
having sum(payment) > 40

-- Exercise 11: List names, and sports code for all clients that practise aerobic - 'AE' and swimming - 'NT'
select name, code
from public.clients
join public.clients_subs 
on clients.id=clients_subs.id 
where code in ('AE', 'NT')

-- Exercise 12: List name, and sport description for all clients that practise - 'AE' and swimming - 'NT'
select c.name, description
from clients c
join public.clients_subs cs 
on c.id=cs.id
join public.sports s 
on cs.code = s.code 
where cs.code in ('AE', 'NT')
order by 1 asc

-- Exercise 13: List all client and personal trainer names
select name from public.clients
Union
select name from public.personal_trainers

-- Exercise 14: List common clients and personal trainer names
select name from public.clients
intersect
select name from public.personal_trainers
--NOTE: there are no common names



-- Create View: to aggregate client id and total payments
CREATE OR REPLACE VIEW public.clients_payments AS
select id, sum(payment) as total_payment from public.clients_subs
group by id

-- Leverage the created view: to easily check clients total payments
SELECT * FROM public.clients_payments cp
JOIN public.clients c
on cp.id=c.id
