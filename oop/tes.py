class Test:
    fname = ""
    lname = ""
    def __init__(self, fname):
        self.fname = fname

    def sayName(self):
        print(f"my name is {self.fname}")

test = Test("sujan")



test.sayName()