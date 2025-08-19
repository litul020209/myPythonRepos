class HashTable:
    def __init__(self,size):
        
        self.size=size
        self.arr=(None,)*self.size
    def get_hash(self,key):
        if type(key)==int:
            return key
        else:
            sum=0
            for x in key:
                sum=sum+ord(x)
            return sum%self.size
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        self.arr(h)=value
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr(h)
    def __delitem__(self,key):
        h=self.get_hash(key)
        del self.arr(h)
        return self.arr(h)
    
        
    
marks=HashTable(10)
marks(1)=10
print(marks(1))





