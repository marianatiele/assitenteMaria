import webbrowser

# Defina o caminho do executável do Opera
path_to_opera = 'C:/Users/maria/AppData/Local/Programs/Opera/launcher.exe'

# Registre o navegador Opera
webbrowser.register('opera', None, webbrowser.BackgroundBrowser(path_to_opera))

def search(frase):
    url = 'https://www.google.com/search?q=' + frase
    webbrowser.get('opera').open(url)

# Teste a função
search('exemplo de pesquisa')
