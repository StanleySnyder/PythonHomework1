width = int(input("Введите ширину рамки: "))

height = int(input("Введите высоту рамки: "))

for line in range(height + 1):
    for col in range(width + 1): 
        if col == width or col == 0:
            print('|', end='')
        elif line == height or line == 0:
            print('-', end='')
        else:
            print(' ', end='')
    print()