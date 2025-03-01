#MIT License
#
#Copyright (c) 2025 xtreme byte
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import sys
import os
import subprocess
import shutil

AUTHOR = "Xtreme Byte"

def print_author_banner():
    banner = f"""
    ##################################################
    # Скрипт создан: {AUTHOR}                        #
    ##################################################
    """
    print(banner)

def create_directories():
    for folder in ['png', 'btx']:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Создана папка: {folder} by {AUTHOR}")

def process_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Где файл '{file_path}'? (спрашивает {AUTHOR})")
        return False

    with open(file_path, 'rb') as file:
        file.seek(4)
        data = file.read()

    file_name = os.path.splitext(file_path)[0]
    ktx_file_path = f"{file_name}.ktx"

    with open(ktx_file_path, 'wb') as ktx_file:
        ktx_file.write(data)

    print(f"Запускаем ConvertXtremeByte.exe для {ktx_file_path} ({AUTHOR})")
    try:
        result = subprocess.run(["ConvertXtremeByte.exe", "-d", "-i", ktx_file_path], 
                              capture_output=True, 
                              text=True)
        
        if result.returncode != 0:
            print(f"Ошибка при конвертации {ktx_file_path} ({AUTHOR}):")
            print(result.stderr)
            return False

        generated_png = None
        for f in os.listdir("."):
            if f.startswith(file_name) and f.endswith(".png"):
                generated_png = f
                break

        for f in os.listdir("."):
            if f.endswith((".pvr", ".ktx")):
                print(f"Удаляем временный файл: {f} ({AUTHOR})")
                os.remove(f)
            elif f.endswith(".png") and f == generated_png:
                dest = os.path.join("png", f)
                print(f"Перемещаем {f} в {dest} ({AUTHOR})")
                shutil.move(f, dest)

        dest_btx = os.path.join("btx", os.path.basename(file_path))
        print(f"Перемещаем {file_path} в {dest_btx} ({AUTHOR})")
        shutil.move(file_path, dest_btx)

        print(f"Файл {file_path} успешно обработан! Спасибо {AUTHOR}")
        return True

    except Exception as e:
        print(f"Произошла ошибка: {str(e)} (сообщает {AUTHOR})")
        return False

def main():
    print_author_banner() 
    print("Запуск скрипта...")
    create_directories()

    btx_files = [f for f in os.listdir(".") if f.lower().endswith(".btx")]

    if not btx_files:
        print(f"В текущей директории не найдено .btx файлов ({AUTHOR}).")
        sys.exit(1)

    successful = 0
    for file_path in btx_files:
        if process_file(file_path):
            successful += 1

    print(f"\nОбработка завершена! ({AUTHOR})")
    print(f"Успешно обработано: {successful} из {len(btx_files)} файлов")
    sys.exit(0 if successful > 0 else 1)

if __name__ == "__main__":
    main()
