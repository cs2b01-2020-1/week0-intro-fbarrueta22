from io import open
import string
def lecturagenoma(name):
    g=open(name,'r')
    g_datos=g.read()
    datos=''
    for i in g_datos:
        if(i!="\n"):
            datos=datos+i
    return datos
def similitud(genoma1,genoma2):
    sum=0
    rango=min(len(genoma1),len(genoma2))
    for i in range(rango):
        if(genoma1[i]==genoma2[i]):
            sum+=1
    return (sum/rango)*100
suma=0
print("Analizando los Genomas.........!")
#genoma1
g1=lecturagenoma('AY274119.txt')
#genoma2
g2=lecturagenoma('AY2784882.txt')
#genoma3
g3=lecturagenoma('MN908947.txt')
#genoma4
g4=lecturagenoma('MN988668.txt')
#genoma5
g5=lecturagenoma('MN988669.txt')

#genoma1 vs genoma2
p12=similitud(g1,g2)
#genoma1 vs genoma3
p13=similitud(g1,g3)
#genoma1 vs genoma4
p14=similitud(g1,g4)
#genoma1 vs genoma5
p15=similitud(g1,g5)

#genoma2 vs genoma3
p23=similitud(g2,g3)
#genoma2 vs genoma4
p24=similitud(g2,g4)
#genoma2 vs genoma5
p25=similitud(g2,g5)

#genoma3 vs genoma4
p34=similitud(g3,g4)
p35=similitud(g3,g5)

#genoma4 vs genoma5
p45=similitud(g4,g5)


print("-------------------------------------------------------------")
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('%','Genoma1','Genoma2','Genoma3','Genoma4','Genoma5'))
print("-------------------------------------------------------------")
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('Genoma1','100',round(p12,2),round(p13,2),round(p14,2),round(p15,2)))
print("-------------------------------------------------------------")
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('Genoma2',round(p12,2),'100',round(p23,2),round(p24,2),round(p25,2)))
print("-------------------------------------------------------------")
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('Genoma3',round(p13,2),round(p23,2),'100',round(p34,2),round(p45,2)))
print("-------------------------------------------------------------")
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('Genoma4',round(p14,2),round(p24,2),round(p34,2),'100',round(p45,2)))
print("-------------------------------------------------------------")
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('Genoma5',round(p15,2),round(p25,2),round(p35,2),round(p45,2),'100'))
print("-------------------------------------------------------------")
