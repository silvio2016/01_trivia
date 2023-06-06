 import json

def generar_trivia():
    # Aquí puedes definir tus preguntas y respuestas para el juego de trivia
    preguntas = [
        {
            "enunciado": "Pregunta 1",
            "opciones": ["Opción A", "Opción B", "Opción C", "Opción D"],
            "respuesta_correcta": 0,
            "explicacion": "Explicación de la respuesta correcta para la Pregunta 1."
        },
        {
            "enunciado": "Pregunta 2",
            "opciones": ["Opción A", "Opción B", "Opción C", "Opción D"],
            "respuesta_correcta": 1,
            "explicacion": "Explicación de la respuesta correcta para la Pregunta 2."
        },
        # Agrega más preguntas aquí
    ]

    trivia = {
        "preguntas": preguntas
    }

    json_trivia = json.dumps(trivia)
    return json_trivia

# Generar el JSON con preguntas y respuestas de la trivia
json_trivia = generar_trivia()
print(json_trivia)
