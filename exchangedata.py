

def swap():
    file1 = input('enter the file1 name? ')
    file2 = input('enter the file2 name? ')

    data1=open(file1,'r').read()
    data2=open(file2,'r').read()

    open(file1, 'w').write(data2)
    open(file2, 'w').write(data1)

   

swap()
