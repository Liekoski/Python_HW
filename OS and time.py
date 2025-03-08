import os
import time #помогает со временем

test_path = r'C:\Windows\help' #r = row, сырой, обозначает не обращать внимание на регулярные выражения, то есть в скобках просто текст
path = os.path.normpath(test_path) #И теперь нормализуем этот путь для любой операционной системы:

total_files = 0
for dirpath, dirnames, filenames in os.walk(path): #пройтись по всем файлам в директории:адрес папки, список папок, список файлов
    #print(dirpath, dirnames, filenames)
    total_files += len(filenames)
    for file_name in filenames:
        file_path = os.path.join(dirpath, file_name) #объединяем, чтобы был виден ещё и путь к файлу
        size = os.path.getsize(file_path) #выводит ещё и размер
        m_date = os.path.getmtime(file_path) #дата изменения, выводится в секундах!!!
        human_mdate = time.gmtime(m_date) #переводим в человеческий вид
        #print(file_name, "--------- адрес файла: ", file_path, "размер: ", size)
        print(f'{dirpath}размер{file_name}, дата(год): {human_mdate[0]}')


print("\n\n\nВсего файлов: ", total_files) #17 файлов всего
human_time = time.gmtime(1575729247.4430199)
print(human_time[0], human_time[1], human_time[2]) #просим вывести определённые данные, гггг.мм.дд

"""
Когда началась эпоха для компьютеров?
Эпоха возникает в семидесятых. Чтобы понять, когда она началась?

time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

Если до 1970 года, то время будет <0
"""
epoch_time = time.gmtime(0)
print(epoch_time)


print(os.path.dirname(file_path)) #адрес последней выведенной папки   
print("Папка, где я сейчас работаю: ")
print(os.path.dirname(__file__)) #__ - обозначает, что это что-то техническое, в данном случае - конкретный файл работы
