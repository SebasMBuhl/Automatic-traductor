import tkinter as tk
from langdetect import detect
from deep_translator import GoogleTranslator
import pycountry
import string
from tkinter import messagebox

# Crear ventana
root = tk.Tk()
root.title("Traductor Automático")
root.geometry("500x400")

# Etiqueta y cuadro de texto para ingresar el mensaje
tk.Label(root, text="Escribe el texto a traducir:").pack(pady=5)
entrada = tk.Text(root, height=5, width=50)
entrada.pack(pady=10)

# Etiqueta y cuadro de texto para idioma destino
tk.Label(root, text="Escribe el idioma destino en inglés (ej. Spanish, French):").pack(pady=5)
entrada_idioma = tk.Entry(root, width=30)
entrada_idioma.insert(0, "Spanish")
entrada_idioma.pack(pady=10)

# Etiqueta para mostrar la traducción
resultado = tk.Label(root, text="", wraplength=400, justify="center")
resultado.pack(pady=20)

# Función para traducir
def trad():
    texto = entrada.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Error", "Escribe un texto primero")
        return

    idioma_origen = detect(texto)

    idioma_destino_nombre = entrada_idioma.get().strip().capitalize()
    target = pycountry.languages.get(name=idioma_destino_nombre)

    if target is None or not hasattr(target, "alpha_2"):
        messagebox.showerror("Error", "Idioma destino no válido. Escribe el nombre en inglés correctamente.")
        return

    traduccion = GoogleTranslator(source=idioma_origen, target=target.alpha_2).translate(texto)
    resultado.config(text=traduccion)

# Botón para traducir
boton = tk.Button(root, text="Traducir", command=trad)
boton.pack(pady=10)

root.mainloop()
