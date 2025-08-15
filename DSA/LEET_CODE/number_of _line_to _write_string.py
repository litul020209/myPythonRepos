s = "bbbcccdddaaa"
w = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

alphabet_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
sum_=0   #real sum upto 100px

count=0  #how many lines in string which reach 100px
ans=[]   #strore the ans in here
for l in s:
    indx=alphabet_list.index(l)
    value=w[indx]
    sum_=sum_+value
    
    if sum_>100:
        count=count+1
        sum_=0
        sum_=sum_+value
if sum_ > 0:
   count +=1
ans.append(count)
ans.append(sum_)
print(ans) 

        




# a=4
# b=0
# c=0
# while c<=50:
#     c=c+a
#     if c>50:
#         print(b)
#     else:
#         b=b+a

