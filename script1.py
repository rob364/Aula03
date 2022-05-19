import os

# Para o arquivo dados1.txt

arquivo1 = open("dados1.txt") #cminho relativo
arquivo2 = open("C:/Aula03 python/Aula03/dados1.txt")#caminho absoluto

arquivo3 = open("Documentos/dados2.txt") #cminho relativo
arquivo4 = open("C:Documentos/dados2.txt")#caminho absoluto


print(os.path.relpath(arquivo1.name))
print(os.path.relpath(arquivo1.name))

print(arquivo1)

