def mutate_string(string):
    list_01=[]
    for x in string:
        list_01.append(x)
    

    list_01[5]="k"
    str_02="".join(list_01)
    print(str_02)

if __name__ == '__main__':
    s = "abracadabra"
    # i, c = input().split()
    
    s_new = mutate_string(s)
    print(s_new)