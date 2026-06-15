import networkx as nx
import numpy as np

def build_pmfg(similarity_matrix):
    """
    Implementa o algoritmo PMFG conforme descrito por Tumminello et al. (2005).
    paper recomendado pelo professor 
    """
    n = similarity_matrix.shape
    
    # construir uma lista ordenada (Sord) de pares de nós em ordem 
    # decrescente de similaridade (sij) 
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            # armazena (nó1, nó2, peso/similaridade)
            edges.append((i, j, similarity_matrix[i, j]))
    
    # ordena de forma decrescente pela similaridade
    edges.sort(key=lambda x: x[1], reverse=True)
    
    # inicializar um grafo vazio para o PMFG
    pmfg = nx.Graph()
    pmfg.add_nodes_from(range(n))
    
    # o número máximo de links no PMFG é 3(n - 2)
    max_edges = 3 * (n - 2)
    current_edge_count = 0
    
    # algoritmo de Construção adiciona arestas sob restrição topológica
    for u, v, weight in edges:
        if current_edge_count >= max_edges:
            break
            
        # adiciona temporariamente a aresta para testar a planaridade
        pmfg.add_edge(u, v)
        
        # verifica se o grafo resultante ainda pode ser imerso em uma 
        # superfície de gênero g=0 (ou seja, se é planar) 
        is_planar, _ = nx.check_planarity(pmfg)
        
        if is_planar:
            current_edge_count += 1
        else:
            # se violar a planaridade, remove a aresta adicionada 
            pmfg.remove_edge(u, v)
            
    return pmfg