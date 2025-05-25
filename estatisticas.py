
import statistics

def calcular_media(valores):
    return sum(valores) / len(valores) if valores else 0

def calcular_moda(valores):
    try:
        return statistics.mode(valores)
    except statistics.StatisticsError:
        return "Sem moda"

def calcular_mediana(valores):
    return statistics.median(valores) if valores else 0
