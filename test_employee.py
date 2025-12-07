from employee_d import Employee_details

def test_employee_details():
    expected = {
        "employee_name": "John Doe"\n
        "employee_id": "E12345"\n
        "department": "Engineering"\n
        "salary": 75000
    }
    
    assert Employee_details("John Doe", "E12345", "Engineering", 75000) == expected output
