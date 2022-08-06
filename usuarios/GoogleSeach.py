import pyttsx3
import webbrowser
from googlesearch import search


class busqueda:
		engine = pyttsx3.init()
		voices = engine.getProperty('voices')
		engine.setProperty('voice', voices[1].id)
		engine.say("¿Que quieres buscar en Google?")
		engine.runAndWait()
		buscar = search(input("¿Que quieres buscar en Google?: \n"), num_results=5)
		print(f"Paginas relacionadas con tu busqueda: \n{buscar}")
		engine.say("Paginas relacionadas con tu busqueda")
		engine.runAndWait()
		engine.say("La Buqueda es de 1 a 5 resultados seleciona la que quieres ver.")
		engine.runAndWait()
        
		op = int()
		op = 1
		op = 2
		op = 3
		op = 4
		op = 5

		op = int(input("La Buqueda es de 1 á 5 resultados: "))

		if op ==1:
    			print(webbrowser.open_new(buscar[0]))
		else:
    			False

		if op ==2:
    			print(webbrowser.open_new(buscar[1]))
		else:
			False			
										
		if op ==3:
    			print(webbrowser.open_new(buscar[2]))
		else:
			False											
    									
		if op ==4:
    			print(webbrowser.open_new(buscar[3]))
		else:
			False

		if op ==5:
    			print(webbrowser.open_new(buscar[4]))
		else:
			False	
