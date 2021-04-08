import pandas as pd
import Dijkstra as dj


data_distance = pd.read_csv (r'C:\Users\betin\OneDrive\Área de Trabalho\ProjetoAlgoritmos\CountyDistances.csv')
data_names = pd.read_csv (r'C:\Users\betin\OneDrive\Área de Trabalho\ProjetoAlgoritmos\CountyNames.csv')
df = pd.DataFrame(data_distance, columns= ['county1','mi_to_county','county2'])

dicg = {}
c1 = df['county1'].unique().tolist()
distance = df['mi_to_county'].unique().tolist()
c2 = df['county2'].unique().tolist()

for i in c1:
    dicg[i] = {}
    a = df.query(f'county1 == {i}')

    for ind, j in a.iterrows():
        dicg[i][int(j['county2'])] = j['mi_to_county']

print(data_names)
print("Escolha duas cidades(informando seu respectivo código) e saiba qual menor trajeto e sua distancia.")
cid1 = int(input("Qual a primeira cidade?"))
cid2 = int(input("Qual a segunda cidade?"))
dj.dijkstra_path(dicg, cid1, cid2)
