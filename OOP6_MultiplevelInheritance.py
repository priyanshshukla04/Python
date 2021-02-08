##################EXAMPLE_1###############
class Dad:
    age = 60
    basketball = 2
    def printdetails(self):
        return f"Dad loves to play and eat"


class Son(Dad):
    age = 28
    def printdetails(self):
        return f"Son loves to play, sleep and read"


class Grandson(Son):
    age = 7

def printdetails(self):
        return f"Grandson is good at badminton and politics"


a = Dad()
b = Son()
c = Grandson()
print(a.age)
print(b.printdetails())
print(c.basketball)

############EXAMPLE_2######################
# electronic device
# pocket gadget
# phone
class Electronic_device:
    no_of_devices = 4
    def print_details(self):
        return f"Electronic devices. {self.no_of_devices}"

class Pocket_gadge(Electronic_device):
    no_of_devices = 10
    def print_details(self):
        return f"No of devices. {self.no_of_devices}"

class Phone(Electronic_device, Pocket_gadge):
    no_of_devices = 12
    def print_details(self):
        return f"No of phones. {self.no_of_devices}"

a = Electronic_device()
b = Pocket_gadge()
c = Phone()
print(a.print_details())
print(b.print_details())