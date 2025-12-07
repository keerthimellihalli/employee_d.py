# test_employee_d.py

from employee import Employee_details

def test_employee_details():
    expected = {
        "employee_name": "John Doe",
        "employee_id": "E12345",
        "department": "Engineering",
        "salary": 75000
    }
    
    assert Employee_details("John Doe", "E12345", "Engineering", 75000) == expected
