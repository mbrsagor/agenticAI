from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional


class EmployeeData(BaseModel):
    name: str = Field(max_length=50)
    age: Optional[int] = 0
    email: EmailStr
    salary: float
    is_active: bool
    stacks: List[str]
    contact_info: Dict[str, str]


def add_employee_data(employee: EmployeeData):
    print(employee.name)
    print(employee.age)
    print(employee.salary)
    print("Data successfully added to the database")


def update_employee_data(employee: EmployeeData):
    print(employee.name)
    print(employee.age)
    print("Data successfully updated to the database")


employee_data = {
    "name": "Mbr Sagor", "age": 30, "salary": 14.00, 
    "email": "sagor@gmail.com",
    "is_active": True, "stacks": ["Python", "Javascript"], 
    "contact_info": {"phone": "0121223", "address": "Dhaka"}
}
employee = EmployeeData(**employee_data)

add_employee_data(employee)
