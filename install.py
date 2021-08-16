import os
import time

os.system("clear")

banner_a = "\n __  __ ____      ____   ___  ____   ___ _____ "


banner_b = "\n|  |/  |  _ |    |  _ | / _ || __ ) / _ |_   _|"


banner_c = "\n| ||/| | |_) |   | |_) | | | |  _ || | | || |  "


banner_d = "\n| |  | |  _ <    |  _ <| |_| | |_) | |_| || |  "


banner_e = "\n|_|  |_|_| |_|___|_| |_||___/|____/ |___/ |_|  "


banner_f = "\n            |_____|                            "

banner_x = [banner_a + banner_b + banner_c + banner_d + banner_e + banner_f]



a = ("[==>                        ]10%")
b = ("[====>                      ]15%")
c = ("[=======>                   ]20%")
d = ("[=========>                 ]30%")
e = ("[===========>               ]40%")
f = ("[==============>            ]50%")
g = ("[================>          ]60%")      
h = ("[==================>        ]70%")
i = ("[====================>      ]80%")
j = ("[========================>  ]90%")
k = ("[==========================>]100% COMPLETADO!!!")



carga = [a, b, c, d, e, f, g, h, i, j, k]

for banner_z in banner_x:
    print(banner_z)
print("[1]Instalar Herramienta [2]EXIT")
user_a = int(input("===> "))
if user_a == 1:
    print("\n[*]ACTUALIZANDO SISTEMA[*]")
    print("\nEspera.....")
    os.system("sudo apt update -y > nul")
    for carga_x in carga:
        print(carga_x)
        time.sleep(0.5)
        os.system("clear")
    print("\n[*]INSTALANDO PYTHON[*]")
    print("\nEspere....")
    os.system("sudo apt install python > nul")
    for carga_z in carga:
        print(carga_z)
        time.sleep(0.5)
        os.system("clear")
    print("\n[*]Instalando Python3[*]")
    print("\nEspere......")
    os.system("sudo apt install python3 > nul")
    for carga_a in carga:
        print(carga_a)
        time.sleep(0.5)
        os.system("clear")
    print("\n[*]INSTALANDO LIBRERIAS NECESARIAS[*]")
    os.system("pip3 install colorama > nul")
    for carga_b in carga:
        print(carga_b)
        time.sleep(0.5)
        os.system("clear")
    print("[*] INSTALANDO GIT [*]")
    os.system("sudo apt install git")
    for carga_r in carga:
        print(carga_r)
        time.sleep(0.5)
        os.system("clear")
    print("[ * ]FINALIZANDO DESCARGAS[ * ]")
    os.system("pip3 install gitpython > nul")
    for carga_v in carga:
        print(carga_v)
        time.sleep(0.5)
        os.system("clear")
    os.system("python3 FsocietyTools.py")    

