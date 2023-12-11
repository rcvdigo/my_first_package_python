"""
Importando os módulos necessários para a execução da função
"""
from skimage.transform import resize

def resize_image(image, proportion):
    """
    Redimensiona uma imagem proporcionalmente de acordo com a proporção especificada.

    Esta função utiliza a função `resize` do módulo `skimage.transform` para redimensionar
    a imagem de entrada. O redimensionamento é feito proporcionalmente com base na
    proporção fornecida. A imagem resultante tem sua altura e largura ajustadas de acordo
    com a multiplicação da proporção pela altura e largura originais da imagem.

    Parâmetros:
    - image (array): A imagem a ser redimensionada.
    - proportion (float): A proporção pela qual a imagem será redimensionada. Deve estar
      no intervalo [0, 1], onde 1 representa nenhum redimensionamento e 0 representa
      uma imagem totalmente reduzida.

    Retorna:
    - image_resized (array): A imagem redimensionada.

    Observações:
    - A função utiliza o redimensionamento anti-aliasing (`anti_aliasing=True`) para melhorar
      a qualidade da imagem após o redimensionamento, suavizando transições e reduzindo artefatos.

    Exemplo de uso:
    ```python
    from skimage.transform import resize_image
    from skimage import io

    # Carrega a imagem
    original_image = io.imread('path/to/image.jpg')

    # Redimensiona a imagem para 50% do tamanho original
    resized_image = resize_image(original_image, proportion=0.5)
    ```

    Referências:
    - Documentação do scikit-image (resize): 
    https://scikit-image.org/docs/stable/api/skimage.transform.html#skimage.transform.resize
    """
    assert 0 <= proportion <= 1, "Especifique uma proporção válida entre 0 e 1."
    height = round(image.shape[0] * proportion)
    width = round(image.shape[1] * proportion)
    image_resized = resize(image, (height, width), anti_aliasing=True)
    return image_resized
