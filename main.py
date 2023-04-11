import openai
import config
import typer
from rich import print  #libreria para dar estilos a los print
from rich.table import Table
import os


def limpio_pantalla():
    sisOper = os.name
    if sisOper == "posix":   # si fuera UNIX, mac para Apple, java para maquina virtual Java
        os.system("clear")
    elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
        os.system("cls")


def __prompt() -> str:
    prompt = typer.prompt('\n💬 escribe aquí tu nueva consulta --> ')

    if prompt == "salir":
        exit = typer.confirm("\n🚨¿Estas seguro que quiere salir del programa?")

        if exit:
            ending = typer.style('🖖🏼 Muchas gracias por tus consultas',
                                 fg=typer.colors.GREEN, bold=True)
            typer.echo(ending)
            raise typer.Exit()

        limpio_pantalla()
        mostrar_tabla()
        return __prompt()

    elif prompt == 'nuevo':
        limpio_pantalla()
        mostrar_tabla()
        return __prompt()

    return prompt


def mostrar_tabla():
    print("💬 [bold green]Python y Chat GPT-3[/bold green]")

    table = Table("comando", "descripción del comando")
    table.add_row("salir", "salir del sistema")
    table.add_row("nuevo", "iniciar nuevo chat")

    print(table)
    print("🆕 Nueva conversación creada")


def main():
    limpio_pantalla()

    openai.api_key = config.api_key

    mostrar_tabla()

    # aca le ponemos el contexto en el que queremos que trabaje
    context = {'role': 'system',
               'content': "eres un asistente especializado en el campo IT."}  # podemos colocar cuantas lineas querramos, e incluso definir como va a trabajar nuestra app para asi darle un mayor contexto de trabajo
    # esta variable contiene el contexto por defecto que le asignamos arriba
    messages = [context]

    while True:
        content = __prompt()

        if content == 'nuevo':
            messages = [context]
            content = __prompt()

        # aca le vamos agregando las pregunta que le hacemos al contexto
        messages.append({'role': 'user', 'content': content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)

        # aca capturamos respuesta de chat gpt
        response_content = response.choices[0].message.content

        # aca le vamos agregando las respuestas que le hacemos al contexto
        messages.append({'role': 'assistant', 'content': response_content})

        print(f'[green][bold green]> [/bold green]{response_content}[/green]')


if __name__ == '__main__':
    typer.run(main)
