[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/designed-in-ms-paint.svg)](https://forthebadge.com)

# uSimulador

Simulador de algoritmos de resolução de labirinto para micro mouse.

## Script breakdown

- [maze.py](./maze.py)       - Cria um objeto do tipo labirinto, com suas paredes e o micromouse

- [interface.py](./interface.py)  - GUI para o labirinto, habilitada por padrão, para desabilitar é só comentar uma linha no arquivo maze.py

- [floodfill.py](./floodfill.py)  - Conjunto de funções que implementam o algoritmo Flood Fill, usado para buscar o melhor caminho entre dois pontos definidos dentro de um labirinto

- [main.py](./main.py)       - Rotina de demonstração da interface gráfica e do algoritmo Flood Fill