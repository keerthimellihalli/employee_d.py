def employee_details(name, emp_id, department, salary):
    return {
        "employee_name": name,
        "employee_id": emp_id,
        "department": department,
        "salary": salary
    }

if __name__ == "__main__":
    # Sample input (indented inside main)
    name = "John Doe"
    empl_id = "E12345"
    department = "Engineering"
    salary = 75000

    details = employee_details(name, empl_id, department, salary)
    print(details)
