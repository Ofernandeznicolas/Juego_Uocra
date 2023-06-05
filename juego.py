## JUEGO - PELEA DE CAMPEONES -
import random
import sys

# Variables de Daño - Escudo - Vida segun la clase del guerrero
dañoGuerrero = (80, 70, 60)
vidaGuerrero = (250, 220, 200)
escudoGuerrero = (150, 120, 100)

dañoMago = (60, 50, 40)
vidaMago = (350, 300, 250)
escudoMago = (100, 80, 50)

dañoDefensa = (30, 20, 10)
vidaDefensa = (500, 450, 400)
escudoDefensa = (200, 150, 100)

# Defino la clase Campeon
class campeon:
    def __init__(self,nombreUsuario, nombreCampeon, clase, vida, daño, escudo):
        self.nombreUsuario = nombreUsuario
        self.nombreCampeon = nombreCampeon
        self.clase = clase
        self.vida = vida
        self.daño = daño
        self.escudo = escudo

        
    def caracteristicas(self): # presentacion
        print(f"Bienvenido {self.nombreUsuario} a la Arena de combate \n")
        print(f"\n Su CAMPEON {self.nombreCampeon} esta listo para la pelea y estas son sus caracteristicas : \n")
        print("Clase Campeon: ", self.clase)
        print("Vida :", self.vida)
        print("Daño : ", self.daño)
        print("Escudo : ", self.escudo)
    
    def actualizacion(self): # actualizacion de personaje
        print(f"Campeon : ",self.nombreCampeon)
        print(f"Clase : ", self.clase)
        print(f"Vida : ", self.vida)
        print(f"Escudo : ",self.escudo)
    
        
    def atacarEscudo(self,enemigo):
        if self.clase ==  "guerrero":
            if enemigo.clase == "mago":
                daño = self.daño * 0.75
                if daño >= enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo
                    print(f"Excelente, tu daño de {daño} poder rompio con el escudo de tu rival apesar de que es un Mago, \n ahora esta vulnerable, acabalo ! \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    print(f"\n Tu ataque infigio daño directo sobre la vida de tu enemigo, su vida esta bajando! \n ahora su vida es de {enemigo.vida}\n")
                    return enemigo.vida
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Estas intentandolo contra un Mago vas bien ... \n Con tu ataque de {daño} de poder no rompiste su escudo lo dañaste, \n ahora su escudo esta debilitado y bajo a {enemigo.escudo}\n")
                    return enemigo.escudo
                    
            if enemigo.clase == "guardian":
                daño = self.daño * 1.25
                if daño >= enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo
                    print(f"Oh !! Este ataque de {daño} de daño rompio escudo del Guardian apesar de su resistencia, aprovecha tu velocidad y liquidalo ! \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    print(f"Veo que este ataque lastimo al Guardian, esa herida le esta costando valor a su vida que ahora es de {enemigo.vida}\n")
                    return enemigo.vida
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Muy dificil penetrar el escudo de un Guardian, y menos con {daño} de daño, verdad? \n Aunque no rompiste su escudo lo dañaste, su escudo bajo a {enemigo.escudo}\n")
                    return enemigo.escudo
            
        if self.clase == "mago": 
            if enemigo.clase == "guerrero":
                daño = self.daño * 1.25
                if daño >= enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo
                    print(f"Este Guerrero no debio meterse con un mago, tu poderoso ataque de {daño} de daño rompio su escudo, ahora sentira el miedo de un ser oscuro \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    print(f"Tu ataque no solo atraveso su escudo sino que infligio daño a su vida, ahora su vida es de {enemigo.vida}\n")
                    return enemigo.vida
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Apesar de tu ventaja de Mago no rompiste el escudo de este Guerrero con {daño} de daño, \n De todas formas lo dañaste y quedo en {enemigo.escudo}\n")
                    return enemigo.escudo
                    
            if enemigo.clase == "guardian":
                daño = self.daño * 0.75
                if daño >= enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo
                    print(f"Decian que un mago no podia hacerle frente a un Guardian? \n Mira con ese ataque de {daño} poder como lo dejaste sin escudo por completo \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    print(f"Ademas tu ataque lastimo a este Guardian, la magia resto su vida que ahora es de {enemigo.vida}\n")
                    return enemigo.vida
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Te lo dije, un Mago debe esforzarse mas si quiere romper el gran escudo de un Guardian\n No alcanza con un ataque de {daño} poder \n Igual lo dañaste, ahora su escudo bajo a {enemigo.escudo}\n")
                    return enemigo.escudo
        
        if self.clase == "guardian":
            if enemigo.clase == "guerrero":
                daño = self.daño * 0.75
                if daño >= enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo
                    print(f"Y decian que los Guardianes no tenian poder \n Pero con {daño} de daño quebraste en mil pedazos su escudo, \n  Ahora ve por su vida \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    print(f"Aunque no solo dañaste su escudo, hiciste daño directo sobre su vida que ahora es de {enemigo.vida}\n")
                    return enemigo.vida
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Debes esforzarte mas si quieres matar a un Guerrero, \nSu vida sera baja pero tu daño {daño} de poder es mas bajo \n Aun asi dañaste su escudo y ahora su proteccion es de {enemigo.escudo}\n")
                    return enemigo.escudo
                    
            if enemigo.clase == "mago":
                daño = self.daño * 1.25
                if daño >= enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo
                    print(f"Puedo ver la cara de preocupacion de ese Mago,\n tu daño de {daño} lo dejo sin escudo, esta indefenso, su oscuridad pronto vera la luz ! \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    print(f"No solo esta preocupado, tiembla, esta asustado, dañaste su vida y ahora esta bajando!! \n Ahora su vida es de {enemigo.vida}\n")
                    return enemigo.vida
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Ese Mago es muy escurridizo, \n Con {daño} de poder todavia no rompiste su escudo lo dañaste, ahora esta debilitado y bajo a {enemigo.escudo}\n")
                    return enemigo.escudo        
    
    def atacarVida(self,enemigo):
        pass    
    
    def matar(self,enemigo):
        pass   
               

## Defino si el ataque mata al enemigo, baja el escudo o ataca sobre la vida

def Atacar(Campeon,Enemigo):
    
    if Enemigo.escudo > 0:
        return Campeon.atacarEscudo(Enemigo)
        
        
    if Enemigo.escudo < 0 and Campeon.daño > Enemigo.vida:
        return Campeon.atacarVida(Enemigo)
        
    if Enemigo.vida < Campeon.daño:
        return Campeon.matar(Enemigo)

        
# Pido ingresar los datos del campeon 1
Nombre_Usuario1 = input("Bienvenido a la lucha de campeones, ahora ingrese el nombre del dueño del Campeon : \n")
Campeon1 = input("Ahora ingrese el nombre de su valiente Campeon : \n")



clases = ["guerrero","mago","chiken", "guardian"]
# Defino la clase del campeon
def Clase_Campeon():
    ClaseCampeon2 = input(f"""Percecto! Ahora debemos definir a que clase pertenece su Campeon {Campeon1}
                          
                      Indique la opcion correcta : 
                      
                      
                      Guerrero : Estos grandes luchadores son reconocidos por su enorme poder de daño, 
                      pero ojo, debido a su contextura no pueden cargar con grandes escudos por lo que su proteccion es media
                      lo que tendras que tener en cuenta, ya que su vida es del nivel mas bajo de todas las clases de campeones. \n
                       
                      Mago : Seres oscuros con habilidades extrañas que poseen un poder de daño intermedio,
                      debido a su contextura chica portan los escudos de menor nivel del todo el reino
                      pero poseen un nivel de vida intermedia, mayor a los guerreros pero menor a los defensas.
                      
                      
                      Defensa : - Los Guardianes protectores de inumerables objetos de valor tienen un poder de daño muy bajo
                      pero son famosos por poseer los escudos mas fuertes y por si no fuera poco
                      poseen mucha vida lo que los vuelves unos campeones dificiles de derribar.
                      
                      
                      
                      --- Deberas tener en cuenta ----
                      
                      -Clase Guerrero:  Tiene una mayor eficacia contra los -Guardianes- ya que son muy lentos para moverse y esquivar ataques
                      pero ten cuidado! Su debilidad son los -Magos- son muy escurrudizos y engañadores, por lo que es dificil impactar un golpe completo.
                      
                      
                      -Clase Guardian:  Como ya te dije, su debilidad son los -Guerreros- cuando estos atacan reciben el daño completo, 
                      pero a la hora de enfrantar a los -Magos- cuentan con una ventaja de tener resistencia en su adn contra la magia. 
                      
                    
                      -Clase Mago:      Su daño es mayor contra los -Guerreros- que tienen mas debilidad por la magia, 
                      pero pueden volverse vulnerables contra los grandes -Guardianes- quienes reciben sus daños directos para atraparlos y atacarlos.
                      
                      
                      Ahora dime.... Cual sera tu clase?? .... 
                      
                      Guerrero - Mago - Guardian \n""").lower() 
    
    contador = 0
    
    while ClaseCampeon2.lower() not in clases:
        contador += 1

        if contador == 2:
            print("""Enfrentarte a otro campeon es mucho para ti, voy a darte una ultima oportunidad, de lo contrario seras considerado una Gallina \n
                coc co co coc .... coc co co coc ... coc co co coc ...\n""")
            
        if contador == 3:
            print("""De golpe te teletransportas a tu silla en el curso, miras hacia todos lados y ves como todos te miran y mormuran....
                    solo puedes escuchar sus carcajadas y cara de verguenza ajena al verte, has perdido tu valentia, pero calma,
                    no todos estamos hechos para la lucha, puedes ser quien hidrate a los campeones, ahora ve y trae cerveza a todo el mundo!!""")
            ClaseCampeon2 = "chiken"
            break

        
            
        ClaseCampeon2 =input(""" Entraste en panico y no supiste que clase elegir....\n
                Deberas ingresar nuevamente tu opcion o huye!!!   ... Que elijes? :\n
                Puedes ingresar nuevamente la clase de tu campeon, vamos solo escribela, no seas 'gallina'
                Puedes pedir que te vuelvan a mandar al menu de clases por si tu memoria es mala solo pon : 'Menu' 
                O simplementes puedes renunciar y seras enviado al publico donde se reiran de ti por tu cobardia, solo pon : 'Gallina' \n""").lower()
       
        if ClaseCampeon2.lower() == "menu":
            ClaseCampeon2 = Clase_Campeon() 
        if ClaseCampeon2.lower() == "gallina":
            print("""\n De golpe te teletransportas a tu silla en el curso, miras hacia todos lados y ves como todos te miran y mormuran....
                solo puedes escuchar sus carcajadas y cara de verguenza ajena al verte, has perdido tu valentia, pero calma,
                no todos estamos hechos para la lucha, puedes ser quien hidrate a los campeones, ahora ve y trae cerveza a todo el mundo!!""")
            ClaseCampeon2 = "chiken"
    
    
    if ClaseCampeon2.lower() == "chiken":
        print("El juego finaliza ")
        sys.exit()
    
    
    
    
    return ClaseCampeon2


ClaseCampeon1 = Clase_Campeon()

print("""
      
      """)


# Asigno los valores de los atributos de los campeones de forma aleatoria segun su clase
def VidaDañoEscudo(atributos):
    ClaseCampeon = atributos
    if ClaseCampeon.lower() == "guerrero":
        vida = random.choice(vidaGuerrero)
        daño = random.choice(dañoGuerrero)
        escudo = random.choice(escudoGuerrero)
    elif ClaseCampeon.lower() == "mago":
        vida = random.choice(vidaMago)
        daño = random.choice(dañoMago)
        escudo = random.choice(escudoMago)
    elif ClaseCampeon.lower() == "guardian":
        vida = random.choice(vidaDefensa)
        daño = random.choice(dañoDefensa)
        escudo = random.choice(escudoDefensa)  

    return vida, daño, escudo

vida, daño, escudo = VidaDañoEscudo(ClaseCampeon1)

#Defino el Campeon 1
Nombre_Usuario1 = campeon(Nombre_Usuario1,Campeon1, ClaseCampeon1, vida, daño, escudo)

Nombre_Usuario1.caracteristicas()

print("""
      MUY BIEN CAMPEON Numero 1 LISTO \n 
      AHORA INGRESAREMOS AL RETADOR \n """)

Nombre_Usuario2 = input("Bienvenido Retador a la lucha de campeones, ahora ingrese el nombre del dueño del Campeon : \n")
Campeon2 = input("Perfecto, es hora de ingresar el nombre de su formidable Campeon : \n")

ClaseCampeon2 = Clase_Campeon()

print("""
      
      """)

vida, daño, escudo = VidaDañoEscudo(ClaseCampeon2)

Nombre_Usuario2 = campeon(Nombre_Usuario2, Campeon2, ClaseCampeon2, vida, daño, escudo)
Nombre_Usuario2.caracteristicas()


Campeones = [Nombre_Usuario1, Nombre_Usuario2]

print("\n Veamos quien sera el primero en atacar .....\n")

primerAtaque = random.choice(Campeones) 
print(f"El primero en atacar es {primerAtaque.nombreUsuario}\n")

# Realizo la primera ronda

if primerAtaque == Nombre_Usuario1:
    Atacar(Nombre_Usuario1, Nombre_Usuario2)
    segundoAtaque = Nombre_Usuario2   
    print(f"\n Y ahora es turno de {segundoAtaque.nombreUsuario} veamos como responde ")
    Atacar(Nombre_Usuario2, Nombre_Usuario1)
    
elif primerAtaque == Nombre_Usuario2:
    Atacar(Nombre_Usuario2, Nombre_Usuario1)
    segundoAtaque = Nombre_Usuario1
    print(f"\n Y ahora es turno de {segundoAtaque.nombreUsuario} veamos como responde ")
    Atacar(Nombre_Usuario2,Nombre_Usuario1)


# Actualizacion personajes

print(f"\n Veamos como quedaron nuestros campeones para el siguiente combate : \n")

print(f"\n Empecemos por el atacante numero 1 {primerAtaque.nombreUsuario} \n")
Nombre_Usuario1.actualizacion()

print(f"Continuemos con el atacante numero 2 {segundoAtaque.nombreUsuario} \n ")

Nombre_Usuario2.actualizacion()