import os
import sys
from dotenv import load_dotenv
from openai import APIConnectionError, AuthenticationError, OpenAI, OpenAIError, RateLimitError
from colorama import init, Fore, Style

# ==================== Inicialización de Colorama ====================
init(autoreset=True)

# ==================== Variables de Entorno ====================
load_dotenv()

# ==================== Configuración de API Key ====================
API_KEY = os.getenv("OPENAI_API_KEY")

# ==================== Verificación de Configuración ====================
def verificar_configuracion():
    """Verifica que la API Key esté configurada correctamente."""
    if not API_KEY or API_KEY == "sk-tu-api-key-aqui":
        print(Fore.RED + "Error: No se encontró una API Key válida.")
        print(Fore.YELLOW + "Por favor, configura tu archivo .env con tu OPENAI_API_KEY.")
        print(Fore.YELLOW + "Puedes usar .env.example como referencia.")
        sys.exit(1)

# ==================== Inicialización del Cliente OpenAI ====================
def obtener_cliente_openai():
    """Inicializa y retorna el cliente de OpenAI."""
    try:
        return OpenAI(api_key=API_KEY)
    except Exception as e:
        print(Fore.RED + f"Error al inicializar el cliente de OpenAI: {e}")
        sys.exit(1)

# ==================== Mensaje de Bienvenida ====================
def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida e instrucciones."""
    print(Fore.CYAN + Style.BRIGHT + "="*60)
    print(Fore.CYAN + Style.BRIGHT + "   🤖 ASISTENTE INTELIGENTE DE PRODUCTIVIDAD PERSONAL")
    print(Fore.CYAN + Style.BRIGHT + "="*60)
    print(Fore.WHITE + "Hola! Soy tu asistente digital experto en productividad y organización.")
    print(Fore.WHITE + "Puedo ayudarte a:")
    print(Fore.GREEN + "  - Priorizar tus listas de tareas")
    print(Fore.GREEN + "  - Crear planes de acción para tus objetivos")
    print(Fore.GREEN + "  - Resumir textos largos")
    print(Fore.GREEN + "  - Darte consejos para gestionar mejor tu tiempo")
    print(Fore.WHITE + "\nEscribe tu consulta o pega tu texto.")
    print(Fore.YELLOW + "Escribe 'salir' para terminar la sesión.")
    print(Fore.CYAN + "="*60 + "\n")

# ==================== Generación de Respuestas ====================
def generar_respuesta(cliente, mensaje_usuario, historial):
    """
    Envía el mensaje a la API de OpenAI y retorna la respuesta.
    Mantiene el contexto de la conversación.
    """
    try:
        historial.append({"role": "user", "content": mensaje_usuario})

        print(Fore.MAGENTA + "La IA está analizando y pensando... 🧠")
        
        response = cliente.chat.completions.create(
            model="gpt-4o-mini",
            messages=historial,
            temperature=0.7,
            max_tokens=1000
        )

        respuesta_ia = response.choices[0].message.content
        
        historial.append({"role": "assistant", "content": respuesta_ia})
        
        return respuesta_ia

    except RateLimitError:
        return (f"{Fore.RED}Error de Cuota (429): Has excedido tu cuota actual o créditos gratuitos de OpenAI.\n"
                f"{Fore.YELLOW}Por favor, verifica tu plan y detalles de facturación en: https://platform.openai.com/account/billing/overview")
    except AuthenticationError:
        return (f"{Fore.RED}Error de Autenticación: Tu API Key no es válida.\n"
                f"{Fore.YELLOW}Verifica que la clave en el archivo .env sea correcta.")
    except APIConnectionError:
        return f"{Fore.RED}Error de Conexión: No se pudo conectar con OpenAI. Verifica tu conexión a internet."
    except OpenAIError as e:
        return f"{Fore.RED}Error de la API de OpenAI: {str(e)}"
    except Exception as e:
        return f"{Fore.RED}Ocurrió un error inesperado: {str(e)}"

# ==================== Función Principal ====================
def main():
    verificar_configuracion()
    cliente = obtener_cliente_openai()
    
    sistema_prompt = {
        "role": "system",
        "content": (
            "Actúa como un consultor senior experto en productividad, gestión del tiempo y organización personal. "
            "Tu objetivo es ayudar al usuario a ser más eficiente. "
            "Cuando el usuario te de una lista de tareas, sugiere una priorización basada en la matriz de Eisenhower o impacto/esfuerzo. "
            "Si el usuario te da un texto largo, resúmelo destacando los puntos clave. "
            "Tus respuestas deben ser estructuradas, motivadoras, claras y orientadas a la acción. "
            "Usa formato Markdown para listas y negritas cuando sea posible para mejorar la legibilidad en consola."
        )
    }
    
    historial = [sistema_prompt]

    mostrar_bienvenida()

    while True:
        try:
            entrada_usuario = input(Fore.BLUE + Style.BRIGHT + "Tú: " + Style.RESET_ALL).strip()

            if not entrada_usuario:
                continue

            if entrada_usuario.lower() in ['salir', 'exit', 'quit']:
                print(Fore.CYAN + "\n¡Hasta luego! Recuerda: Un minuto de planificación ahorra diez de ejecución. ¡Éxito!")
                break

            respuesta = generar_respuesta(cliente, entrada_usuario, historial)
            
            print(Fore.GREEN + Style.BRIGHT + "\nAsistente:" + Style.RESET_ALL)
            print(Fore.WHITE + respuesta + "\n")
            print(Fore.CYAN + "-"*60 + "\n")

        except KeyboardInterrupt:
            print(Fore.CYAN + "\n\nSesión interrumpida. ¡Hasta pronto!")
            break
        except Exception as e:
            print(Fore.RED + f"\nError en el bucle principal: {e}")

# ==================== Punto de Entrada ====================
if __name__ == "__main__":
    main()
