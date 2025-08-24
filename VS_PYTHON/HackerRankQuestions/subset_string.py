s="banana"
s=s.upper()

ans=[]
n=len(s)
for i in range (n):
    for j in range (n+1):
        if i>= j:
            continue
        w=s[i:j]
        ans.append(w)

sans=set(ans)
fans=list(sans)
fans.sort()
vowel_list=["A","E","I","O","U"]
result_v=[]
for x in fans:
    if x[0] in vowel_list:
        result_v.append(x)
ans_v_dict={}
for w in result_v:
    l=len(w)
    count=0
    for i in range(n-l+1):
        if w==s[i:i+l]:
            count=count+1
        
    ans_v_dict[w]=count

set_result_v=set(result_v)
result_c=sans.difference(set_result_v)

ans_c_dict={}
for w in result_c:
    l=len(w)
    count=0
    for i in range(n-l+1):
        if w==s[i:i+l]:
            count=count+1
        
    ans_c_dict[w]=count

Stuart_count=0
Kevin_count=0
for v1 in ans_c_dict.values():
    Stuart_count=Stuart_count+v1

for v2 in ans_v_dict.values():
    Kevin_count=Kevin_count+v2

if Stuart_count>Kevin_count:
    print(f"Stuart {Stuart_count}")
else:
    print(f"Kevin {Kevin_count}")


     