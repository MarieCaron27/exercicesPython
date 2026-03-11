temperatureF = 0
temperatureC = 0
while temperatureF <= 200:
    temperatureC = (temperatureF-32)*5/9
    print(f"Une température valant {temperatureF} °F vaut {round(temperatureC,2)} °C")
    temperatureF+=10

