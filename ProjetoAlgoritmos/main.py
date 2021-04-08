import pandas as pd
import Dijkstra as dj


data_distance = pd.read_csv (r'C:\Users\Wagner Bernardo\Creative Cloud Files\everything\meus programinhas\algoritmo\projetoalg\ProjetoAlgoritmos\ProjetoAlgoritmos\CountyDistances.csv', encoding='latin-1')
data_names = pd.read_csv (r'C:\Users\Wagner Bernardo\Creative Cloud Files\everything\meus programinhas\algoritmo\projetoalg\ProjetoAlgoritmos\ProjetoAlgoritmos\CountyNames.csv', encoding='latin-1')
df = pd.DataFrame(data_distance, columns= ['county1','mi_to_county','county2'])

dicg = {}
c1 = df['county1'].tolist()
distance = df['mi_to_county'].tolist()
c2 = df['county2'].tolist()



for i in range(0, len(c1)-1):
    dicg[int(c1[i])] = {}
for i in range(0,len(c1)-1):
    dicg[int(c1[i])][int(c2[i])] = distance[i]




print("Escolha duas cidades(informando seu respectivo código) e saiba qual menor trajeto e sua distancia.")
<<<<<<< HEAD
cid1 = int(input("Qual o primeiro condado?"))
cid2 = int(input("Qual o segundo condado?"))

dj.dijkstra_path(dicg, cid1, cid2)