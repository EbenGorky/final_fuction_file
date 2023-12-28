def add_functions():
    d = {}
    val = []
    name = input('enter name of the formula : ')
    fom = input('enter the formula : ')
    lhs = fom.split('=')[0].strip()
    rhs = fom.split('=')[1].strip()


    for i in fom.split('=')[1].strip():
        if i.isalpha() and i not in val:
            val.append(i)

    s_val = ''
    for i in val:
        s_val += f"\t{i} = input('enter the value for the {i} : ')\n"
    
    s_function = f"""\ndef {name}:
    {s_val}
        {fom}
        print('the value of {lhs} is ' {lhs})\n"""
    print(s_function)
    
    with open(r'functions_project.py','a') as f:
        f.write(s_function)

n = int(input('enter the number of functions to create '))
for i in range(n):
    add_functions()
