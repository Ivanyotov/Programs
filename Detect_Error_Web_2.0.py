import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import tkinter as tk
from tkinter import ttk, messagebox

def check_links():
    # Deshabilitar botón de comprobación de enlaces y reiniciar barra de progreso
    btn_check['state'] = tk.DISABLED
    progress_bar['value'] = 0
    root.update()

    # Obtener la URL ingresada por el usuario
    url = entry_url.get()

    try:
        # Realizar una solicitud HTTP a la página web y obtener el contenido HTML
        response = requests.get(url)
        html_content = response.content

        # Analizar el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Detectar enlaces rotos, internos y externos
        broken_links = []
        internal_links = []
        external_links = []
        links = soup.find_all('a')

        for i, link in enumerate(links):
            link_url = link.get('href')
            if link_url:
                absolute_url = urljoin(url, link_url)
                parsed_base_url = urlparse(url)
                parsed_link_url = urlparse(absolute_url)

                if parsed_base_url.netloc == parsed_link_url.netloc:
                    internal_links.append(absolute_url)
                else:
                    external_links.append(absolute_url)

                link_response = requests.get(absolute_url)
                if link_response.status_code != 200:
                    broken_links.append(absolute_url)

            progress_bar['value'] = (i + 1) * 100 / len(links)
            root.update()

        # Mostrar resultados en una ventana emergente
        messagebox.showinfo(
            'Resultados',
            f'Enlaces rotos ({len(broken_links)}):\n{broken_links}\n\nEnlaces internos ({len(internal_links)}):\n{internal_links}\n\nEnlaces externos ({len(external_links)}):\n{external_links}'
        )
    except:
        # Mostrar un mensaje de error en caso de cualquier excepción
        messagebox.showerror('Error', 'Ocurrió un error al analizar la página web.')

    # Habilitar botón de comprobación de enlaces y reiniciar barra de progreso
    btn_check['state'] = tk.NORMAL
    progress_bar['value'] = 0

# Crear la ventana de la aplicación
root = tk.Tk()
root.title('Detector de Enlaces Rotos')
root.geometry('600x400')

# Crear etiqueta y campo de entrada para la URL
label_url = ttk.Label(root, text='Ingrese la URL de la página web:')
label_url.pack(pady=10)
entry_url = ttk.Entry(root, width=50)
entry_url.pack()

# Crear botón de comprobación de enlaces
btn_check = ttk.Button(root, text='Comprobar Enlaces', command=check_links)
btn_check.pack(pady=10)

# Crear barra de progreso
progress_bar = ttk.Progressbar(root, orient='horizontal', length=500, mode='determinate')
progress_bar.pack(pady=10)

# Iniciar el ciclo de eventos de la ventana
root.mainloop()