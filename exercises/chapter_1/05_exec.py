def convert_celsius_fahrenheit(tempCelsius):
    return (tempCelsius * 9/5) + 32

def main():
    print("Sistema conversor de temperatura")
    print("Graus Celsius para Fahrenheit")
    strIntput = input("\nDigite temperatura em graus Celsius:")
    tempC = float(strIntput)
    tempF = convert_celsius_fahrenheit(tempC)
    print(tempC,"ºC = ",tempF,"ºF")
    
main()