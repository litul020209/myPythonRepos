word="apple"

a=True
while a==True:
      n=len(word)
      
      for i in range(n+1):
          print(word[0:i])

      word=word[1:n]

      if not word:
         break   
        


