import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Dijkstra as dj

st.title('County Distance')
st.subheader('\"If you don\'t like the road you\'re walking, start paving another one.\"')
st.subheader('- Dolly Parton')
st.header('    Abaixo segue uma parte de um banco de dados de distâncias de um condado ao outro. Os condados são dos arquivos Census 2000 SF1 e Census 2010 SF1.  Os códigos de condado são códigos de condado FIPS. Os primeiros dois dígitos dos códigos de condado FIPS são códigos de estado FIPS. Abaixo você pode digitar dois condados e vê a menos distância entre eles.')


@st.cache
def data_distance1():
    data_distance = pd.read_csv (r'C:\Users\Wagner Bernardo\Creative Cloud Files\everything\meus programinhas\algoritmo\projetoalg\ProjetoAlgoritmos\ProjetoAlgoritmos\CountyDistances.csv', encoding='latin-1')
    return data_distance

@st.cache
def data_names1():
    data_names = pd.read_csv (r'C:\Users\Wagner Bernardo\Creative Cloud Files\everything\meus programinhas\algoritmo\projetoalg\ProjetoAlgoritmos\ProjetoAlgoritmos\CountyNames.csv', encoding='latin-1')
    return data_names

data = data_names1()
data1 = data_distance1()
df = pd.DataFrame(data1, columns= ['county1','mi_to_county','county2'])
dicg = {}
c1 = df['county1'].tolist()
distance = df['mi_to_county'].tolist()
c2 = df['county2'].tolist()

for i in range(0, len(c1)-1):
    dicg[int(c1[i])] = {}
for i in range(0,len(c1)-1):
    dicg[int(c1[i])][int(c2[i])] = distance[i]


st.write(data)
st.write('Escolha duas cidades(informando seu respectivo código) e saiba qual menor trajeto e sua distancia.')
user_input = st.text_area("Qual a primeira cidade?")
user_input1 = st.text_area("Qual a segunda cidade?")

if st.button('Enviar'):
    result = int(user_input)
    result1 = int(user_input1)
    dj.dijkstra_path(dicg, result, result1)