
def flipping(bin_str,k):
    if k!=1:
       ans=""
       for x in bin_str:
            if x == "0":
              ans=ans+"01"
            else:
                ans=ans+"10"
       return flipping(ans,k-1)
    else:
        return bin_str
           

bin_str=input("Enter binary string: ")
k=int(input("Enter steps: "))
res=flipping(bin_str,k)
print(res)
