"""
Importando os módulos necessários para a execução da função
"""
import numpy as np


from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def find_difference(image1, image2):
    """
    Realiza a comparação de diferenças entre duas imagens.

    Esta função utiliza a métrica de similaridade estrutural (SSIM) para comparar as
    diferenças entre duas imagens. A comparação é feita convertendo as imagens para tons
    de cinza e calculando o SSIM.

    Parâmetros:
    - image1 (array): A primeira imagem a ser comparada.
    - image2 (array): A segunda imagem a ser comparada.

    Retorna:
    - normalized_difference_image (array): Uma imagem representando as diferenças normalizadas
      entre as duas imagens.

    Observações:
    - A função assume que ambas as imagens têm a mesma forma (mesma largura e altura).
    - O resultado do SSIM é impresso no console para fornecer uma métrica de similaridade
      entre as imagens.

    A métrica SSIM varia de -1 a 1, onde 1 indica que as imagens são idênticas. Valores mais
    próximos de 1 indicam maior similaridade.

    Exemplo de uso:
    ```python
    from skimage.metrics import find_difference
    from skimage import io

    # Carrega as imagens a serem comparadas
    image1 = io.imread('path/to/image1.jpg')
    image2 = io.imread('path/to/image2.jpg')

    # Calcula as diferenças normalizadas entre as imagens
    differences = find_difference(image1, image2)
    ```

    Referências:
    - Documentação do scikit-image (SSIM): 
    https://scikit-image.org/docs/stable/api/skimage.metrics.html#skimage.metrics.structural_similarity
    """
    assert image1.shape == image2.shape, "Especifique 2 imagens com a mesma forma"
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(gray_image1,
                                                      gray_image2,
                                                      full=True)
    print("Similaridade das imagens:", score)
    normalized_difference_image = (difference_image - np.min(difference_image)) / (
        np.max(difference_image) - np.min(difference_image))
    return normalized_difference_image

def transfer_histogram(image1, image2):
    """
    Realiza a transferência de histograma entre duas imagens.

    Esta função utiliza a função `match_histograms` do módulo `skimage.exposure` para
    transferir o histograma da imagem de origem (`image1`) para a imagem de destino (`image2`).

    Parâmetros:
    - image1 (array): A imagem de origem cujo histograma será transferido.
    - image2 (array): A imagem de destino que receberá o histograma da imagem de origem.

    Retorna:
    - matched_image (array): A imagem de destino após a transferência do histograma.

    Observação:
    A opção `multichannel=True` é utilizada para indicar que as imagens possuem múltiplos canais
    de cor (por exemplo, imagens RGB).

    A transferência de histograma é útil em processamento de imagem para equalizar as 
    distribuições de intensidade entre duas imagens, tornando-as mais visualmente 
    semelhantes em termos de contraste
    e brilho.

    Exemplo de uso:
    ```python
    from skimage.exposure import transfer_histogram
    from skimage import io

    # Carrega as imagens de origem e destino
    image1 = io.imread('path/to/image1.jpg')
    image2 = io.imread('path/to/image2.jpg')

    # Aplica a transferência de histograma
    result_image = transfer_histogram(image1, image2)
    ```

    Referências:
    - Documentação do scikit-image: 
    https://scikit-image.org/docs/stable/api/skimage.exposure.html#skimage.exposure.match_histograms
    """
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image
