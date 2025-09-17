
my_list=[1234445555,-789044,111100002223409,]
res=[]

list_0=[]
list_negative=[]
zero_negative_index=1
i=1
for num in my_list:
    if num <0:
        temp=-num
        list_negative=list_negative+[zero_negative_index]
    else:
        temp=num
    length=0
    
    while temp !=0:
        digit=num%10
        length+=1
        temp //=10

    if num%(10**(length-1))==0:
        list_0=list_0+[zero_negative_index]

    zero_negative_index+=1
    if num <0:
        temp=-num
    else:
        temp=num
    list1=[]
    numlen=length
    while temp!=0:
        digit=temp//(10**(length-1))
        if digit not in list1:
            list1+=[digit]

        temp=temp%(10**(length-1))          
        length=length-1
    
    
    new_num=0
    for x in list1:
        new_num=(new_num*10)+x
        
    if i in list_0:
        new_num=new_num*10
    if i in list_negative:
        new_num=-new_num
    res=res+[new_num]
    i+=1
    
print(res)



