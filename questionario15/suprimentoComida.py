quantidadeCasos = int(input()) 


for i in range(0, quantidadeCasos): 
         
       quantiadadeAlimentos = float(input()) 
       
       dias = 0
       
       while (quantiadadeAlimentos) > 1 :

            quantiadadeAlimentos = quantiadadeAlimentos/2  

            dias+= 1 

       print(dias, "dias")