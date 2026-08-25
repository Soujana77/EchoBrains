# **# LOGICAL OPERATORS IN SQL**



##### Logical operators in SQL are used to \*\*combine multiple conditions\*\* in a SQL query.



They are mainly used with the `WHERE` clause to filter records.



The main logical operators are:



1\. `AND`

2\. `OR`

3\. `NOT`



We will use our `employees` table for the examples.



```sql

SELECT \* FROM employees;

```



Our table contains columns such as:



```text

name

age

salary

exp

dept

city

joining\_date

bonus

```



\---



###### **# 1. AND OPERATOR**



The `AND` operator is used when \*\*ALL conditions must be TRUE\*\*.



\### Syntax



```sql

SELECT column\_name

FROM table\_name

WHERE condition1 AND condition2;

```



\### Example



```sql

SELECT \*

FROM employees

WHERE age > 25 AND salary > 70000;

```



This returns employees whose:



\* age is greater than 25

\* AND salary is greater than 70,000



Both conditions must be satisfied.



\### Example with department and city



```sql

SELECT \*

FROM employees

WHERE dept = 'IT' AND city = 'Bangalore';

```



This returns employees who work in the \*\*IT department AND are located in Bangalore\*\*.



\### Important



If an employee satisfies only one condition, they will NOT be selected.



For example:



```text

age = 28       → TRUE

salary = 60000 → FALSE

```



Since:



```text

TRUE AND FALSE = FALSE

```



the employee will not appear in the result.



\---



###### **# 2. OR OPERATOR**



The `OR` operator is used when \*\*at least one condition must be TRUE\*\*.



\### Syntax



```sql

SELECT column\_name

FROM table\_name

WHERE condition1 OR condition2;

```



\### Example



```sql

SELECT \*

FROM employees

WHERE city = 'Bangalore' OR city = 'Mumbai';

```



This returns employees who are:



\* from Bangalore

\* OR from Mumbai



Only one condition needs to be true.



\### Example



```sql

SELECT \*

FROM employees

WHERE dept = 'IT' OR salary > 90000;

```



This returns employees who:



\* work in IT



OR



\* have a salary greater than 90,000



An employee can satisfy either one or both conditions.



\### Truth idea



```text

TRUE OR TRUE   = TRUE

TRUE OR FALSE  = TRUE

FALSE OR TRUE  = TRUE

FALSE OR FALSE = FALSE

```



\---



###### **# 3. NOT OPERATOR**



The `NOT` operator is used to \*\*reverse the result of a condition\*\*.



In simple words:



```text

NOT TRUE  → FALSE

NOT FALSE → TRUE

```



\### Syntax



```sql

SELECT column\_name

FROM table\_name

WHERE NOT condition;

```



\### Example



```sql

SELECT \*

FROM employees

WHERE NOT dept = 'IT';

```



This returns all employees who are \*\*not\*\* in the IT department.



Another way of writing this is:



```sql

SELECT \*

FROM employees

WHERE dept <> 'IT';

```



Here `<>` means \*\*not equal to\*\*.



\---



###### **# USING AND, OR, AND NOT TOGETHER**



We can combine multiple logical operators.



\### Example



```sql

SELECT \*

FROM employees

WHERE dept = 'IT'

AND salary > 60000

AND city = 'Bangalore';

```



All three conditions must be TRUE:



```text

Department = IT

AND

Salary > 60000

AND

City = Bangalore

```



\---



###### **# USING OR WITH MULTIPLE CONDITIONS**



```sql

SELECT \*

FROM employees

WHERE city = 'Bangalore'

OR city = 'Mumbai'

OR city = 'Chennai';

```



This selects employees from any of these three cities.



However, there is a shorter way to write this:



```sql

SELECT \*

FROM employees

WHERE city IN ('Bangalore', 'Mumbai', 'Chennai');

```



\---



###### **# COMBINING AND AND OR**



This is very important in SQL.



Example:



```sql

SELECT \*

FROM employees

WHERE dept = 'IT'

AND salary > 70000

OR city = 'Mumbai';

```



