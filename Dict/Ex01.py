

def add_dict(student,dict):
    student.append(dict)
    return student

def add_in_list(n,a,c):
    list_01=[n,a,c]
    list_02=["name","age","course"]
    dict={}
    for i in range (len(list_01)):
        dict[list_02[i]] = list_01[i]

    return dict

student=[
    {
        "name":"Litul Biswal",
        "age":21,
        "course":"C++"
    },
    {
        "name":"Adashya Das",
        "age":23,
        "course":"Java"
    },
    {
        "name":"Anupam Mishra",
        "age":22,
        "course":"Python"
    }
]

dict=add_in_list("Sriya Duta",22,".Net")
print(dict)
final_list=add_dict(student,dict)
print(final_list)


