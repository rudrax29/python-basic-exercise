class rectangle():
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def area(self):
        print(self.length*self.width)

r=rectangle(20,10)
r.area()
        
