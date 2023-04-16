import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import tkinter as tk
from tkinter import messagebox

def check_links():
    # Obtener la URL ingresada por el usuario
    url = entry_url.get()

    try:
        # Realizar una solicitud HTTP a la página web y obtener el contenido HTML
        response = requests.get(url)
        html_content = response.content

        # Analizar el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Detectar enlaces rotos
        broken_links = []
        possible_broken_links = []
        for link in soup.find_all('a'):
            link_url = link.get('href')
            if link_url:
                absolute_url = urljoin(url, link_url)
                link_response = requests.get(absolute_url)
                if link_response.status_code != 200:
                    broken_links.append(absolute_url)
                elif '404' in link_response.text:
                    possible_broken_links.append(absolute_url)
                elif 'error' in link_response.text.lower():
                    possible_broken_links.append(absolute_url)

        # Mostrar resultados en una ventana emergente
        messagebox.showinfo('Resultados', f'Enlaces rotos:\n{broken_links}\n\nPosibles enlaces rotos:\n{possible_broken_links}')
    except:
        # Mostrar un mensaje de error en caso de cualquier excepción
        messagebox.showerror('Error', 'Ocurrió un error al analizar la página web.')

# Crear la ventana de la aplicación
root = tk.Tk()
root.title('Detector de Enlaces Rotos')
root.geometry('400x300')

# Crear etiqueta y campo de entrada para la URL
label_url = tk.Label(root, text='Ingrese la URL de la página web:')
label_url.pack(pady=10)
entry_url = tk.Entry(root, width=50)
entry_url.pack()

# Crear botón de comprobación de enlaces
btn_check = tk.Button(root, text='Comprobar Enlaces', command=check_links)
btn_check.pack(pady=10)

# Iniciar el ciclo de eventos de la ventana
root.mainloop()

        