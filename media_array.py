def media_array(array):
    if len(array) == 0:
        print("O array está vazio")
        return
    media = sum(array) / len(array)
    print(f"A média dos números é {media}")

