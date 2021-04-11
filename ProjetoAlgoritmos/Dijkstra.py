import streamlit as st

def dijkstra(grafo, origem, fim):

    verificacao = { }
    distancia = { }
    no = { }
    nao_visitados = []
    atual = origem
    no[atual] = 0

    
    for vertice in grafo.keys():
        nao_visitados.append(vertice)  
        distancia[vertice] = float('inf') 

    distancia[atual] = [0,origem] 
    nao_visitados.remove(atual)

    while nao_visitados:
        for vizinho, peso in grafo[atual].items():
            peso_somado = peso + no[atual]
            if distancia[vizinho] == float("inf") or distancia[vizinho][0] > peso_somado:
                distancia[vizinho] = [peso_somado,atual]
                verificacao[vizinho] = peso_somado
        
                 
        if verificacao == {}: 
            break    

        minVizinho = min(verificacao.items(), key=lambda x: x[1]) 
        atual=minVizinho[0]
        no[atual] = minVizinho[1]
        nao_visitados.remove(atual)
        del verificacao[atual]

    st.balloons()
    st.success("Aqui estão os resultados:")
    st.write("A menor distância de %s até %s é: %smi" % (origem, fim, distancia[fim][0]))
    st.write("O menor caminho é: %s" % print_caminho(distancia,origem, fim))          
    

def print_caminho(distancias, inicio, fim):
    if  fim != inicio:
        return "%s -- > %s" % (print_caminho(distancias,inicio, distancias[fim][1]),fim)
    else:
        return inicio
