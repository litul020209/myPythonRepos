digit=[9,9,9]
if not digit:
    print("no digit in there")
else: 
     result="".join(str(n) for n in digit)
     ans=int(result)
     ans=ans+1
     ans_str=str(ans)
     ans_list=[]
     for x in ans_str:
          y=int(x)
          ans_list.append(y)
     print(ans_list)

     
