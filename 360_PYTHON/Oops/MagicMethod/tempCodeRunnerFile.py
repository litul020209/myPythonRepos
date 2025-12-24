class Sample:
    def __init__(self,a,b):
        self.a=a 
        self.b=b 
    def __str__(self):
        return f"{self.a},{self.b}"
        
    def __add__(self,other):
        return Sample(self.a+other.a,self.b+other.b)
    def __sub__(self,other):
        return Sample(self.a-other.a,self.b-other.b)
    def __mul__(self,other):
        return self.a*other.a,self.b*other.b
s1=Sample(10,20)
s2=Sample(20,30)
s3=Sample(30,40)
print(s1+s2+s3)
print(s1-s2-s3)
