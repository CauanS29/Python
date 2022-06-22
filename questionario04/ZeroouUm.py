alice = int(input()) 
beto = int(input()) 
clara = int(input()) 

vencedor = "*" 

if alice != beto and alice != clara : 
   vencedor = "A" 

elif beto != alice and beto != clara : 
   vencedor = "B" 

elif clara != alice and clara != beto : 
   vencedor = "C" 

print(vencedor) 