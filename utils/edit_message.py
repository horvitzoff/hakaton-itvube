def clean_message(message):
    zn = ['!','.','?',',',':',';','/','|','(',')','{','}','[',']']
    for i in range(len(zn)):
        message = message.replace(zn[i],' ')
    return message.lower().split()

def func_compare(b,a):
    check = 0
    for i in b:
        if i in a:
            check += 1
    if check == len(b):
        return True
    else:
        return False