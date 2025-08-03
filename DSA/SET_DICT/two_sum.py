#using set
set_01=[2,7,11,15]
target=26
dict_01={}
for i in range(len(set_01)):
    rem=target-set_01[i]
    if rem  in dict_01:
        a= [dict_01[rem],i]
    dict_01[set_01[i]]=i
    
print(a)