SQL evaluates logical expressions according to operator precedence, so when mixing `AND` and `OR`, it is best to use \*\*parentheses\*\* to make your intention clear.



For example:



```sql

SELECT \*

FROM employees

WHERE (dept = 'IT' AND salary > 70000)

OR city = 'Mumbai';

```



This means:



```text

Employees who:

&#x20;   (work in IT AND earn more than 70000)

OR

&#x20;   work in Mumbai

```



\---



###### **# USING NOT WITH AND**

###### 

Example:



```sql

SELECT \*

FROM employees

WHERE NOT (dept = 'IT' AND city = 'Bangalore');

```



This excludes employees who satisfy \*\*both\*\* conditions:



```text

IT + Bangalore

```



\---



###### **# USING NOT WITH OR**



Example:



```sql

SELECT \*

FROM employees

WHERE NOT (city = 'Bangalore' OR city = 'Mumbai');

```



This returns employees who are \*\*neither from Bangalore nor Mumbai\*\*.



\---



###### **# LOGICAL OPERATORS WITH OTHER OPERATORS**



Logical operators are commonly combined with comparison operators.



Comparison operators include:



```text

=       Equal to

<>      Not equal to

!=      Not equal to

>       Greater than

<       Less than

>=      Greater than or equal to

<=      Less than or equal to

```



Example:



```sql

SELECT \*

FROM employees

WHERE age >= 25 AND salary <= 80000;

```



Here:



```text

age >= 25

```



is one condition, and:



```text

salary <= 80000

```



is another condition.



`AND` combines them.



\---



###### **# PRACTICAL EXAMPLES USING OUR EMPLOYEES TABLE**

###### 

###### \### Example 1: IT employees earning more than 60,000

###### 

```sql

SELECT name, salary, dept

FROM employees

WHERE dept = 'IT' AND salary > 60000;

```



###### \### Example 2: Employees from Bangalore or Chennai

###### 

```sql

SELECT name, city

FROM employees

WHERE city = 'Bangalore' OR city = 'Chennai';

```



###### \### Example 3: Employees not working in HR



```sql

SELECT name, dept

FROM employees

WHERE NOT dept = 'HR';

```



###### \### Example 4: Employees older than 25 with more than 3 years of experience



```sql

SELECT name, age, exp

FROM employees

WHERE age > 25 AND exp > 3;

```



###### \### Example 5: IT employees from Bangalore



```sql

SELECT name, dept, city

FROM employees

WHERE dept = 'IT' AND city = 'Bangalore';

```



###### \### Example 6: Employees from Bangalore with salary greater than 50,000 OR employees from Mumbai

###### 

```sql

SELECT \*

FROM employees

WHERE (city = 'Bangalore' AND salary > 50000)

OR city = 'Mumbai';

```



\---



###### **# TRUTH TABLE**



###### \## AND



Both conditions must be TRUE.



```text

Condition 1    Condition 2    Result

\-------------------------------------

TRUE           TRUE            TRUE

TRUE           FALSE           FALSE

FALSE          TRUE            FALSE

FALSE          FALSE           FALSE

```



###### \## OR



At least one condition must be TRUE.



```text

Condition 1    Condition 2    Result

\-------------------------------------

TRUE           TRUE            TRUE

TRUE           FALSE           TRUE

FALSE          TRUE            TRUE

FALSE          FALSE           FALSE

```



###### \## NOT



NOT reverses the result.



```text

Condition      NOT Condition

\----------------------------

TRUE           FALSE

FALSE          TRUE

```



\---



###### **# OPERATOR PRECEDENCE**



When multiple operators are used together, SQL follows an order of evaluation.



Generally:



```text

1\. NOT

2\. AND

3\. OR

```



For example:



```sql

WHERE A OR B AND C

```



is generally interpreted as:



```sql

WHERE A OR (B AND C)

```



NOT:



```sql

WHERE (A OR B) AND C

```



To avoid confusion, use parentheses:



```sql

WHERE (A OR B) AND C

```



or:



```sql

WHERE A OR (B AND C)

```



This makes the query much easier to understand.



\---





