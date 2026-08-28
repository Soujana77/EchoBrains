### **7. Universal Selector**



\* **{**

&#x20;   **margin: 0;**

&#x20;   **padding: 0;**

**}**



\* selects everything.



You'll commonly see this in CSS resets.



### **8. Grouping Selectors**

### 

Suppose you want the same style for h1, h2, and p.



Instead of:



**h1 {**

&#x20;   **color: blue;**

**}**



**h2 {**

&#x20;   **color: blue;**

**}**



**p {**

&#x20;   **color: blue;**

**}**



You can write:



**h1, h2, p {**

&#x20;   **color: blue;**

**}**



**}**

#### **9. Colors**



CSS provides several ways to specify colors.



Color Name

**h1 {**

&#x20;   **color: red;**

**}**

HEX

**h1 {**

&#x20;   **color: #ff0000;**

**}**

RGB

**h1 {**

&#x20;   **color: rgb(255, 0, 0);**

**}**

RGBA



RGBA adds transparency.



**h1 {**

&#x20;   **color: rgba(255, 0, 0, 0.5);**

**}**



0.5 = 50% opacity**.**

