# SE L2T11 - Working with SQL

1. SQL code to create the Student table:

CREATE TABLE Student (
STU_NUM CHAR(6) PRIMARY KEY,
STU_SNAME VARCHAR(15),
STU_FNAME VARCHAR(15),
STU_INITIAL CHAR(1),
STU_STARTDATE DATE,
COURSE_CODE CHAR(3),
PROJ_NUM INT(2)
);

2. SQL code to insert the first two rows into the Student table:

INSERT INTO Student (STU_NUM, STU_SNAME, STU_FNAME, STU_INITIAL, STU_STARTDATE, COURSE_CODE, PROJ_NUM)
VALUES
('01', 'Snow', 'John', 'E', '2014-04-05', '201', '6'),
('02', 'Stark', 'Arya', 'C', '2017-07-12', '305', '11');

3. SQL code to list all attributes for a COURSE_CODE of 305:

STU_NUM  STU_SNAME  STU_FNAME  STU_INITIAL  STU_STARTDATE  COURSE_CODE  PROJ_NUM

02       Stark      Arya       C           2017-07-12     305          11
06       Tyrell     Margaery   Y           2017-07-12     305          10

4. SQL code to change the course code to 304 for the person whose student number is 07:

UPDATE Student
SET COURSE_CODE = '304'
WHERE STU_NUM = '07';

5. SQL code to delete the row of the person named Jamie Lannister, who started on 5 September 2012, whose course code is 101 and project number is 2:

DELETE FROM Student
WHERE STU_SNAME = 'Lannister'
AND STU_FNAME = 'Jamie'
AND STU_STARTDATE = '2012-09-05'
AND COURSE_CODE = '101'
AND PROJ_NUM = '2';

6. SQL code that will change the PROJ_NUM to 14 for all those students who started before 1 January 2016 and whose course code is at least 201:

UPDATE Student
SET PROJ_NUM = '14'
WHERE STU_STARTDATE < '2016-01-01'
AND COURSE_CODE >= '201';

7. SQL code that will delete all of the data inside a table, but not the table itself:

DELETE FROM Student;

8. SQL code that will delete the Student table entirely:

DROP TABLE Student;