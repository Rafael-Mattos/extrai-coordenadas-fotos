# Python Extrator de coordenadas 
Código Python para criar um arquivo CSV com as coordenadas extraídas dos metadados das fotos contidas em uma pasta.

## Rodando o arquivo ".exe" no Windows
Caso esteja precisando apenas de um software para extrair as coordenadas de um determinado conjunto de fotos sem precisar entender o código, basta:
1. Baixar o arquivo de extensão ".exe";
2. Criar uma pasta e copiar nela todas as fotos das quais se deseja extrair as coordenadas (lembrando que os arquivos das fotos devem conter as informações de coordenadas em seus metadados);
3. Copiar o arquivo ".exe" baixado na pasta recém criada;
4. Clicar duas vezes no arquivo ".exe" para executar a operação;
5. Note que não há indicação de carregamento e dependendo da quantidade de fotos o código pode demorar mais ou menos para finalizar a execução;
6. Após concluído o processo, será criado um arquivo de nome "coordenadas.csv" com os nomes das fotos e suas respectivas coordenadas;
7. Se o arquivo não aparecer de imediato, tente clicar com o botão direito em um espaço vazio da pasta e em seguida clicar em atualizar.<br/><br/>
Observação: Caso o arquivo ".exe" tenha sido gerado conforme os procedimentos descritos abaixo, o nome do arquivo de coordenadas será conforme configurado no código.

## Instruções para implementação

### Pré-requisitos
* As fotos a serem utilizadas para extração das coordenadas devem conter estas informações em seus respectivos metadados, portanto, assegure-se de configurar o aparelho utilizado para tirar as fotos para tal
* Instalação do Python 3 com PIP
* Instalar as bibliotecas necessárias:
1. Instalar a biblioteca Pillow - Será utilizada para acessar os metadados das fotos
```
pip install Pillow
```
2. Instalar a biblioteca UTM - Será utilizada para realizar a conversão das coordenadas de graus decimais para UTM
```
pip install utm
```
3. Instalar a biblioteca PyInstaller - Será utilizada para gerar um arquivo ".exe" para ser rodado no Windows
```
pip install pyinstaller
```
### Rodando arquivo ".py"
Para gerar as coordenadas de um determinado conjunto de fotos, basta colocar as fotos em uma pasta separada (lembrando que as fotos devem conter as respectivas coordenadas em seus metadados) junto ao arquivo "extrai_coordenadas.py" baixado. Em seguida, navegar pelo terminal ou prompt de comando até a pasta em questão e rodar o seguinte comando
```
python extrai_coordenadas.py
```
Após concluído o processamento, será gerado um arquivo "_coordenadas.csv" com as coordenadas em graus decimais e em UTM, no DATUM WGS 84, de todas as fotos contidas na pasta.

### Gerando um arquivo executável para Windows ".exe"
Para gerar um arquivo que rode em qualquer PC com Windows, independente de ter o Python instalado, é possível gerar um arquivo no formato ".exe". Para isso, basta abrir o terminal de comando ou prompt, navegar até a pasta em que o arquivo "extrai_coordenadas.py" foi baixado e utilizar a biblioteca PyInstaller com o comando:
```
pyinstaller -w -F extrai_coordenadas.py
```
Obs: O trecho "extrai_coordenadas.py" é o nome do arquivo Python que será convertido em ".exe"<br/><br/>
Para executar o arquivo ".exe", seguir os passos descritos em ["Rodando o arquivo ".exe" no Windows"](#rodando-o-arquivo-exe-no-windows)
# Autor
Rafael Rosa de Mattos
