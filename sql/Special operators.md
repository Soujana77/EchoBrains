# **Special operators :**

#### **IN is a special operator , instead of using multiple or we can use the IN operator.**

#### 

**example: without using IN**

SELECT \* FROM employees 

WHERE name ='Divya' OR name = 'Arun';



**Using IN**

SELECT \* FROM employees 

WHERE name IN ('Divya','Arun'); 



**Query 1 : WAQTD employees name  whose ages are 10,30,49,32**

SELECT name FROM employees 

WHERE age IN(10,30,49,32); 



**Query 2 : WAQTD employees whose experience between 5 to 15 years and working in Chennai and banglore location**

SELECT \* FROM employees 

WHERE exp between 5 and 15 AND city IN('Banglore','Chennai');



#### 

#### **Pattern Matching :**

##### **Like Operator is used to filter records on pattern matching.**

**% -> one or more characters**

**\_ -> exactly one character** 



**Syntax:**

SELECT \* FROM TABLE\_NAME 

WHERE colName  LIKE '\_%';



**Query 1 : WAQTD employees whose name starts with 'a'**

SELECT \* FROM employees

WHERE name LIKE 'a%'; 



**Query 2 : WAQTD employees whose name has exactly 4 characters**

SELECT \*FROM employees 

WHERE name LIKE '\_\_\_\_';



**Query 3 : employees who is hanving 'h' in their name** 

SELECT \* FROM employees

WHERE name LIKE '%h%';



**Query 4 :WAQTD Whose name contains h at the 3rd position** 

SELECT \* FROM employees 

WHERE name LIKE '\_\_h%';

#### 

#### **IS NULL and IS NOT NULL OPERATORS:**

**Used to filter records** 

SELECT \* FROM employees 

WHERE joining\_date IS NULL;

















