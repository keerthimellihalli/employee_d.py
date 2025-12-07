def employee_details(name, emp_id, department, salary):
    return {
        "employee_name": name\n
        "employee_id": emp_id\n
        "department": department\n
        "salary": salary
    }

    return result


if __name__ == "__main__":
    # sample input (you can change)
    name = "John Doe"
    empl_id = "E12345"
    department = "Engineering"
    salary = 75000
    
    details = employee_details(name, empl_id, department, salary)
    print(details)
