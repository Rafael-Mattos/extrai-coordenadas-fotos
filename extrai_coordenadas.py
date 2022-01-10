import os
from PIL import Image
import pandas as pd
import utm

#Configura as extensões aceitas
extensoes = ['jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG']

def converte_graus_decimais(direcao,coord):
    #As coordenadas vêm em graus, minutos e segundos, esta função organiza os dados e converte eles para graus decimais
    graus = coord[0][0] / coord[0][1]
    minutos = coord[1][0] / coord[1][1]
    segundos = coord[2][0] / coord[2][1]
    
    coordenada = graus + minutos / 60 + segundos / 3600

    if direcao in ['S','W']:
        coordenada = coordenada * (-1)

    return coordenada

def extrair_coordenadas(arq):
    try:
        foto = Image.open(arq) #Abre a foto escolhida
        imagem = foto._getexif()
        
        if 34853 in imagem: # Caso tenha as coordenadas contidas nos metadados
            info = foto._getexif()[34853] #Seleciona as informações das coordenadas
            
            lat = converte_graus_decimais(info[1],info[2]) #1: Norte ou sul; 2: Latitude
            longit = converte_graus_decimais(info[3],info[4]) #3: Oeste ou leste; 4: Longitude
            
            #Converte as coordenadas para UTM
            utm_x, utm_y, fuso, letra = utm.from_latlon(lat, longit)
            fuso_letra = str(fuso) + letra
            
        else: # Caso não tenha as coordenadas contidas nos metadados
            lat = '-'
            longit = '-'
            utm_y = '-'
            utm_x = '-'
            fuso_letra = '-'
        
    except:
        lat = '-'
        longit = '-'
        utm_y = '-'
        utm_x = '-'
        fuso_letra = '-'

    return [arq, lat, longit, utm_x, utm_y, fuso_letra]

def rodar():
    fotos = [
        nome for nome in os.listdir('.') if any(nome.endswith(ext) for ext in extensoes)
    ]
    
    df = pd.DataFrame(columns=['Foto','Lat','Long','E(m)','N(m)','Fuso'])
    
    for nome in fotos:
        linha = extrair_coordenadas(nome)
        df.loc[len(df)] = linha
    
    df.to_csv('_coordenadas.csv', sep=';', index=False)

if __name__ == '__main__':
    rodar()
