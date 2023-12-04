class Employee:
    def __init__(self,ID,fname, lname, phone, email):
        self.ID = ID
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email

    def __str__(self):
            return f"ID: {self.ID} Name: {self.fname} {self.lname} Phone: {self.phone} Email: {self.email}"

class EmployeeCRUD:
     def __init__(self):
          self.emplyees = []

     def create_Employee(self,ID,fname, lname, phone, email):
          new_employee = Employee(ID,fname, lname, phone,email)
          self.emplyees.append(new_employee)

          return new_employee
     
     def read_Employee(self, ID=None, fname=None, lname=None, phone=None, email=None):
        for employee in self.emplyees:
             
            if(ID is None or employee.fname == fname) and \
            
     
     
    