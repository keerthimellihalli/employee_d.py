from employee import employee_details

def test_employee_details():
    expected = {
        "employee_name": "John Doe",
        "employee_id": "E12345",
        "department": "Engineering",
        "salary": 75000
    }

    result = employee_details("John Doe", "E12345", "Engineering", 75000)
    assert result == expected
