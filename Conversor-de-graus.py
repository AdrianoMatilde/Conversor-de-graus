# Conversor de Gruas  Celsius e Fahrenheit

# Definindo calculos de conversão
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Esolhendo qual conversão executar
opcao = input("Digite '1' para converter de Celsius para Fahrenheit, ou '2' para converter de Fahrenheit para Celsius: ")

if opcao == '1':
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:.2f}°C em Fahrenheit é: {fahrenheit:.2f}°F")

elif opcao == '2':
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit:.2f}°F em Celsius é: {celsius:.2f}°C")
    print("Volte sempre!")

else:
    print("Opção inválida. Por favor, digite '1' ou '2'.")