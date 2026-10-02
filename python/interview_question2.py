employees = [
    {"id": 101, "name": "Arun", "department": "IT", "salary": 45000},
    {"id": 102, "name": "Priya", "department": "HR", "salary": 38000},
    {"id": 103, "name": "Rahul", "department": "IT", "salary": 52000},
    {"id": 104, "name": "Divya", "department": "Finance", "salary": 48000},
    {"id": 105, "name": "Karthik", "department": "IT", "salary": 60000}
]

def display_employee_details(employee):
    print(employee["id"], employee["name"], employee["department"], employee["salary"])

for employee in employees:
    display_employee_details(employee)

def emp_highest_salary(employees):
    highest_salary = 0     

    highest_salary_employee = None
    for employee in employees:
        if employee["salary"] > highest_salary:
            highest_salary = employee["salary"]
            highest_salary_employee = employee