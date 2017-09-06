class mathDojo(object):
    def __init__(self):
        self.total = 0
    def add(self,num,*args):
        if (type(num) == list) or (type(num) == tuple):
            for y in num:
                self.total += y
        else:
            self.total += num
        self.args = list(args)
        if len(self.args) == 0:
            return self
        else:
            for x in self.args:
                if (type(x) == list) or (type(x) == tuple):
                    for y in x:
                        self.total += y
                else:
                    self.total += x
            return self
    def subtract(self,num,*args):
        if (type(num) == list) or (type(num) == tuple):
            for y in num:
                self.total -= y
        else:
            self.total -= num
        self.args = list(args)
        if len(self.args) == 0:
            return self
        else:
            for x in self.args:
                if (type(x) == list) or (type(x) == tuple):
                    for y in x:
                        self.total -= y
                else:
                    self.total -= x
            return self
    def result(self):
        print self.total
