import math
import matplotlib.pyplot as plt #chat gebitoca




#dist entre 2 pontos
def euclidean_distance(point1, point2):
    # = sqrt((x1 - x2)² + (y1 - y2)² + (z1 - z2)²)
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2)





#acha a estrela mais proxima, lembrando q a lista stars sempre remove a estrela ja visitada 
def find_nearest_star(current_position, stars):
    melhor_estrela = None
    melhor_distancia = 99999999.0

    for star in stars: #itera em todas as estrelas
        distance_get = euclidean_distance(current_position, star) #pega dist de cada estrela referente naquela estrela

        if distance_get < melhor_distancia: #achou a estrela mais perta
            melhor_estrela = star
            melhor_distancia = distance_get
    return melhor_estrela, melhor_distancia




if __name__ == "__main__":
    #inicializaçao de variavel
    ponto_atual = (0.0, 0.0, 0.0) #varios float
    total_distance = 0.0 #float

    path = []



    #extrai as estrela
    stars = []
    with open('stars.xyz', 'r') as file:
        for line in file: #cada linha tem X Y Z
            x, y, z = map(float, line.split()) #split = tokeniza os float, map = retira os valor pela quantidade de tokens
            stars.append((x, y, z)) #bota todas estrela no vetor vazio

    print(f"achei {len(stars)} estrelas! [enter]") #ver se pegou 100 estrelas como esperado
    input()

    copia_stars = stars #só pra ver se ta certo depois, no fim do codigo



    for _index, strela in enumerate(stars):
        print(f"{_index}: {strela[0]:.4f} {strela[1]:.4f} {strela[2]:.4f}") #printa as estrela pra ver se ta certo

    print(f"\n[enter]")
    input()



    #remove um bug, em q começa em 0 0 0 mas ja tem uma estrela 0 0 0
    stars.remove(ponto_atual)


    #heuristica
    for _ in range(len(stars)): #itera em todas as estrelas do vetor (é pra ser 100)
        melhor_estrela, melhor_distancia = find_nearest_star(ponto_atual, stars) #acha a estrela mais perta, obviamente

        stars.remove(melhor_estrela) #tira da lista original
        path.append(melhor_estrela) #adiciona no path

        total_distance += melhor_distancia #soma distancia

        ponto_atual = melhor_estrela #referencia a nova estrela como a atual


    #printa distancia
    print(f'distancia total: {total_distance}')
    print('\n[enter]')
    input()




    #printa path
    for star in path:
        print(f'{star}\t', end = '')
    print('\n[enter]')
    input()




    #iterador pra ver se ta tudo certo
    for star_copy in copia_stars:
        if star_copy not in path:
            print(f'eita, achei uma estrela nada a ver!\t na lista original: {star_copy}')
            exit()





    ################################################################
    # parte pra printar em 3d, tirado do chat gpt <- extra
    ################################################################

    #cria a 'janela' de plot
    fig = plt.figure()
    img = fig.add_subplot(111, projection='3d')

    #extract coordinates x, y, z from the path
    xs, ys, zs = zip(*path)

    #calculate the color gradient from light blue to dark red
    min_z, max_z = min(zs), max(zs) 
    colors = [
        (0.0, 0.5 * (1 - (z - min_z) / (max_z - min_z)), 1.0 - 0.5 * (z - min_z) / (max_z - min_z)) for z in zs
    ] # /\ errado

    #plot the path with gradient colors
    for i in range(len(xs) - 1):
        img.plot(xs[i:i+2], zs[i:i+2], ys[i:i+2], color = colors[i], marker = 'o')

    #set axis labels
    img.set_xlabel('x')
    img.set_ylabel('z')
    img.set_zlabel('y')

    plt.title('movements between the stars')

    #save the plot to a file and display the message
    plt.savefig('movements_between_the_stars.png')
    print("\nthe plot has been saved as 'movements_between_the_stars.png'.")

