entera = 10 
entera += 1 # contador ++

#casting
entera = str(entera)

if(entera > 10):
    print("dentro del if")
elif(entera < 25):
    print("dentro del elif")
else:
    print("dentro del else")
    
lista = [1,5,7,1,3]
for i in lista :
    print(i) # impresion de la lista
    
for i in range(15):
    print(i) #imprime hasta el 14
    

while(entera > 10):
    print("-----")

# DO WHILE
while True:
    if(entera == 4):
        break # break rompe iteraciones

while True:
    #------ el continue vuelve aca!
    if(entera == 4):
        continue
    
#validar

terminal_str = "aa123.87"

try:
    peso = int(terminal_str)
except:
    print("Error")