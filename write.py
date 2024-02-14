from pathlib import Path
import time

file_name = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

# Making .txt log file
Path(f'./Log/{file_name}.txt').touch()

f = open(f"./Log/{file_name}.txt","a")

for i in range(10):
    f.write("HELLO !!! \n")