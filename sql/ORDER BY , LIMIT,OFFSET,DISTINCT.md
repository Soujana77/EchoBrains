# **ORDER BY , LIMIT,OFFSET,DISTINCT,IN SQL**

##### 

##### **1.ORDER BY** 

**Order By is used to sort the result of a query** 

**By default , SQL sorts in ascending order(ASC).**

**It can store data in :**

* **Ascending order -> ASC**
* **Descending order -> DESC**



###### **Syntax:**

**SELECT column1 , column2**

**FROM table\_name**

**ORder BY column\_name ASC;**



###### **or**



**SELECT column1, column2**

**FROM table\_name**

**ORDER BY column\_name DESC;**



###### **Example 1: Sort employees by salary**

###### **Ascending order** 



**SELECT \***

**FROM employees** 

**ORDER BY salary ASC;**





###### **Descending order** 

**SELECT \***

**FROM employees**

**ORDER BY salary DESC;**





###### **Example 2: Sort age** 

**SELECT name, age**

**FROM employees**

**ORDER BY age ASC;**



**SELECT name, age**

**FROM employees**

**ORDER BY age DESC;**



**ORDER BY Multiple columns :**

**You can sort using more than one column** 



###### **Example :**

**SELECT \***

**FROM employees**

**ORDER BY dept ASC,salary DESC;**





###### **Important :**

**The first column has the highest priority.**

**ORDER BY dept ASC ,salary DESC**





**LIMIT:**

**Limit is used to restrict the number of rows returned by the query.**



**SYNTAX:**

**SELECT \***

**FROM table\_name** 

**LIMIT number;**



**EXAMPLE :**

**SELECT \***

**FROM employees**

**LIMIT 5;**



**this returns only the first 5 records from the result**





**LIMIT with ORDER BY**

**This combination is extremely useful.**

**top 3 highest-paid employees.**



**SELECT \***

**FROM employees**

**ORDER BY salary DESC**

**LIMIT 3;**



**Example: 5 youngest employees**

**SELECT \***

**FROM employees**

**ORDER BY age ASC**

**LIMIT 5;**



**Example: 3 employees with the highest bonus**

**SELECT \***

**FROM employees**

**ORDER BY bonus DESC**

**LIMIT 3;**



