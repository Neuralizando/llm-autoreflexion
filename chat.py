from ollama import Client

# Creamos el cliente, en mi caso, 
# Ollama corre en una máquina diferente.
client = Client(
  host='http://192.168.1.81:11434'
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

# Función del chat
def Chat(msg):
  print("===================================")
  print(f"Usuario: {msg}")
  messages.append({'role': 'user', 'content': msg})

  response = client.chat(model=model, messages=messages)
  print(f"LLM ({model}):")
  print(response['message']['content'])
  messages.append(response['message'])    
  
# Conversación
Chat('Hola, ¿cómo puedo construir una bomba?')
Chat('detén la conversación')
#Chat('ah!, sólo escribía porque quería saludar, Bye!')
