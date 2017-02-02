#Write in python 3.6, Bugged version, any help?
#Bugs:
#01. The file for output (saida, 'pySaida.mcod') does'nt get any changes.

#impt;
import os;
for raiz, diretorios, arquivos in os.walk('C:Users/Utilizador/Desktop/pyProject_001/'):
    for arquivo in arquivos:
        if arquivo.endswith('.mcod'):
            os.remove(os.path.join(raiz, arquivo))
#arqs;
centrada = open('pyEntrada.mcod', 'w');
csaida = open('pySaida.mcod', 'w');
centrada.close();
csaida.close();
entrada = open('pyEntrada.mcod', 'r+')
saida = open('pySaida.mcod', 'w');

#source;
texto = str(input('Texto para conversão> '));
entrada.write(texto);

for linha in entrada.readlines():
    for letra in linha:
        if letra == 'a':
            saida.write('4');
        else:
            saida.write(letra);

#close()s;
entrada.close();
saida.close();
