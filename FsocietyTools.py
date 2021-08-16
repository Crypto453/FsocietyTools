import os
import time
import git

os.system("clear")

banner_a = " _____               _      _        _____           _     "

banner_b = "|  ___|__  ___   ___(_) ___| |_ _   |_   _|__   ___ | |___ "

banner_c = "| |_ / __|/ _ | / __| |/ _ | __| | | || |/ _ | / _ || / __|"

banner_d = "|  _||__ | (_) | (__| |  __/ |_| |_| || | (_) | (_) | |__ |"

banner_e = "|_|  |___/|___/ |___|_||___||__||__, ||_||___/ |___/|_|___/"

banner_f = "                                 |___/                      "

banner = [banner_a, banner_b, banner_c, banner_d, banner_e, banner_f]

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

carga_a = [a, b, c, d, e, f, g, h, i, j, k]

opciones_a = ["[ 1 ] Envio de mensajes Anonimos", "[ 2 ] Fuerza Bruta", "[ 3 ] VPN", "[ 4 ] TorBrowser", "[00] Salir"]

opciones_b = ["[ 1 ] SETSMS", "[ 2 ] GOD-KILLER", "[ 3 ] TBomb", "[ 00 ] Volver"]

opciones_c = ["[ 1 ] Brutex ", "[ 2 ] Hydra", "[ 3 ] cupp", "[ 4 ] Medusa", "[ 5 ] Crunch", "[00] Volver"]

opciones_d = ["[ 1 ] VPNBOOK", "Por Ahora solo e conseguido vpn gratuitas \nde vpnbook"]

vpn_book = ["[ 1 ] PL226 OpenVPN Certificate Bundle", "[ 2 ] CA198 OpenVPN Certificate Bundle", "[ 3 ] FR1 OpenVPN Certificate Bundle (optimized)", "[ 4 ] FR8 OpenVPN Certificate Bundle", "[ 5 ] LEER" ,"[00] Volver"]



for banner_x in banner:
    print(banner_x)
    time.sleep(0.5)
print("Creador: @Crypto_453")
time.sleep(1)
for op_x in opciones_a:
    print(op_x)
    time.sleep(1)
user_a = int(input("===> "))
if user_a == 1:
    os.system("clear")
    for banner_v in banner:
        print(banner_v)
    for op_z in opciones_b:
        print(op_z)
        time.sleep(1)
    user_b = int(input("===> "))
    if user_b == 1:
        os.system("clear")
        us_a = input("Escriba la ruta: ")
        git.Git(f"{us_a}").clone("https://github.com/Darkmux/SETSMS")
        os.system("python3 FsocietyTools.py")
        for ca in carga_a:
            print(ca)
            time.sleep(0.5)
            os.system("clear")
    elif user_b == 2:
        us_b = input("Escriba la ruta: ")
        git.Git(f"{us_b}").clone("https://github.com/FDX100/GOD-KILLER")
        os.system("python3 FsocietyTools.py")
        for ca_a in carga_a:
            print(ca_a)
            time.sleep(0.5)
            os.system("clear")
    elif user_b == 3:
        us_c = input("Escriba la ruta: ")
        git.Git(f"{us_c}").clone("https://github.com/TheSpeedX/TBomb")
        os.system("python3 FsocietyTools.py")
        for ca_b in carga_a:
            print(ca_b)
            time.sleep(0.5)
            os.system("clear")
    elif user_b == 00:
        os.system("python3 FsocietyTools.py")
    else:
        print("ERROR!!!")
        os.system("python3 FsocietyTools.py")    

elif user_a == 2:
    os.system("clear")
    for banner_z in banner:
        print(banner_z)
    for force in opciones_c:
        print(force)
        time.sleep(0.5)
    user_c = int(input("===> ")) 
    if user_c == 1:
        us_d = input("Escriba la ruta: ")   
        git.Git(f"{us_d}").clone("https://github.com/1N3/BruteX")
        for carga_u in carga_a:
            print("carga_u")
            time.sleep(0.5)
            os.system("clear")
        os.system("python3 FsocietyTools.py")
    elif user_c == 2:
        os.system("sudo apt install -y hydra > nul")
        for carga_t in carga_a:
            print(carga_t)
            time.sleep(0.5)
            os.system("clear")
        os.system("python3 FsocietyTools.py")
    elif user_c == 3:
        us_f = input("Escriba la ruta: ")
        git.Git(f"{us_f}").clone("https://github.com/Mebus/cupp")
        for carga_n in carga_a:
            print(carga_n)
            time.sleep(0.5)
            os.system("clear")
        os.system("python3 FsocietyTools.py")
    elif user_c == 4:
        os.system("sudo apt install -y medusa  > nul")
        for carga_y in carga_a:
            print(carga_y)
            timr.sleep(0.5)
            os.system("clear")
        os.system("python3 FsocietyTools.py")
    elif user_c == 5:
        os.system("sudo apt install -y crunch")
        for carga_b in carga_a:
            print(carga_b)
            time.sleep(0.5)
            os.system("clear")
        os.system("python3 FsocietyTools.py")  
    elif user_c == 00:
        os.system("python3 FsocietyTools.py")
    else:
        print("ERROR!!!!")
        os.system("python3 FsocietyTools.py")
elif user_a == 3:
    os.system("clear")
    for banner_aa in banner:
        print(banner_aa)
    for vpn_a in vpn_book:
        print(vpn_a)
        time.sleep(0.5)
    user_d = int(input("===> "))
    if user_d == 1:
        os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-PL226.zip > nul")
        for loading_a in carga_a:
            print(loading_a)
            time.sleep(0.3)
            os.system("clear")
        os.system("python3 FsocietyTools.py")
    elif user_d == 2:
        os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-CA198.zip > nul")
        for loading_b in carga_a:
            print(loading_b)
            time.sleep(0.4)
            os.system("clear")
        os.system("python3 FsocietyTools.py")
    elif user_d == 3:
        os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-FR1.zip > nul")
        for loading_c in carga_a:
            print(loading_c)
            time.sleep(0.3)
            os.system("clear")
        os.system("python3 FsocietyTools.py")
    elif user_d == 4:
        os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-FR8.zip > nul")
        for loading_d in carga_a:
            print(loading_d)
            time.sleep(0.3)
            os.system("clear")
        os.system("python3 FsocietyTools.py")
    elif user_d == 5:
        print("Saludos \nHe encontrado algunos vpn gratuitos en \nla pagina oficial de vpnbook aqui led dejo la pagina")
        time.sleep(3)
        print("https://www.vpnbook.com/")
        time.sleep(3)
        print("Las descargas de las vpn se guardaran en la ruta actual")
        time.sleep(3)
        print("para usarlo deben extraer el zip con unzip <nombre del vpn>")
        time.sleep(3)
        print("su uso es algo como esto \n sudo openvpn 'nombre del vpn, luego les pedira la contraseña root \nponer el usuario y contraseña que esta en la pagina oficial'")
        time.sleep(3)
        print("Los vpn se guardaran en la carpeta actual")
        os.system("pwd")
    elif user_d == 6:
        os.system("python3 FsocietyTools.py")
    else:
        print("ERROR!!!" * 10)
        os.system("pyhon3 FsocietyTools.py")
elif user_a == 4:
    print("Debes ir a la siguiente pagina y descargar la version para linux.")
    time.sleep(1)
    print("https://www.torproject.org/download/")
elif user_a == 00:
    os.system("python3 FsocietyTools.py")
else: 
    print("ERROR!!!!")
    os.system("python3 FsocietyTools.py")
            

        






                


