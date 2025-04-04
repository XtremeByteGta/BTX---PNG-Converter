# BTX to PNG Converter Script  
🚀 A Handy Tool for Converting .btx Files to .png by Xtreme Byte  

---

## What is it?  
BTX to PNG Converter Script is a Python script designed to streamline the process of converting .btx files into .png images. Powered by the ConvertXtremeByte.exe utility, it automates file handling and organizes everything neatly into folders. Created by Xtreme Byte, this tool is perfect for batch processing .btx files with ease!  

---

## Features  
- 🔹 Extracts .btx data — Converts .btx to a temporary .ktx file  
- 🔹 Converts to .png — Uses ConvertXtremeByte.exe for seamless conversion  
- 🔹 Cleans up — Deletes temporary .ktx and .pvr files  
- 🔹 Organizes files — Moves .btx to a btx folder and .png to a png folder  
- 🔹 User-friendly output — Displays progress with a touch of Xtreme Byte flair  

---

## Requirements  
- ✅ Python 3.x — Make sure Python is installed  
- ✅ ConvertXtremeByte.exe — Must be in the same directory as the script  
- ✅ .btx files — Place them in the script’s working directory  

---

## Installation  
1. Download the script (btx_converter.py or name it whatever you like)  
2. Move it to the folder with your .btx files  
3. Ensure ConvertXtremeByte.exe is in the same directory  
4. Install Python if you don’t have it:  
   👉 [Download Python](https://www.python.org/downloads/)  
5. Ready to roll! 🎉  

---

## How to Use?  
1. Open a terminal (or command prompt) in the script’s directory  
2. Run this command:  
   python btx_converter.py  
3. Watch the magic happen: 😎  
   - Creates png and btx folders if they don’t exist  
   - Processes all .btx files in the directory  
   - Shows you the progress with Xtreme Byte’s signature style  

Example Output:  
##################################################  
# Скрипт создан: Xtreme Byte                     #  
##################################################  
Запуск скрипта...  
Создана папка: png by Xtreme Byte  
Создана папка: btx by Xtreme Byte  
Запускаем ConvertXtremeByte.exe для example.ktx (Xtreme Byte)  
Перемещаем example.png в png/example.png (Xtreme Byte)  
Перемещаем example.btx в btx/example.btx (Xtreme Byte)  
Файл example.btx успешно обработан! Спасибо Xtreme Byte  
Обработка завершена! (Xtreme Byte)  
Успешно обработано: 1 из 1 файлов  

---

## Possible Issues  
- Missing ConvertXtremeByte.exe 😕 — Ensure it’s in the same folder as the script  
- No .btx files 😢 — The script will let you know if there’s nothing to process  
- Conversion errors ⚠️ — Any issues from ConvertXtremeByte.exe will show up in the console  

---

## Notes  
- The script keeps your original .btx files safe by moving them to the btx folder  
- Temporary files (.ktx, .pvr) are auto-deleted after conversion  
- Proudly crafted by Xtreme Byte — his mark is all over the output!  

---

## License  
This script is shared "as is". Feel free to use or tweak it however you want. Xtreme Byte isn’t responsible for any hiccups you might run into.  

---

Enjoy converting with style! 🚀 Xtreme Byte approves!
