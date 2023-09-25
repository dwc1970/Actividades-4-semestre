
# dar formato a un string

nombre = 'Dario'
edad = 52
mensaje_con_formato = 'Mi nombre es %s y tengo %s años' % (nombre, edad)
print(mensaje_con_formato)

# Creamos una tupla
persona = ('Mericia', 'Maya', 5000.00)
mensaje_con_formato = 'Hola %s %s , Tu sueldo es %.2f' % persona # Aqui le pasamos el objeto que es la tupla
print(mensaje_con_formato)

nombre = 'Juan'
edad = 19
sueldo = 3000
mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'. format(nombre,edad, sueldo)
print(mensaje_con_formato)

mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje)

diccionario = {'nomre' : 'ivan', 'Edad' : '35', 'Sueldo': 8000.00}
mensaje = 'Nombre {persona[nombre]}'.format(persona=diccionario)
print(mensaje)