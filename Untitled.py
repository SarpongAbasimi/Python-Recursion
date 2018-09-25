def do_n(f,n):
    if n <= 0:
        print('done')
    else:
        f()
        do_n(f,n-1)

def p():
    print('Hello sarpong')



do_n(p,10)
