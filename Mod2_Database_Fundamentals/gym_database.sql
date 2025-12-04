-- Creating tables
CREATE TABLE public.clients
( id character varying(20) PRIMARY KEY, name character varying(100) NOT NULL ); 
CREATE TABLE public.personal_trainers
( id character varying(20) PRIMARY KEY, name character varying(100) NOT NULL ); 
CREATE TABLE public.sports
( code character varying(10) PRIMARY KEY, description character varying(100) NOT NULL ); 
CREATE TABLE public.pts_work
( id character varying(20) REFERENCES public.personal_trainers(id), code character varying(10) REFERENCES public.sports(code), salary integer NOT NULL); 
CREATE TABLE public.clients_subs 
( id character varying(20) REFERENCES public.clients(id), code character varying(10) REFERENCES public.sports(code), payment integer NOT NULL);

-- Input data on tables
INSERT INTO public.clients
(id, name) 
VALUES 
('6078', 'Ana'), 
('5819', 'Rui'), 
('4526', 'Nuno'), 
('3955', 'Rita'), 
('9999', 'José'); 

INSERT INTO public.personal_trainers
(id, name) 
VALUES 
('9876', 'Luís'), 
('1234', 'Joana');

INSERT INTO public.sports 
(code, description) 
VALUES 
('KB', 'Kickbox'), 
('NT', 'Natação'), 
('AE', 'Aerobica'); 

INSERT INTO public.clients_subs 
(id, code, payment) 
VALUES ('6078', 'AE', '25'), 
('5819', 'KB','30'),
 ('4526', 'KB','30'), 
('4526', 'NT','20'), 
('3955', 'KB','30'), 
('3955', 'NT','20'), 
('3955', 'AE','25'); 
--('9876', 'KB','0'); 

INSERT INTO public.pts_work
(id, code, salary) 
VALUES 
('1234', 'KB', '40'),
('1234', 'NT','30'), 
('9876', 'NT','30'), 
('9876', 'AE','35');