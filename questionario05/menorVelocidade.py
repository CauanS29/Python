def velkmh (VO, A, T,) : 
    V = VO + A*T  
    return V 

VoCarro1 = float(input()) 
ACarro1 = float(input()) 
Tcarro1 = float(input()) 
VfinalCarro1 = velkmh (VoCarro1, ACarro1, Tcarro1) 

VoCarro2 = float(input()) 
ACarro2 = float(input()) 
Tcarro2 = float(input()) 
VfinalCarro2 = velkmh (VoCarro2, ACarro2, Tcarro2) 

VoCarro3 = float(input()) 
ACarro3 = float(input()) 
Tcarro3 = float(input()) 
VfinalCarro3 = velkmh (VoCarro3, ACarro3, Tcarro3) 

menorVelocidade = min(VfinalCarro1, VfinalCarro2, VfinalCarro3) * 3.6

print("%.1f"%menorVelocidade) 

