import matplotlib.pyplot as plt
import numpy as np
import webbrowser
 
#Definimos una lista con paises como string
paises = ['Estados Unidos', 'España', 'Mexico', 'Rusia', 'Japon']
#Definimos una lista con ventas como entero
ventas = [25, 32, 34, 20, 25]
 
fig, ax = plt.subplots()
#Colocamos una etiqueta en el eje Y
ax.set_ylabel('Ventas')
#Colocamos una etiqueta en el eje X
ax.set_title('Cantidad de Ventas por Pais')
#Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
plt.bar(paises, ventas)
plt.savefig('barras_simple.png')
#Finalmente mostramos la grafica con el metodo show()
# plt.show()




# url = 'https://pythonexamples.org'
# webbrowser.register('chrome',
# 	None,
# 	webbrowser.BackgroundBrowser("/usr/bin/google-chrome-stable"))
# webbrowser.get('chrome').open(url)


import webbrowser

url = 'barras_simple.png'

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
chrome_path = '/usr/bin/google-chrome %s'
#chrome_path = '/usr/bin/google-chrome-stable %s'

webbrowser.get(chrome_path).open(url)