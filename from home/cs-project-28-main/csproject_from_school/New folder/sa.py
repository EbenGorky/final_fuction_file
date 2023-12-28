#a = ['sin','cos','tan']
def add_for():
    #with open('functions_project.py','a') as fp:
    fn = input('function name : ').replace(' ','_')
    ln = input('function last name : ')
    fo = input('formula : ')
    lhs,rhs = tuple(fo.split('='))
    v = ''
    for i in rhs:
        if i.isalpha() and i not in v:
            v = v + str(i) +','
    v = v[:-1]
    print(v)
    #fun = f"\ndef {fn}__{ln}({v}):\n\treturn ('{lhs}=',{rhs},':{fo}')\n"
    #    fp.write(fun)
    print(v)
    for i in a:
        pass



    print('\n','-'*5,'new','-'*5,'\n')


add_for()