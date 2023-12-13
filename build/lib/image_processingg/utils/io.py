"""
Importando os módulos necessários para a execução da função auxiliar
"""
from skimage.io import imread, imsave

def read_image(path, is_gray=False):
    """
    Carrega uma imagem do caminho especificado.

    Utiliza a função `imread` do módulo `skimage.io` para carregar a imagem do caminho
    fornecido. A opção `as_gray` é utilizada para determinar se a imagem deve ser lida
    como escala de cinza.

    Parâmetros:
    - path (str): O caminho do arquivo de imagem a ser carregado.
    - is_gray (bool): Indica se a imagem deve ser lida como escala de cinza. O padrão é False.

    Retorna:
    - image (array): A imagem carregada.

    Exemplo de uso:
    ```python
    from skimage.io import read_image

    # Carrega uma imagem colorida
    color_image = read_image('path/to/color_image.jpg')

    # Carrega uma imagem em escala de cinza
    gray_image = read_image('path/to/gray_image.jpg', is_gray=True)
    ```
    """
    image = imread(path, as_gray=is_gray)
    return image

def save_image(image, path):
    """
    Salva uma imagem no caminho especificado.

    Utiliza a função `imsave` do módulo `skimage.io` para salvar a imagem no caminho fornecido.

    Parâmetros:
    - image (array): A imagem a ser salva.
    - path (str): O caminho do arquivo no qual a imagem será salva.

    Exemplo de uso:
    ```python
    from skimage.io import save_image

    # Salva uma imagem
    save_image(image, 'path/to/save_image.jpg')
    ```
    """
    imsave(path, image)
