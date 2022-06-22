def gasolinaBarata (transformacaoGalao, gasolinaBR) :
     
     comparaGasolinas = "Mais barata no Brasil"

     if transformacaoGalao == gasolinaBR:
        comparaGasolinas = "Igual" 
     
     elif transformacaoGalao < gasolinaBR: 
          comparaGasolinas = "Mais barata nos EUA"
     
     return(comparaGasolinas) 


gasolinaEUA = float(input()) 
gasolinaBR = float(input()) 
cotacaoDolar = float(input()) 



transformacaoGalao = (gasolinaEUA * cotacaoDolar)/3.8

print("Gasolina EUA: R$ %.2f"%transformacaoGalao) 
print("Gasolina Brasil: R$ %.2f"%gasolinaBR) 
print(gasolinaBarata(transformacaoGalao, gasolinaBR)) 