import os
import time
import zipfile
#import zlib

# Файлы и каталоги, которые необходимо скопировать, собираются в список.
# Ваши каталоги для архивирования 
sources =  ["C:\\projects", "C:\\Users\\Zver\\Documents\\ViberDownloads"]
# Для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# Резервные копии должны храниться в основном каталоге резерва.
target_dir = "E:\\Backup" # Подставьте ваш путь.

# Файлы помещаются в zip-архив.
# Текущая дата служит именем подкаталога в основном каталоге.
today = target_dir + os.sep + time.strftime('%Y%m%d') 
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
# И следующий, если надо добавить дополнительный источник
comment = input('Введите комментарий --> ')
add_new_source = input("Введите доп источник архивирования, если надо ")
if len(comment) == 0: # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep +now + '_' + \
        comment.replace('', '_') + '.zip'
    sources.append(add_new_source)

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
    print('Каталог успешно создан', today)

# Метод "zipf" для помещения файлов в zip-архив и сжимаем
zipf = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED)
for source in sources: # проходим все источники для архивирования
    for root, dirs, files in os.walk(source): #итератор по содержимому каталогов
        for file in files:
            fn = os.path.join(root, file)
            zipf.write(fn) # пишем файлы в архив
zipf.close()
   

# проверка создался ли бекап
if zipfile.is_zipfile(fn) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')

