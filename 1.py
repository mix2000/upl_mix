from datetime import datetime
from pathlib import Path

from editable import *
from popup import *
from recreatefile import *
from sendsftp import *

blockFile = "C:/Users/one/Documents/block.txt"
fileWatch = "C:/Users/one/Desktop/list.xlsx"

while True:
    timestamp = editabledate(fileWatch)
    file = Path(blockFile)
    dateFileUpdate = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    if not file.is_file():
        print('Файла не существует')
        recreatefile(blockFile, dateFileUpdate)
        WindowsBalloonTip("Создан файл", "Создан файл - блокировки. Записана новая дата")
        sendsftp(fileWatch)
    else:
        f = open(blockFile)
        dataUpdateBefore = f.read()
        if dataUpdateBefore == dateFileUpdate:
            WindowsBalloonTip("Дата обновления", "Файл не обновлялся")
        else:
            recreatefile(blockFile, dateFileUpdate)
            WindowsBalloonTip("Дата обновления", "Файл обновился - " + dateFileUpdate)
            sendsftp(fileWatch)
            # отправка файла на сайт

    print(dateFileUpdate)
    time.sleep(60 * 10)
    print('Прошло 10 минут')
