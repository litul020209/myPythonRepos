def revString(str):
    if not str:
        return ""
    return revString(str[1:])+str[0]
     

final_str=revString("Litul")
print(final_str)