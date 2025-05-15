import re
from collections import Counter

def contar_palavras(texto):
    palavras_limpas = re.sub(r'[^\w\s]', '', texto).lower()
    words = palavras_limpas.split()
    return dict(Counter(words))

texto = input("Escreva algo para contar as palavras: ")
print(contar_palavras(texto))