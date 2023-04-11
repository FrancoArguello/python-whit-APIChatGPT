Está app consume la API de Chat GPT3.

Tambien esta app nos permite configurar el contexto en el cual la inteligencia artifical va a desarrollar las respuestas que nos va a brindar, esto nos permite que las respuestas sean mucho más acotadas y referidas al campo de investigación sobre el cual estamos haciendo la consulta.
La configuración del contexto se hace mediante la variable context la cual va a pasar los datos a través de un diccionario por ejemplo:
context = {
    'role': 'system',
    'content': "eres un asistente especializado en el campo IT, particularmente en el area de Desarrollo backEnd con Python y todas sus librerias disponibles."}

también a medida que le vamos realizando consultas va a ir creardo su contexto automaticamente usando de referencia las preguntas y respuestas, realizadas por le usuario y el sistema.

También se utilizo la libreria rich para poder darle estilos a los print que se van realizando para que la consola se vea más atractiva.