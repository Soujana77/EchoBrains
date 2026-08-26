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





#### **OFFSET** 

**OFFSET is used to skip a specific number of rows before returning the result** 



**Is is specifically useful for pagination .**



**SELECT \***

**FROM table\_name**

**LIMIT number**

**OFFSET number;**



**Example :**

**SELECT \*** 

**FROM employees** 

**LIMIT 5 OFFSET 2;**



###### **This means:**

###### 

###### **Skip the first 2 rows**

###### **Then return the next 5 rows**

###### 

**Imagine the sorted result is:**



**1. Soujanya**

**2. Rahul**

**3. Priya**

**4. Arun**

**5. Sneha**

**6. Vikram**

**7. Ananya**

**8. Karan**



**LIMIT 5 OFFSET 2**



**SQL skips:**



**1. Soujanya**

**2. Rahul**



**and returns:**



**3. Priya**

**4. Arun**

**5. Sneha**

**6. Vikram**

**7. Ananya**







**OFFSET WITH ORDER BY**



**Usually, OFFSET makes more sense when combined with ORDER BY.**



**Example:**



**SELECT \***

**FROM employees**

**ORDER BY salary DESC**

**LIMIT 3 OFFSET 3;**



**First, employees are sorted by salary:**



**1. Highest salary**

**2. 2nd highest**

**3. 3rd highest**

**4. 4th highest**

**5. 5th highest**

**6. 6th highest**

**...**



**Then:**



**OFFSET 3**



**skips the first 3.**



**Then:**



**LIMIT 3**



**returns the next 3.**



**So this gives you the:**



**4th highest**

**5th highest**

**6th highest**

**OFFSET AND PAGINATION**



**This is one of the most common real-world uses of LIMIT and OFFSET.**



**Suppose a website displays 10 employees per page.**



**Page 1**

**SELECT \***

**FROM employees**

**LIMIT 10 OFFSET 0;**



**Returns:**



**Rows 1–10**

**Page 2**

**SELECT \***

**FROM employees**

**LIMIT 10 OFFSET 10;**



**Returns:**



**Rows 11–20**

**Page 3**

**SELECT \***

**FROM employees**

**LIMIT 10 OFFSET 20;**



**Returns:**



**Rows 21–30**



**The formula is:**



**OFFSET = (page\_number - 1) × number\_of\_rows\_per\_page**



**For 10 records per page:**



**Page 1 → OFFSET 0**

**Page 2 → OFFSET 10**

**Page 3 → OFFSET 20**

**Page 4 → OFFSET 30**

