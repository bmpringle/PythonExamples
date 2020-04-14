class NumberComparer:

    def __init__(self, true, false):
        self.saywhenfalse = false
        self.saywhentrue = true

    def greaterThan(self, x_in, y_in):
        if(x_in > y_in):
            print(self.saywhentrue)
        else:
            print(self.saywhenfalse)
    
    def lessThan(self, x_in, y_in):
        if(x_in < y_in):
            print(self.saywhentrue)
        else:
            print(self.saywhenfalse)

    def equalTo(self, x_in, y_in):
        if(x_in == y_in):
            print(self.saywhentrue)
        else:
            print(self.saywhenfalse)

    def notEqualTo(self, x_in, y_in):
        if(x_in != y_in):
            print(self.saywhentrue)
        else:
            print(self.saywhenfalse)

comparer = NumberComparer("RIGHT", "WRONG")
comparer.equalTo(5, 2)
comparer.greaterThan(5, 2)
comparer.lessThan(5, 2)
comparer.saywhentrue = "changed saywhentrue"
comparer.notEqualTo(5, 2)