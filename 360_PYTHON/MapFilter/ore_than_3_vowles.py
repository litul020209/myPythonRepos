words = ("appleio", "bananao", "cherry")
vowles={"a","e","i","o","u"}
ans=tuple(filter(lambda s:len([x  for x in s if x in vowles]) >3,words))
print(ans)