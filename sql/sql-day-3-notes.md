

# DATATYPE:

## 1.NUMERIC TYPES

TINYINT        - 

SMALLINT

MEDIUMINT

INT 

BIGINT

DECIMAL

FLOAT

DOUBLE



## 2.CHARACTER TYPES

CHAR           

VARCAHRA

TEXT

LONGTEXT

## 

## 3.DATE

DATE    - Calander  - '2026-08-05'

TIME    - time of day - '14:30:00'

DATETIME-Date and time -'

TIMESTAMP

YEAR

BOOLEAN

BLOB

LONGBLOB

#### 

#### RENAME TABLE OLD\_T\_N TO NEW\_T\_N;

eg:  rename table Employees to emp;

#### 

#### CREATE TABLE table\_name(columnName datatype,columnName datatype);

eg:CREATE TABLE Employees(

&#x20;   emp\_ID INT,

&#x20;   age TINYINT,

&#x20;   dob DATE,

&#x20;   salary DECIMAL(10,2),

&#x20;   gender CHAR(1),

&#x20;   address TEXT,

&#x20;   login\_time TIME,

&#x20;   last\_time DATETIME,

&#x20;   active BOOLEAN,

&#x20;   emailID VARCHAR(50),

&#x20;   mobileNumber VARCHAR(15)

);

#### 

#### DROP TABLE table\_name;

DROP TABLE emp;



ALTER is used to 

create new column in existing table:



ALETR TABLE table\_name

ADD column datatype;

&#x20;eg:ALTER TABLE EMP 

&#x20;    add bonus decimal(5,2)









