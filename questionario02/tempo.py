tempo = int(input())  

horas = tempo//3600 
restoSegundos = tempo%3600 
minutos = restoSegundos//60 
segundos = restoSegundos%60 

print(horas, ":", minutos, ":", segundos) 