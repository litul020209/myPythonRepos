employees = [
    {
        'fname': 'Nitish',
        'lname': 'Singh',
        'age': 33,
        'grade': 'skilled'
    },
    {
        'fname': 'Ankit',
        'lname': 'Verma',
        'age': 34,
        'grade': 'semi-skilled'
    },
    {
        'fname': 'Neha',
        'lname': 'Singh',
        'age': 35,
        'grade': 'highly-skilled'
    },
    {
        'fname': 'Anurag',
        'lname': 'Kumar',
        'age': 30,
        'grade': 'skilled'
    },
    {
        'fname': 'Abhinav',
        'lname': 'Sharma',
        'age': 37,
        'grade': 'highly-skilled'
    }

]

list(map(lambda x:x['fname'] + ' ' + x['lname'],list(filter(lambda x:True if x['grade'] == 'highly-skilled' else False,employees))))