import calendar
from pathlib import Path

carpeta_mes= list(calendar.month_name[1:])  # guarda una lista de los meses del años desde el indice 1
carpeta_dias=["dia1","dia2"]  # lista de los dias 1 y 2 se pueden poneer los que se deseen 

for i, meses in enumerate(carpeta_mes):
    for dia in  carpeta_dias:
        Path(f'2024/{i+1}.{meses}/{dia}').mkdir(parents=True, exist_ok=True)
        
        #crea carpetas de calendario,  con path puede crear carpetas automaticas
        #parents es para poder crear sub carpetas y exist_ok es para que no se rompa el codigo con el errorsi ya existe la carpeta