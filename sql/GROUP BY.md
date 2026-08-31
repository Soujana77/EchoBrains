### **GROUP BY :**

* It is used to create groups based on the column values 
* always comes after where/from 

**Syntax**

&#x20;	SELECT g\_colName , AGGREGATE\_func(\*)

&#x09;FROM table\_name

&#x09;GROUP BY g\_colName 



**Query 14: WAQTD the number of employees working in each department** 



**SELECT dept , count(\*)**

**FROM employees** 

**GROUP BY dept ;** 



**Note: GROUP BY works only with aggregate functions**



**Query 1: WAQTD the employees working in each department** 

&#x09; **SELECT  dept , COUNT(\*)**

&#x09; **FROM employees**

&#x09; **GROUP BY dept;**



**Query 2: WAQTD the average salary , total salary , number of employees and maximum salary , minimum salary in each city** 

&#x09;**SELECT city, AVG(bonus+salary), MIN(salary),MAX(salary) COUNT(\*)**

&#x09;**FROM employees**

&#x09;**GROUP BY city;**



**Query 3: WAQTD the  ORDER BY** 

&#x09;**SELECT city, AVG(bonus+salary), MIN(salary),MAX(salary), COUNT(\*)**

&#x09;**FROM employees**

&#x09;**GROUP BY city**

&#x09;**ORDER BY city;**



&#x20;

**Query 4: WAQTD the ORDER BY employees count**

&#x20;       **SELECT city , AVG(bonus+salary),MIN(salary),MIN(salary),COUNT(\*)**

&#x09;**FROM employees** 



**Query 4: WAQTD the average salary of employees working each city and whose experience is greater than 6 years** 

&#x09;**SELECT city, AVG(salary)**

&#x09;**FROM employees** 

&#x09;**WHERE exp>6** 

&#x09;**GROUP BY city;** 

&#x09;

Query 5: WAQTD the 
