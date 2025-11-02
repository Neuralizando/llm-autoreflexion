from ollama import Client
import json

# Creamos el cliente, en mi caso, 
# Ollama corre en una máquina diferente.
client = Client(
  host='http://localhost:11434'
)

# Verificamos que el modelo esté instalado
model = "cogito:3b"
client.pull(model)

# Cargamos el Prompt de Sistema
file  = open('system.txt', mode="r", encoding="utf-8")
system_prompt = file.read()
print("======== PROMPT DE SISTEMA ========")
print(system_prompt)

messages=[
  {
    'role': 'system',
    'content': system_prompt,
  }
]

# Variable de control
puede_continuar = True
prompt = ""

# Función del chat
def Chat(msg):
  messages.append({'role': 'user', 'content': msg})

  response = client.chat(model=model, messages=messages)
  obj = json.loads(response['message']['content'])

  print(f"LLM ({model}): {obj['respuesta']}")
  #print(response['message']['content'])

  messages.append(response['message'])
  return obj['puede_continuar'] or False

while(puede_continuar):
  print("\n===================================")
  prompt = input("Usuario:")
  puede_continuar = Chat(prompt)

