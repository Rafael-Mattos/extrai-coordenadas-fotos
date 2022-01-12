# Python Extrator de coordenadas 
Código Python para criar um arquivo CSV com as coordenadas extraídas dos metadados das fotos contidas em uma pasta.

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
