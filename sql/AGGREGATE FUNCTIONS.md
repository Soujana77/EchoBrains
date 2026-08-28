### **AGGREGATE FUNCTIONS:**



###### **This is used to perform the calculations on the multiple records and gives the result as a single value.**



**COUNT()->It is used to count the records in the table.**

**SUM()  ->It is used to find the total of a column**

**AVG()  -> It is used to find the average of the give column**

**MAX()  ->It is used to find the maximum value from the column**

**MIN()  -> It is used to find the minimum value from the column**

##### 

##### **COUNT():**

**Used to count the number of records in a table.**



###### **SYNTAX**

**SELECT aggregate\_function\_name(col)**

**FROM TABLE\_NAME;**



**---------------------------------------------------------**

**Query 1: WAQTD the number of employees in the table .**



&#x09;**SELECT COUNT(\*)**

&#x09;**FROM employees;**



**Query 2: WAQTD the number of employees working in finance department**

&#x20;	

&#x09;**SELECT COUNT(\*)**

&#x09;**FROM employees** 

&#x09;**WHERE dept="Finance";**



**Query 3: WAQTD the total salary of all the employees**

&#x09;

&#x09;**SELECT SUM(salary)**

&#x09;**FROM employees;**



**Query 4: WAQTD the average salary of the employees**

&#x20;

&#x09;**SELECT AVG(salary)**

&#x09;**FROM employees;**



**Query 5: WAQTD the maximum salary from the employees**

&#x20;	

&#x09;**SELECT MAX(salary)**

&#x09;**FROM employees;**



**Query 6: WAQTD the minimum salary from the employees**

&#x20;	

&#x09;**SELECT MIN(salary)**

&#x09;**FROM employees;**

&#x09;



**Note: COUNT(\*) gives all records counts irrespective of null values**

&#x20;     **COUNT(col) gives count of values present in the column and ignore the null values** 



**It is possible to perform all the functions in a single query:**

**SELECT COUNT(\*),AVG(salary),SUM(salary),MIN(bonus),MAX(bonus)**

**FROM employees** 



**Query 7: WAQTD the highest salary lowest salary of the employees** 



&#x09;**SELECT MAX(salary),MIN(salary)**

&#x20;       **FROM employees;**



**Query 8: WAQTD the max total salary of the employee** 



&#x09;**SELECT MAX** 



**Query 9: WAQTD the lowest salary in finance department**



&#x09;**SELECT MIN(salary)**

&#x09;**FROM employees**

&#x09;**WHERE dept="Finance";**



**Query 10: WAQTD the lowest salary of the employee whose experience is greater than 5 years** 



&#x09;**SELECT MIN(experience)**

&#x09;**FROM employees**

&#x09;



**Query 11: WAQTD the number of employees working in sales**



&#x09;**SELECT COUNT(department)**

&#x09;**FROM employees**

&#x09;**WHERE dept="Sales";**


**Query 12: WAQTD the average salary of IT department**



&#x09;**SELECT AVG(salary)**

&#x09;**FROM employees**

&#x09;**WHERE dept="IT";**



**Query 13: WAQTD the average annual salary of employees who is department name starts with d and experience is greater than 20 years** 



&#x09;**SELECT AVG(salary) AS average\_annual\_salary**

&#x09;**FROM employees**

&#x09;**WHERE dept LIKE 'D%'**

&#x09;**AND exp > 20;**









