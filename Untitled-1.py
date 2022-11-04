def files():
    with open('1.txt', encoding= 'utf-8') as f1, open('2.txt', encoding= 'utf-8') as f2, open('fw.txt', 'a', encoding= 'utf-8') as fw:

        count_1= 0
        text_1=[]
        for line in f1:
            count_1+= 1
            text_1.append(f'строка номер {count_1} файла номер 1')

        count_2= 0
        text_2= []
        for line in f2:
            count_2+= 1
            text_2.append(f'строка номер {count_2} файла номер 2')

        #сравниваю, тут я даже не представляю сравнение по другому и если файлов будет больше двух
        a= count_1 > count_2
        if a == True:
            fw.write(f"1.txt\n{count_1}\n")
            for a in text_1:
                fw.write(f'{a}\n')
            fw.write(f"2.txt\n{count_2}\n")
            for b in text_2:
                fw.write(f'{b}\n')
        else:
            fw.write(f"2.txt\n{count_2}\n")
            for b in text_2:
                fw.write(f'{b}\n')
            fw.write(f"1.txt\n{count_1}\n")
            for a in text_1:
                fw.write(f'{a}\n')

files()