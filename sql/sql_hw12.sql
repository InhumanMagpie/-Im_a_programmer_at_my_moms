CREATE TABLE students
(
    id          int NOT NULL PRIMARY KEY,
    first_name  varchar(20),
    second_name varchar(20)
);

INSERT INTO students (first_name, second_name) VALUES ('Vasilii', 'Boba');
INSERT INTO students (first_name, second_name) VALUES ('Andrei', 'Biba');
INSERT INTO students (first_name, second_name) VALUES ('Dmitrii', 'Pupsen');
INSERT INTO students (first_name, second_name) VALUES ('Aleksandr', 'Vupsen');

CREATE TABLE classrooms
(
    id int NOT NULL PRIMARY KEY,
    number varchar(6)
);

INSERT INTO classrooms (number) VALUES ('125');
INSERT INTO classrooms (number) VALUES ('574');
INSERT INTO classrooms (number) VALUES ('420');
INSERT INTO classrooms (number) VALUES ('969');

select id from classrooms
where number = '969';

select first_name, second_name from students
where where_is = (select id from classrooms
where number = '969');

select first_name, second_name from students
JOIN classrooms ON classrooms.id = students.where_is
where classrooms.number = '969'
