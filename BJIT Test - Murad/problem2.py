class Customer:
    def __init__(self):
        self.name = self.name
        self.address = self.address
        self.mobile = self.mobile
        self.website = self.website
        self.email = self.email
        self.fax = self.fax
        self.language = self.language

class Customer_Contact(Customer):
    def __init__(self,contact_name,title,job_position,email,phone,mobile,notes):
        #for ttiel we need to deploy a list to select the actual tittle
        title = ["Doctor", "Madam","Miss","Mister","Professor"]
        self.contact_name = contact_name
        self.title = title
        self.job_position = job_position
        self.email = email
        self.phone = phone
        self.mobile = mobile
        self.notes = notes



class Components_Buyer(Customer):
    def __init__(self):
        pass

class Consultancy_service(Customer):
    def __init__(self):
        pass
class Distributor(Customer):
    def __init__(self):
        pass

class Employee(Customer):
    def __init__(self):
        pass

class Manufacturer(Customer):
    def __init__(self):
        pass
class office_supplies(Customer):
    def __init__(self):
        pass





