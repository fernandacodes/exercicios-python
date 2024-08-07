from sequencia_numerica import sequencia_numerica
from tabuada import tabuada
from media_idades import media_idades
from maior_e_menor import maior_e_menor
from positivo_ou_negativo import positivo_ou_negativo
from soma_array import soma_array
from media_array import media_array
from maior_string import maior_string
from inverter_array import inverter_array
from maior_intervalo import maior_intervalo

if __name__ == "__main__":
    print("Sequência Numérica:")
    sequencia_numerica()
    
    print("\nTabuada do 5:")
    tabuada(5)
    
    print("\nMédia de Idades (10, 20, 30):")
    media_idades(10, 20, 30)
    
    print("\nMaior e Menor (10, 20, 30):")
    maior_e_menor(10, 20, 30)
    
    print("\nPositivo ou Negativo (10):")
    positivo_ou_negativo(10)
    
    print("\nSoma dos Números do Array [1, 2, 3, 4, 5]:")
    soma_array([1, 2, 3, 4, 5])
    
    print("\nMédia dos Números do Array [1, 2, 3, 4, 5]:")
    media_array([1, 2, 3, 4, 5])
    
    print("\nMaior String do Array ['Amarelo', 'Banana', 'Azul', 'Peixe']:")
    maior_string(["Amarelo", "Banana", "Azul", "Peixe"])
    
    print("\nArray Invertido [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:")
    inverter_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    print("\nMaior Intervalo entre Letras na String 'AAAABBBAABABBAAAAAAABBA':")
    maior_intervalo("AAAABBBAABABBAAAAAAABBA")
