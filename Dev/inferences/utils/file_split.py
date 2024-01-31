import os

path = "Amostra/"
dirs = os.listdir(path)

for file in dirs:
    # file name with extension
    file_name = os.path.basename(file)
    l = file_name.split("_")
    email = l[0]
    print(email)
    cultivo_id = l[1]
    print(cultivo_id)
    dateTime = f"{l[2][:4]}-{l[2][4:6]}-{l[2][6:8]} {l[3][:2]}:{l[3][2:4]}:{l[3][4:6]}"
    print(dateTime)