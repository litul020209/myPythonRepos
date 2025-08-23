b_name=input("Enter the Boys name: ").lower()
g_name=input("Enter the Boys name: ").lower()

first_part=["t","r","u","e"]
second_part=["l","o","v","e"]

f_name=b_name+g_name
count1=0
for x in f_name:
    if x in first_part:
        count1+=1
count2=0
for y in second_part:
    if y in second_part:
        count2+=1

print(f"{count1}{count2}%")