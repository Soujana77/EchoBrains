# **Forms**

###### 1\. What is an HTML Form?

###### 

###### An HTML form is used to collect information from users and send that information to a server for processing.

###### 

###### Examples:



* Login forms
* Registration forms
* Contact forms
* Feedback forms
* Search forms
* Online application forms



###### The main element used to create a form is the <form> tag.

###### 

###### **Basic syntax**

**<form action="server-url" method="post">**

&#x20;   **<!-- form elements -->**

**</form>**



###### **2. Important Attributes of <form>**

###### **action**



###### Specifies where the form data should be sent.

###### 

###### **<form action="process.php">**



###### Here, the data is sent to process.php.

###### 

###### method

###### 

###### Specifies how the data should be sent.

###### 

###### There are two commonly used methods:

###### 

###### GET

###### **<form method="get">**

###### Data is appended to the URL.

###### Suitable for search forms.

###### Data is visible in the browser URL.

###### Not suitable for sensitive information.

###### 

###### Example:

###### 

###### **search.php?name=Soujanya**

###### **POST**

###### **<form method="post">**

###### Data is sent in the HTTP request body.

###### Data doesn't appear in the URL.

###### Commonly used for login, registration, and other forms that submit data.

###### 

###### 3\. <input> Element

###### 

###### The <input> tag is used to create different types of input fields.

###### 

###### Text

###### <input type="text">

###### 

###### Used for names, usernames, etc.

###### 

###### Password

###### <input type="password">

###### 

###### Hides the characters entered by the user.

###### 

###### Email

###### <input type="email">

###### 

###### Used for email addresses and provides basic browser validation.

###### 

###### Number

###### <input type="number">

###### 

###### Used for numerical values.

###### 

###### Radio Button

###### <input type="radio" name="gender" value="male">

###### 

###### Used when the user should select one option from a group.

###### 

###### Example:

###### 

###### <input type="radio" name="gender" value="male"> Male

###### <input type="radio" name="gender" value="female"> Female

###### 

###### The same name makes them part of the same group.

###### 

###### Checkbox

###### <input type="checkbox" name="skills" value="python">

###### 

###### Used when the user can select multiple options.

###### 

###### Date

###### <input type="date">

###### 

###### Allows the user to select a date.

###### 

###### File

###### <input type="file">

###### 

###### Allows the user to upload a file.

###### 

###### Submit

###### <input type="submit" value="Submit">

###### 

###### Submits the form.

###### 

###### Reset

###### <input type="reset" value="Reset">

###### 

###### Resets the form fields to their initial values.

###### 

###### **4. <label> Element**

###### 

###### <label> gives a description to an input field.

###### 

###### <label for="name">Name:</label>

###### <input type="text" id="name">

###### 

###### The for attribute of <label> should match the id of the input.

###### 

###### This improves accessibility and usability.

###### 

###### 

###### **5. name Attribute**

###### 

###### The name attribute identifies the data when the form is submitted.

###### 

###### <input type="text" name="username">

###### 

###### For example, with:

###### 

###### <input type="text" name="username" value="Soujanya">

###### 

###### the submitted data contains something like:

###### 

###### username=Soujanya

###### 

###### Important: id is mainly used for identifying an element in the page, while name is important for submitting form data.

###### 

###### **6. value Attribute**

###### 

###### Specifies the initial/current value of an input.

###### 

###### <input type="text" name="city" value="Bangalore">

###### 

###### **7. placeholder**

###### 

###### Displays a hint inside an input field.

###### 

###### <input type="text" placeholder="Enter your name">

###### 

###### Example:

###### 

###### | Enter your name        |

###### 

###### The placeholder disappears when the user starts typing.

###### 

###### **8. required**

###### 

###### Makes an input field mandatory.

###### 

###### <input type="email" required>

###### 

###### The user cannot submit the form without filling it.

###### 

###### **9. <textarea>**

###### 

###### Used for multi-line text.

###### 

###### <textarea name="message" rows="5" cols="30"></textarea>

###### 

###### Useful for:

###### 

###### Comments

###### Feedback

###### Address

###### Messages

###### 

###### **10. <select> and <option>**

###### 

###### Used to create a dropdown list.

###### 

###### <select name="course">

###### &#x20;   <option value="cse">CSE</option>

###### &#x20;   <option value="ise">ISE</option>

###### &#x20;   <option value="ece">ECE</option>

###### </select>

###### 

###### The user can select one option.

###### 

###### **11. <button>**

###### 

###### Creates a button.

###### 

###### <button type="submit">Submit</button>

###### 

###### Common button types:

###### 

###### <button type="submit">Submit</button>

###### <button type="reset">Reset</button>

###### <button type="button">Click Me</button>

###### 12\. Important Input Types

###### Input Type	Purpose

###### text	Single-line text

###### password	Password

###### email	Email address

###### number	Numbers

###### radio	Select one option

###### checkbox	Select multiple options

###### date	Select date

###### time	Select time

###### file	Upload file

###### url	Website URL

###### tel	Phone number

###### color	Select color

###### range	Select a value within a range

###### submit	Submit form

###### reset	Reset form

###### 13\. Useful Form Attributes

###### required

###### <input type="text" required>

###### 

###### Field must be filled.

###### 

###### readonly

###### <input type="text" value="CSE" readonly>

###### 

###### User can see the value but cannot modify it.

###### 

###### disabled

###### <input type="text" disabled>

###### 

###### The input cannot be used.

###### 

###### min and max

###### <input type="number" min="18" max="60">

###### 

###### Restricts the numerical range.

###### 

###### maxlength

###### <input type="text" maxlength="20">

###### 

###### Limits the number of characters.

