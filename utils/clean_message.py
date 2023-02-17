def clean_message(message):
    zn = ['!','.','?',',',':',';','/','|','(',')','{','}','[',']']
    for i in range(len(zn)):
        message = message.replace(zn[i],' ')
    return message.lower().split()