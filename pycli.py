import os

if os.path.isdir("bin") == False:
    print("This path bin doesnt exist.")
    exit()

mifile = os.listdir("bin")
fileslen = len(mifile)

for i in range(0,fileslen):
    mifile[i] = mifile[i].replace(".py" , "")

path = os.getcwd() + "\\bin\\"

while True:
    cmds = input("PyClI --> ")
    cmds = cmds.split()

    if len(cmds) == 0:
        continue
    
    elif cmds[0] == "exit":
        exit()

    elif cmds[0] == "cd":
        try:
            os.chdir(cmds[1])

        except:
            print("Failed to change directory.") 
        continue
    
    elif cmds[0] in mifile:
        os.system("python3 " + path + cmds[0] + ".py ")
        continue
    
    print("Error , command not found.")    
