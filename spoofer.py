import os
import shutil
import random
import string
import winreg
import sys
import ctypes
import tkinter as tk
from tkinter import scrolledtext, font
import subprocess
import time

#The %x completed is fake. I added it because it's a project I did when I was younger, and I thought it looked more professional

def cerrar_teamspeak_si_abierto(log_output):
    try:
        result = subprocess.run(['tasklist'], capture_output=True, text=True)
        if "ts3client_win64.exe" in result.stdout:
            insertar_log(log_output, "[*] TeamSpeak detected. Closing...\n", "info")
            subprocess.run(['taskkill', '/F', '/IM', 'ts3client_win64.exe'],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            insertar_log(log_output, "[+] TeamSpeak closed.\n", "success")
            time.sleep(3)
        else:
            insertar_log(log_output, "[i] TeamSpeak isn't open. Proceding...\n", "info")
    except Exception as e:
        insertar_log(log_output, f"[!] Error 92: {e}\n", "error") #when closing teamspeak

def borrar_config_ts3(log_output):
    carpeta = os.path.expandvars(r'%APPDATA%\TS3Client')
    if os.path.exists(carpeta):
        shutil.rmtree(carpeta)
        insertar_log(log_output, "[+] 38% complete.\n", "success")
    else:
        insertar_log(log_output, "[-] Error 92. (Maybe it was spoofed already?)\n", "error")

def generar_id_producto():
    secciones = [
        ''.join(random.choices(string.digits, k=5)),
        ''.join(random.choices(string.digits, k=3)),
        ''.join(random.choices(string.digits, k=7)),
        ''.join(random.choices(string.digits, k=5)),
    ]
    return '-'.join(secciones)

def cambiar_product_id(log_output):
    key_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
    try:
        nuevo_id = generar_id_producto()
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE) as clave:
            winreg.SetValueEx(clave, "ProductId", 0, winreg.REG_SZ, nuevo_id)
            insertar_log(log_output, "[+] 75% complete\n", "success")
    except PermissionError:
        insertar_log(log_output, "[!] Permission denied. Execute as admin.\n", "error")
    except Exception as e:
        insertar_log(log_output, f"[!] Error 33: {e}\n", "error")

def insertar_log(output, texto, tipo):
    output.insert(tk.END, texto, tipo)
    output.see(tk.END)

def spoof(log_output):
    log_output.delete(1.0, tk.END)
    insertar_log(log_output, "[*] Started spoofing...\n", "info")

    cerrar_teamspeak_si_abierto(log_output)
    borrar_config_ts3(log_output)
    cambiar_product_id(log_output)

    insertar_log(log_output, "[✔] Spoofing successfully finished.\n", "success")
    insertar_log(log_output, "[!] Remember to use VPN.\n\n", "info")

def verificar_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()

def main():
    if not verificar_admin():
        print("[!] This script must be run as administrator.")
        sys.exit(1)

    ventana = tk.Tk()
    ventana.title("TS3 Spoofer by alcachofo")
    ventana.geometry("400x300")
    ventana.resizable(False, False)

    salida = scrolledtext.ScrolledText(ventana, width=50, height=10, font=("Courier", 9))
    salida.pack(pady=5)

    # configure styles
    fuente_negrita = font.Font(salida, salida.cget("font"))
    fuente_negrita.configure(weight="bold")
    salida.tag_config("success", foreground="green", font=fuente_negrita)
    salida.tag_config("error", foreground="red", font=fuente_negrita)
    salida.tag_config("info", foreground="blue", font=fuente_negrita)

    boton = tk.Button(ventana, text="Spoof", font=("Arial", 12), command=lambda: spoof(salida))
    boton.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()
