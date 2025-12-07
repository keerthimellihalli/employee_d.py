def employee_details(name, emp_id, department, salary):
    return {
        "employee_name": name,
        "employee_id": emp_id,
        "department": department,
        "salary": (salary),
    }

if __name__ == "__main__":
    # Sample input
    {
  'employee_name': 'John Doe\n',
  'employee_id': 'E12345\n',
  'department': 'Engineering\n',
  'salary': '75000\n'
}


    details = employee_details(name, empl_id, department, salary)
    print(details)

