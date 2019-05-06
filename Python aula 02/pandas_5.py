# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:52:35 2019

@author: Aluno 10
"""

from db import DB

print("===Carregando os dados do sqlite para o python")

database = DB(filename = 'logs.sqlite3', dbtype = 'sqlite')


print(database.tables)

print("===tabela")
log_df = database.tables.log
log_df
print("===O comando database traz vazio, se quiser os dados precisa usar o all")
log_df = database.tables.log.all()
print(log_df)

print("===Usar com select")
log_df = database.query('select * from log where user_id = 3')
print(log_df)


