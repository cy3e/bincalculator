import bina

print("bienvenido a mi aplicacion")
print
print ("presiona 1 para iniciar o presiona 0 para salir")

p = int(input())

if p == 1:
   menu()
   
else:
    exit()

def menu():
    print("elija el valor que desea que le retorne")
    print("1: decimal")
    print("2: binario")
    print("3: Hexadecimal")
    print("e: to exit")
    print("F: to give me respect")
        
    r = int(input())
       
    if r == 1:
           bina.decimal
            
    elif r == 2:
        bina.binario
            
                
    elif r ==3:
        bina.hexa
          
    else:
        exit()