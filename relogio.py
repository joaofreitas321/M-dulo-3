from datetime import datetime
import time
despertou = False
while True:
    print(datetime.now())
    hora_atual = datetime.now().strftime("%H:%M:%S")
    print(hora_atual)
    #esperar 1 segundo
    time.sleep(1)
    if datetime.now().hour >= 16 and datetime.now().minute >= 35 and datetime.now().second >= 0 and despertou == False:
        print("ACORDA!!!!!!")
        despertou = True