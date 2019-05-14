# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:29:23 2019

@author: Aluno 10
"""

#pip install -U scikit-learn
#pip install yellowbrick

import pandas as pd
from db import DemoDB

database = DemoDB()
print(database.tables)

#Pegando a tabela de album e artista
album = database.tables.Album.all()
print(album.head())

#PEgando a tabela de artista
artist = database.tables.Artist.all()
print(artist.head())

#Juntando as tabelas
album_artista = pd.merge(artist, album)
print(album_artista.head())

#declarando as ligações
album_artista = pd.merge(artist,album, on = "ArtistId")

#Renomear o Id do artista
album.rename(columns={'ArtistId':'Artist_Id'}, inplace = True)

album_artista = pd.merge(album, 
                         artist, 
                         left_on = 'Artist_Id', 
                         right_on="ArtistId")
print(album_artista.head())

#retirar os campos duplicados
album_artista = pd.merge(album, 
                         artist, 
                         left_on = 'Artist_Id', 
                         right_on="ArtistId").drop('Artist_Id', axis = 1)
print(album_artista.head())

#Conjunto de dados de vendas
#Unir os dados do setores

vendas1 = pd.DataFrame({'nome' : ['Lucas', 'Vinicius'],
                        'codigo' : [10,20]
                        })


vendas2 = pd.DataFrame({'nome' : ['Ana', 'Vinicius', 'Joana'],
                        'valor' : [5000,3500,2020]
                        })

vendas_total = pd.merge(vendas1, vendas2, on = 'nome', how = 'inner')
print(vendas_total.head())

vendas_total = pd.merge(vendas1, vendas2, on = 'nome', how = 'outer')
print(vendas_total.head())

vendas_total = pd.merge(vendas1, vendas2, on = 'nome', how = 'left')
print(vendas_total.head())

vendas_total = pd.merge(vendas1, vendas2, on = 'nome', how = 'right')
print(vendas_total.head())

