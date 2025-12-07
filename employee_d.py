def Employee_details(name, empl_id, department, salary):
    result = {
        "employee_name": name,
        "employee_id": empl_id,
        "department": department,
        "salary": salary
    }
    return result


if __name__ == "__main__":
    # sample input (you can change)
    name = "John Doe"
    empl_id = "E12345"
    department = "Engineering"
    salary = 75000
    
    details = Employee_details(name, empl_id, department, salary)
    print(details)
