name=input("Enter your name:")
Roll_number=input("Enter your roll number:")
python=float(input("Enter the marks of python:"))
SQL=float(input("Enter the marks of SQL:"))
Java=float(input("Enter the marks of Java:"))
HTML=float(input("Enter the marks of HTML:"))
CSS=float(input("Enter the marks of CSS:"))
total_marks=python+SQL+Java+HTML+CSS
percentage=(total_marks/500)*100
Average=total_marks/5

print("Name:",name)
print("Roll number:",Roll_number)
print("Python:",python)
print("SQL:",SQL)
print("Java:",Java)
print("HTML:",HTML)
print("CSS:",CSS)
print("Total marks:",total_marks)
print("Percentage:",percentage)
print("Average:",Average)   


if percentage > 90 and percentage < 100:
    print("Grade A")
elif percentage > 80 and percentage < 89:
    print("Grade B")
elif percentage > 70 and percentage < 79:
    print("Grade C")
elif percentage > 60 and percentage < 69:
    print("Grade D")
elif percentage < 60 and percentage > 0:
    print("Grade E")
else:
    print("Invalid input")       


if python >=40 and SQL >=40 and Java >=40 and HTML >=40 and CSS >=40:
    print("Result: Pass")
else:
    print("Result: Fail")
