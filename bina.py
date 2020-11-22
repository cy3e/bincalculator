import bincalc

dic_hex = {
    '0':0000,'1':0001,'2':0010,'3':0011,'4':0100,'5':0101,'6':0110,'7':0111,
    '8':1000,'9':1001,'a':1010,'b':1011,'c':1100,'d':1101,'e':1110,'f'':1111
}

dic_dec = {
    '0':0000,'1':0001,'2':0010,'3':0011,'4':0100,'5':0101,'6':0110,'7':0111,
    '8':1000,'9':1001,'10':1010,'11':1011,'12':1100,'13':1101,'14':1110,'15':1111
}
dic_bin = {
    '0000':0,'0001':1,'0010':2,'0011':3,'0100':4,'0101':5,'0110':6,'0111':7,
    '1000':8,'1001':9,'1010':10,'1011':11,'1100':12,'1101'13,'1110':14,'1111':15
}

binario = []

def binario():
    print("***********************binario-translator*****************************")
    bin = int(input("introduce el binario"))

    for j in bin:
        if j in dic_bin:
            bina.append(dic_bin)
        else:
            print("el caracter",j,"no es valido introduce otro")
    resultado_final = ("").join(binario)

def decimal():
     print("***********************binario-to-decimal-translator*****************************")
    bin = int(input("introduce el binario"))

    for j in bin:
        if j in dic_dec:
            bina.append(dic_dec)
        else:
            print("el caracter",j,"no es valido introduce otro")
    resultado_final = ("").join(binario)
    

def hexa():
    print("***********************binario-to-Hexa-translator*****************************")
    bin = int(input("introduce el binario"))

    for j in bin:
        if j in dic_dec:
            bina.append(dic_dec)
        else:
            print("el caracter",j,"no es valido introduce otro")
    resultado_final = ("").join(binario)
    print("")
    print("su respuesta es ",binario_final)
    print("")

    con = ns(input("desea continuar"))
    if con == "no":
        break
    subprocess.call(["cmd.exe","/C","cls"])
















'''print("ingrese un valor")
valor = int(input())
print( bin(valor))
print(hex (valor))
b = bin(valor)
print(int(b,2))
print("tu valor es ")
f = int(input())'''