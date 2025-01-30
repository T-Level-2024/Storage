class Test:
    self.input1, self.input2 = None, None
    def __init__(self, input1, input2):
        self.input1, self.input2 = input1, input2
    
    def multiply(self):
        return self.input1, self.input2

A = Test(5, 20)
Test.multiply(100)