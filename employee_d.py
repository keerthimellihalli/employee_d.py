# Function definition
def employee_details(name, emp_id, department, salary):
    return {
        "employee_name": name,
        "employee_id": emp_id,
        "department": department,
        "salary": salary
    }

# Run only when this file is executed directly
if __name__ == "__main__":
    # Sample input
    name = "John Doe"
    emp_id = "E12345"
    department = "Engineering"
    salary = 75000

    # Get the details dictionary
    details = employee_details(name, emp_id, department, salary)

    # Combine all fields into one string with \n
    output = (
        f"employee_name: {details['employee_name']}\n"
        f"employee_id: {details['employee_id']}\n"
        f"department: {details['department']}\n"
        f"salary: {details['salary']}"
    )

    # Print the final output
    print(output)
