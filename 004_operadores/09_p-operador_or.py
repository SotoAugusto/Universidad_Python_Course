#asistir juego

vacaciones = int(input("Está de vacaciones? \n 1 para sí\n 2 para no\n"))
diaDescanso = int(input("Está de día de descanso? \n 1 para sí\n 2 para no\n"))

if vacaciones == 1:
  vacaciones = True
else:
    vacaciones = False
    

if diaDescanso == 1:
  diaDescanso = True
else:
    diaDescanso = False   
    
    
if vacaciones or diaDescanso == True:
  print(f"------------------------\nPuede asistir al juego.")
else:
    print(f"------------------------\nNo puede asistir al juego, está ocupado")



