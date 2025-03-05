def distancia_euclid(p1,p2): #função que calcula a distância euclidiana
  return((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def proximo_ponto(num_coordenadas,coordenadas): #função para calcular o trajeto e a distancia total
  caminho = [0] #lista que armazena o caminho percorrido, já iniciando pelo ponto 0
  indices_disponiveis = list(range(1,num_coordenadas)) #lista de indices que ainda não foram tracados no caminho
  atual = 0 # armazena o indice do ponto atual
  soma_dist = 0

  while len(indices_disponiveis) > 0:
    menor_distancia = -1 # armazena a menor distancia
    proximo_ponto = -1 # armazena qual será o proximo ponto do caminho

    for i in indices_disponiveis:
      dist = distancia_euclid(coordenadas[atual],coordenadas[i]) # calculo da distância

      if menor_distancia == -1 or dist < menor_distancia: #verificação se é o menor caminho possivel entre p0 e p1
        menor_distancia = dist  
        proximo_ponto = i
    
    soma_dist += menor_distancia # somo a menor distancia a distancia total
    caminho.append(proximo_ponto) # adiciono o ponto ao caminho
    indices_disponiveis.remove(proximo_ponto) # removo o proximo ponto dos indices disponiveis, pois ele já foi percorrido
    atual = proximo_ponto 
  
  soma_dist += distancia_euclid(coordenadas[atual],coordenadas[0]) # adiciono a distancia do ultimo ponto ate o ponto de indice 0 a soma
  caminho.append(0)
  
  return caminho,soma_dist

    
def pedir_imputs(): # função que pede as entradas
  n_coordenadas = int(input())
  coordenadas = []
  
  for i in range(n_coordenadas):
    x, y = map(int, input().split())
    coordenadas.append([x,y])

  caminho, distancia = proximo_ponto(n_coordenadas,coordenadas)
  
  string_caminho = ""
  
  for i in range(len(caminho)): #for que prepara a string do caminho para o output
    
    if i < (len(caminho)-1):
      string_caminho += (str(caminho[i]) + " ")
    else:
      string_caminho += str(caminho[i])

  print(f"Caminho: {string_caminho}")  
  print(f"Distancia: {distancia:.6f}")

pedir_imputs()
