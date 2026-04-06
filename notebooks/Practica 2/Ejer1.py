text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# Salida esperada:
# Total de líneas: 19
# Total de palabras: 137
# Promedio de palabras por línea: 7.21

#Calcular total de palabras
palabras = len(text.split()) #Nos devuelve una lista con todas las palabras sin espacios
print(f"total de palabras {palabras}")

#calcular total de lineas
cant_lineas = len(text.splitlines()) #splitelines() divide el texto en una lista usando de separacion '\n'
print(f"total de lineas {cant_lineas}")
print()

promedio = palabras / cant_lineas
print(f"Lineas por encima del promedio: {promedio:.2f}")
cant_palabras = 0
por_encima_del_promedio = []

for linea in text.splitlines():
    cant_palabras_por_linea = len(linea.split())
    if(cant_palabras_por_linea > promedio):
        por_encima_del_promedio.append(linea)
        print(f"{linea} ({cant_palabras_por_linea})")
    #input()
    
