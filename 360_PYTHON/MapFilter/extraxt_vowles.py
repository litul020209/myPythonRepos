s="abceiklaou"
vowles={"a","e","i","o","u"}
ans="".join(list(filter(lambda x:   x in vowles ,s)))
print(ans)