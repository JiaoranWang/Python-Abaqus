## How to change the execute scripts in runcae.py? Original Exe_1.py, new Exe_2.py
with open("testing.bat", "rt") as bat_file:
    text = bat_file.readlines()
new_text = []
for line in text:
    if "abaqus cae script=" in line:
        # new_text.append(line.replace("Exe_1.py", "Exe_2.py"))
        # Slicing then replacing the string:
        a = line.find('=')
        b = line[a+1:]
        # new_text.append(line.find('abaqus cae script='))
        # print(a)
        # print(b)
        # print(line)
        new_text.append(line.replace(b, "Exe_5.py"))
        print(new_text)
    else:
        new_text.append(line)
with open("testing.bat", "wt") as bat_file:
    for line in new_text:
        bat_file.write(line)