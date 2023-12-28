#import functions_project as fun


def add_to_functions():
    d = {}
    val = []
    name = input('enter name of the formula : ')
    fom = input('enter the formula : ')
    rhs = fom.split('=')[1].strip()
    a = ''
    for i in rhs:
        if i != f'{i}*':
            a += i + '*'
    rhs = a[0:-1]
    lhs = fom.split('=')[0].strip()
    fom = lhs+'='+rhs
    for i in rhs:
        if i.isalpha():
            if input(f'is {i} is constant (y/n) : ') in 'yY':
                d[i] = float(input(f'enter the value of {i} constant : '))
            else:
                val.append(i)
    
    for i in d:
        fom = fom.replace(i,str(d[i]))
    
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


add_to_functions()
