import os

print("**OS homework**")

hw_path = r'C:\Users\DarkLord\Desktop\opiskelu\Python\os_homework'
print("Все картинки: ") 

total_pictures = []
for dirpath, dirnames, filenames in os.walk(hw_path): #пройтись по всем файлам в директории:адрес папки, список папок, список файлов
    #print(dirpath, dirnames, filenames)
    for file_name in filenames:
        file_path = os.path.join(dirpath, file_name) #объединяем, чтобы был виден ещё и путь к файлу
        if file_name.endswith(".jpg"):
            print(f'{file_path}')

print("\n\nПустые папки: ")

for dirpath, dirnames, filenames in os.walk(hw_path):
    if len(dirnames) == 0 and len(filenames) == 0:
        print(f'{dirpath}')
        
