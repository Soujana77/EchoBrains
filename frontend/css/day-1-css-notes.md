# **CSS-Cascading Style Sheet**

**HTML creates the structure/content of a webpage, while CSS controls its appearance and layout.**



**For example:**



HTML:



<h1>Hello World</h1>

<p>Welcome to my website</p>



**Without CSS, it looks very plain.**



**CSS can change:**



Color

Font

Size

Background

Spacing

Borders

Alignment

Position

Layout

Responsiveness

Animations



#### **DAY 1 — CSS Fundamentals**



##### **1.Basic CSS Syntax**

**selector{**

&#x09;**property:value;**

**}**



**h1 {**

&#x09;**color:blue;**

&#x09;**font-size:40px;**

**}**



**Here:**



**h1 → selector**

**color → property**

**blue → value**

**font-size → property**

**40px → value**





#### **2. Three Ways to Add CSS**



##### **A. Inline CSS**



###### **CSS directly inside an HTML element.**



**<h1 style="color: red;">Hello</h1>**



**Good for quick testing, but generally not recommended for larger websites.**



##### **B. Internal CSS**

###### **CSS is written inside <style>**



**<!DOCTYPE html>**

**<html>**

**<head>**



**<style>**

&#x20;   **h1 {**

&#x20;       **color: blue;**

&#x20;   **}**



&#x20;   **p {**

&#x20;       **color: green;**

&#x20;   **}**

**</style>**



**</head>**



**<body>**



**<h1>Hello</h1>**

**<p>Welcome</p>**



**</body>**

**</html>**



#### **C. External CSS ⭐** 



###### **CSS is placed in a separate .css file**



**index.html**

**<!DOCTYPE html>**

**<html>**

**<head>**

&#x20;   **<link rel="stylesheet" href="style.css">**

**</head>**



**<body>**



**<h1>Hello World</h1>**

**<p>Welcome to CSS</p>**



**</body>**

**</html>**

**------------------------------------------------------------**

**style.css**

**h1 {**

&#x20;   **color: blue;**

**}**



**p {**

&#x20;   **color: green;**

**}**





#### **3. CSS Comments**



**Comments are ignored by the browser.**



**/\* This is a CSS comment \*/**



**h1 {**

&#x20;   **color: red;**

**}**



#### **4. CSS Selectors**



**Selectors tell CSS which HTML elements should be styled.**



**There are several important selectors.**



##### **A. Element Selector**



**Selects all elements of a particular type.**



**p {**

&#x20;   **color: red;**

**}**



**This affects every <p>.**



**<p>One</p>**

**<p>Two</p>**

**<p>Three</p>**



**All three become red.**



#### **5. Class Selector ⭐**



**A class can be given to HTML elements.**



**<p class="important">Hello</p>**

**<p>Normal paragraph</p>**



**CSS:**



**.important {**

&#x20;   **color: red;**

**}**



**Notice:**



**.important**



**The . means class.**



**Multiple elements can have the same class:**



**<p class="important">Hello</p>**

**<h2 class="important">Welcome</h2>**



**Both receive the style.**



#### **6. ID Selector**



**<h1 id="title">My Website</h1>**



**CSS:**



**#title {**

&#x20;   **color: purple;**

**}**



**# means ID.**



**Generally:**



**class → reusable**

**id → identifies one particular element**

