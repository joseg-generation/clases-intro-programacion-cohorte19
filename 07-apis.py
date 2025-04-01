
# importar el módulo
import requests

def trivia_fetch(num):
 respuesta = requests.get(f"http://numbersapi.com/{num}?json") # obtener
 trivia = respuesta.json()
 return trivia


def main():
  number = input("Ingresa un número: ")
  response = trivia_fetch(number)
  print(f"Para el número {response["number"]}, la respuesta es: ")
  print(response["text"])






if __name__=="__main__":
  main()


