import requests
import sys
import time
import os
import phonenumbers
from dotenv import load_dotenv
from colorama import Style, Back, Fore, init

init()
load_dotenv()
# Colores y estilos
S = Style.BRIGHT
C = Fore.CYAN
R = Fore.RED
B = Fore.BLUE
M = Fore.MAGENTA
G = Fore.GREEN
Bl = Fore.BLACK
Y = Fore.YELLOW
Bb = Back.BLACK
Bw = Back.WHITE


os.system("clear" if os.name == "posix" else "cls")

# Logo
print(C + """
    ▇▇◤▔▔▔▔▔▔▔◥▇▇
    ▇▇▏◥▇◣┊◢▇◤▕▇▇
    ▇▇▏▃▆▅▎▅▆▃▕▇▇
    ▇▇▏╱▔▕▎▔▔╲▕▇▇
    ▇▇◣◣▃▅▎▅▃◢◢▇▇
    ▇▇▇◣◥▅▅▅◤◢▇▇▇
    ▇▇▇▇◣╲▇╱◢▇▇▇▇
""" + G + "T3nshi")

# Animación del título
logo = Bw + S + Bl + """
𝕸𝖘𝖏 𝕺𝖋 𝕬𝖓𝖔𝖓𝖞𝖒𝖔𝖚𝖘
""" + Bb

for l in logo:
    sys.stdout.flush()
    print(l, end="")
    time.sleep(0.05)


#Función verificar
def limpiar_numero(numero):
    numero = numero.replace(" ", "").replace("-", "")  
    try:
        parsed_number = phonenumbers.parse(numero, None)  
        if phonenumbers.is_valid_number(parsed_number):  
            codigo_pais = phonenumbers.region_code_for_number(parsed_number)
            print(G + f"\n🌎 País detectado: {codigo_pais}\n")
            return f"+{parsed_number.country_code}{parsed_number.national_number}"
        else:
            print(R + "❌ Número inválido, intenta de nuevo.")
            return None
    except:
        print(R + "❌ Error al procesar el número. Inténtalo de nuevo.")
        return None



def efecto_carga():
    animacion = ["⠏", "⠛", "⠹", "⠼", "⠶", "⠧"]
    for _ in range(10):
        for char in animacion:
            sys.stdout.write(f"\r{Y}📡 Enviando... {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    print("\n")


#Guardar mensaje
def registrar_mensaje(numero, mensaje, api):
    with open("mensajes_enviados.txt", "a", encoding="utf-8") as f:
        f.write(f"Número: {numero} | Mensaje: {mensaje} | API: {api}\n")



def enviar_textbelt(numero, mensaje):
    respuesta = requests.post("https://textbelt.com/text", {
        "phone": numero,
        "message": mensaje,
        "key": os.getenv("TEXTBELT_KEY", "textbelt"),
    }).json()

    efecto_carga()

    if respuesta.get("success"):
        print(G + "✅ Mensaje enviado con éxito usando Textbelt.")
        registrar_mensaje(numero, mensaje, "Textbelt")
    else:
        print(R + f"❌ Error: {respuesta.get('error', 'Desconocido')}")



def enviar_vonage(numero, mensaje):
    api_key = os.getenv("VONAGE_API_KEY")
    api_secret = os.getenv("VONAGE_API_SECRET")

    url = "https://rest.nexmo.com/sms/json"
    payload = {
        "api_key": api_key,
        "api_secret": api_secret,
        "to": numero,
        "from": "Vonage",
        "text": mensaje,
    }

    respuesta = requests.post(url, data=payload).json()

    efecto_carga()

    if respuesta.get("message-count") == "1" and respuesta["messages"][0]["status"] == "0":
        print(G + "✅ Mensaje enviado con éxito usando Vonage.")
        registrar_mensaje(numero, mensaje, "Vonage")

        saldo_restante = float(respuesta["messages"][0].get("remaining-balance", "0"))
        print(Y + f"📩 Saldo restante: {saldo_restante:.2f} USD")
    else:
        print(R + "❌ Error al enviar el mensaje.")



def seleccionar_api(numero, mensaje):
    while True:
        print(Y + "\n🔹 ELIGE EL MÉTODO DE ENVÍO 🔹\n")
        print(B + "[1] 🚀 Textbelt (Gratis, pero limitado)")
        print(C + "[2] 📡 Vonage/Nexmo (Más estable, pero con costo)")
        print(R + "[3] ❌ Cancelar\n")

        opcion = input(Fore.WHITE + "📌 Selecciona una opción (1, 2 o 3): ")

        if opcion == "1":
            enviar_textbelt(numero, mensaje)
            break
        elif opcion == "2":
            enviar_vonage(numero, mensaje)
            break
        elif opcion == "3":
            print(R + "\n❌ Cancelado.")
            return
        else:
            print(R + "\n❌ Opción inválida. Intenta de nuevo.")


while True:
    numero = None
    while not numero:
        numero_ingresado = input(G + "\n📞 Ingresa el número: " + Fore.WHITE)
        numero = limpiar_numero(numero_ingresado)

    mensaje = input(f"{G}✉️  Mensaje a enviar: " + Fore.WHITE)

    seleccionar_api(numero, mensaje)

    otra_vez = input(G + "\n🔄 ¿Quieres enviar otro mensaje? (S/N): " + Fore.WHITE).strip().lower()
    if otra_vez != "s":
        print(R + "\n👋 Saliendo del programa...")
        break
