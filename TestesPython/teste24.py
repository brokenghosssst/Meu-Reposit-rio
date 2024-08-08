import csv
import pandas as pd

archive = open("empregados.csv")

reader = csv.reader(archive,delimiter=";")
for line in reader:
    print(line)

print(archive)

archive.close 

arquivo = open("produtos.csv")

leitor = csv.reader(arquivo,delimiter=";")
for linha in leitor:
    print(linha)

print(arquivo)

archive.close

nome_usuario = input("Informe o nome do usuário:")
print(f"Nome do usuário é: {nome_usuario}")

arquivo = ("produtos.csv")
df = pd.read_csv('produtos.csv', delimiter=";")
print(df)

arquivo.close

nome_usuario = input("Informe o nome do usuário:")
print(f"Nome do usuário é: {nome_usuario}")

arquivo = ("empregados.csv")
df = pd.reader_csv('empregados.csv', delmiter=";")
print(df)