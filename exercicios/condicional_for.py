#for n in range(0, 30, 3):
    #print(n)
    
texto = "python"
nova_string = ''

for letra in texto:
    if letra =='p':
        nova_string=nova_string +letra.upper()
    elif letra =='n':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
        
print(nova_string)