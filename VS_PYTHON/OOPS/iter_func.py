# class iter_func():
#     def __iter__(self):
#         self.n1=1
#         return self
    

#     def __next__(self):
#         if self.n1<=20:
#             n2=self.n1
#             self.n1=self.n1+1
#             return n2
#         else:
#             return StopIteration

    

# numbers=iter_func()
# num=iter(numbers)
# for x in num:
#     print(num)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)