details = employee_details("John Doe", "E12345", "Engineering", 75000)

# Option 1: Using a loop
for key, value in details.items():
    print(f"{key}: {value}")  # Each print already adds a newline automatically

# Option 2: Using a single print with \n
output = (
    f"employee_name: {details['employee_name']}\n"
    f"employee_id: {details['employee_id']}\n"
    f"department: {details['department']}\n"
    f"salary: {details['salary']}"
)
print(output)
