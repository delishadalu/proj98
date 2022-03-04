

def swap():
    file1 = input('enter the file1 name? ')
    file2 = input('enter the file2 name? ')

    file1text=open(file1,'r')
    data1=file1text.read()

    file2text=open(file2,'r')
    data2=file2text.read()

    file1text = open(file1, 'w')
    file1text.write(data2)

    file2text = open(file2, 'w')
    file2text.write(data1)


swap()
