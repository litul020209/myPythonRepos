


def concate(*args):
    new_dict={}
    for x in args:
        new_dict.update(x)
    return new_dict



dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

ans=concate(dic1,dic2,dic3)
print(ans)
