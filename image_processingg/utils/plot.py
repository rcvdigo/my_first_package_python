"""
Importando os módulos necessários para a execução da função auxiliar
"""
import matplotlib.pyplot as plt

def plot_image(image):
    """
    Plota uma única imagem em escala de cinza.

    Utiliza o módulo `matplotlib.pyplot` para exibir uma imagem em escala de cinza.

    Parâmetros:
    - image (array): A imagem a ser exibida.

    Exemplo de uso:
    ```python
    from skimage import io
    from matplotlib.pyplot import plot_image

    # Carrega uma imagem
    image = io.imread('path/to/image.jpg')

    # Plota a imagem
    plot_image(image)
    ```
    """
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def plot_result(*args):
    """
    Plota imagens e seu resultado em uma única linha.

    Utiliza o módulo `matplotlib.pyplot` para exibir várias imagens e o resultado final
    em uma única linha.

    Parâmetros:
    - *args (array): Uma série de imagens a serem exibidas.

    Exemplo de uso:
    ```python
    from skimage import io
    from matplotlib.pyplot import plot_result

    # Carrega as imagens
    image1 = io.imread('path/to/image1.jpg')
    image2 = io.imread('path/to/image2.jpg')

    # Plota as imagens e o resultado
    plot_result(image1, image2, result_image)
    ```
    """
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12, 4))
    names_lst = [f'Imagens {i}' for i in range(1, number_images)]
    names_lst.append('Resultado')
    for ax, name, image in zip(axis, names_lst, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()

def plot_histogram(image):
    """
    Plota os histogramas RGB de uma imagem.

    Utiliza o módulo `matplotlib.pyplot` para exibir os histogramas das componentes
    de cor vermelha, verde e azul de uma imagem colorida.

    Parâmetros:
    - image (array): A imagem cujos histogramas serão exibidos.

    Exemplo de uso:
    ```python
    from skimage import io
    from matplotlib.pyplot import plot_histogram

    # Carrega uma imagem colorida
    color_image = io.imread('path/to/color_image.jpg')

    # Plota os histogramas
    plot_histogram(color_image)
    ```
    """
    fig, axis = plt.subplots(nrows=1, 
                             ncols=3, 
                             figsize=(12, 4), 
                             sharex=True, 
                             sharey=True)
    color_lst = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title(f'Histograma {color.title()}')
        ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)
    fig.tight_layout()
    plt.show()
