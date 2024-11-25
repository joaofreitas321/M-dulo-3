from datetime import datetime
import time

while True:
    print(datetime.now())
    hora_atual = datetime.now().strftime("%H:%M:%S")
    print(hora_atual)
    #esperar 1 segundo
    time.sleep(1)