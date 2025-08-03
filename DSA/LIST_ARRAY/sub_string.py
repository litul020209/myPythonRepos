def count_substring(string, sub_string):
    substrings = []
    n = len(string)
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.append(string[i:j])
    ans=0
    for x in substrings:
        if x==sub_string:
            ans=ans+1
        else:
            continue
    return ans
    

if __name__ == '__main__':
    string ="ABCDCDC"
    sub_string ="CDC"
    
    count = count_substring(string, sub_string)
    print(count)