## JUEGO - PELEA DE CAMPEONES - ##

# Librerias :
import random
import sys
import time

# Defino mis variables de Daño - Escudo - Vida segun la clase del guerrero:
dañoGuerrero = (80, 70, 60)
vidaGuerrero = (250, 220, 200)
escudoGuerrero = (150, 120, 100)

dañoMago = (60, 50, 40)
vidaMago = (350, 300, 250)
escudoMago = (100, 80, 50)

dañoDefensa = (40, 30, 20)
vidaDefensa = (500, 450, 400)
escudoDefensa = (200, 150, 100)

# Defino la clase Campeon:
class campeon:
    def __init__(self,nombreUsuario, nombreCampeon, clase, vida, daño, escudo):
        self.nombreUsuario = nombreUsuario
        self.nombreCampeon = nombreCampeon
        self.clase = clase
        self.vida = vida
        self.daño = daño
        self.escudo = escudo

        
    def caracteristicas(self): # presentacion
        print(f"- - - - - Bienvenido {self.nombreUsuario} a la Arena de combate - - - - -  \n")
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
        # Guerrero Atacar Escudo:
        if self.clase ==  "guerrero":
            if enemigo.clase == "mago":
                daño = self.daño * 0.75
                if daño > enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo
                    print(f"Excelente, tu daño de {daño} poder rompio con el escudo de tu rival apesar de que es un Mago, \n ahora esta vulnerable, acabalo ! \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    if enemigo.vida <= 0:
                        enemigo.vida = 0
                        print(f"--Golpe Final-- Tu daño de {daño} poder liquido la vida de tu rival... \n Campeon de Campeones!!! \n No temblaste a la hora de enfrentarte a un Mago, demostraste que un Guerrero es digno rival para enfrentar las artes oscuras \n ")
                        return enemigo.vida
                    if enemigo.vida > 0:
                        enemigo.escudo = 0
                        print(f"\n Tu ataque infigio daño directo sobre la vida de tu enemigo, su vida esta bajando! \n ahora su vida es de {enemigo.vida}\n")
                        return 
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Estas intentandolo contra un Mago vas bien ... \n Con tu ataque de {daño} de poder no rompiste su escudo lo dañaste, \n ahora su escudo esta debilitado y bajo a {enemigo.escudo}\n")
                    return enemigo.escudo
                
                if enemigo.escudo == daño:
                    enemigo.escudo = 0
                    print(f"Ese ataque de {daño} termino rompiendo todo su escudo \n no fue lo suficiente para dañar su vida, pero no te desesperes que con unos ataques mas bastara para acabarlo")
                    return enemigo.escudo
                
                    
            if enemigo.clase == "guardian":
                daño = self.daño * 1.25
                if daño > enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo
                    print(f"Oh !! Este ataque de {daño} de daño rompio escudo del Guardian apesar de su resistencia, aprovecha tu velocidad y liquidalo ! \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    if enemigo.vida <= 0:
                        enemigo.vida = 0
                        print(f"--Golpe Final-- Tu daño de {daño} poder liquido la vida de tu rival... \n Campeon de Campeones!!! \n Ahora los Campeones Guardianes pensaran 2 veces si atreverse a enfrentar a un Campeon Guerrero, ni su gran escudo puede protegerlo contra tu poder \n  ")
                        return enemigo.vida
                    if enemigo.vida > 0: 
                        enemigo.escudo = 0
                        print(f"Veo que este ataque lastimo al Guardian, esa herida le esta costando valor a su vida que ahora es de {enemigo.vida}\n")
                        return 
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Muy dificil penetrar el escudo de un Guardian, y menos con {daño} de daño, verdad? \n Aunque no rompiste su escudo lo dañaste, su escudo bajo a {enemigo.escudo}\n")
                    return enemigo.escudo
                
                if enemigo.escudo == daño:
                    enemigo.escudo = 0
                    print(f" Adios a tu escudo Guardian, no resistio mas y con un ataque de {daño} de daño \n Pero no te apresures, aunque no tenga escudo la vida de un Guardian es alta")
                    return enemigo.escudo
            
            if enemigo.clase == "guerrero":
                daño = self.daño * 1
                if daño > enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo
                    print(f"{daño} de poder necesitaste para romperle el escudo a otro Guerrero \n Ahora esta indefenso, demuestrale quien es el mejor Guerrero \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    if enemigo.vida <= 0:
                        enemigo.vida = 0
                        print(f"--Golpe Final-- Tu ataque no solo termino con su escudo sino tambien con su vida... \n Campeon de Campeones!!! \n Demostraste quien es el Guerrero que manda en tu clase \n ")
                        return enemigo.vida
                    if enemigo.vida > 0:
                        enemigo.escudo = 0
                        print(f"\n Tu ataque no solo rompio su escudo, infigio daño directo sobre su vida \n Ahora su vida es de {enemigo.vida}\n")
                        return 
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Es duro enfrentarte uno de tu misma clase, no? \n Con tu ataque de {daño} de poder no rompiste su escudo pero lo dañaste \n ahora su escudo esta debilitado y es de {enemigo.escudo}\n")
                    return enemigo.escudo
                
                if enemigo.escudo == daño:
                    enemigo.escudo = 0
                    print(f"Con ese ataque de {daño} destruiste su escudo \n No fue suficiente para dañarle la vida, pero si para ponerlo contra las cuerdas \n")
                    return enemigo.escudo
        #Mago Atacar Escudo:    
        if self.clase == "mago": 
            if enemigo.clase == "guerrero":
                daño = self.daño * 1.25
                if daño > enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo
                    print(f"Este Guerrero no debio meterse con un mago, tu poderoso ataque de {daño} de daño rompio su escudo, ahora sentira el miedo de un ser oscuro \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    if enemigo.vida <= 0:
                        enemigo.vida = 0
                        print(f"--Hechizo Liquidador-- Tu Magia de {daño} de poder acabo con su vida... \n Campeon de Campeones!!! \n Pobre Guerrero al creer que podia contra un Mago, ahora los otros Guerreros sabran porque deben temer a la Magia Oscura \n ")
                        return enemigo.vida
                    
                    if enemigo.vida > 0:
                        enemigo.escudo = 0
                        print(f"Tu ataque no solo atraveso su escudo sino que infligio daño a su vida, ahora su vida es de {enemigo.vida}\n")
                        return
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Apesar de tu ventaja de Mago no rompiste el escudo de este Guerrero con {daño} de daño, \n De todas formas lo dañaste y quedo en {enemigo.escudo}\n")
                    return enemigo.escudo
                
                if enemigo.escudo == daño:
                    enemigo.escudo = 0
                    print(f"Esta magia de {daño} de poder alcanzo para destruir su escudo \n No dañaste su vida pero sabe que tampoco podra resistir muchos ataques mas \n ")
                    return enemigo.escudo
                    
            if enemigo.clase == "guardian":
                daño = self.daño * 0.75
                if daño > enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo
                    print(f"Decian que un mago no podia hacerle frente a un Guardian? \n Mira con ese ataque de {daño} poder como lo dejaste sin escudo por completo \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    enemigo.escudo = 0
                    if enemigo.vida <= 0:
                        enemigo.vida = 0
                        print(f"--Hechizo Liquidador-- Tu Magia de {daño} de poder acabo con su vida\n Campeon de Campeones!!! \n Pensaron que un enorme Guardian derrotaria facilmente a un Mago? Nunca subestimes la inteligencia de un Mago y su Magia Oscura \n")
                        return enemigo.vida
                    
                    if enemigo.vida > 0:
                        
                        print(f"Ademas tu ataque lastimo a este Guardian, la magia resto su vida que ahora es de {enemigo.vida}\n")
                        return 
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Te lo dije, un Mago debe esforzarse mas si quiere romper el gran escudo de un Guardian\n No alcanza con un ataque de {daño} poder \n Igual lo dañaste, ahora su escudo bajo a {enemigo.escudo}\n")
                    return enemigo.escudo
                
                if enemigo.escudo == daño:
                    enemigo.escudo = 0
                    print(f"Quebraste ese inmenso escudo con {daño} de daño  Aun asi no pudiste rozar tu vida \n Sigue atacando estas mas cerca de su muerte\n")
                    return enemigo.escudo
                
            if enemigo.clase == "mago":
                daño = self.daño * 1
                if daño > enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo
                    print(f"{daño} de Magia fueron necesarios para romper su escudo \n esta lucha de Magos se vuelve mas interesante ahora que no tiene un escudo para protegerse \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    if enemigo.vida <= 0:
                        enemigo.vida = 0
                        print(f"--Hechizo Liquidador-- No solo rompiste su escudo tambien su vida... \n Campeon de Campeones!!! \n Entre Magos ahora se conoce quien manda \n ")
                        return enemigo.vida
                    if enemigo.vida > 0:
                        enemigo.escudo = 0
                        print(f"\n Tu magia no solo termino con su escudo, tambien dañaste su vida \n Que ahora quedo en {enemigo.vida}\n")
                        return 
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Enfrentar a otro Mago hace las cosas dificiles \n Con tu magia de {daño} de poder no terminaste con su escudo pero si lo rajaste \n ahora quedo debilitado y es de {enemigo.escudo}\n")
                    return enemigo.escudo
                
                if enemigo.escudo == daño:
                    enemigo.escudo = 0
                    print(f"Ese ataque magico de {daño} destruyo su escudo \n No fue tan eficaz para dañarle la vida, aunque ahora quedo desprotegido \n")
                    return enemigo.escudo
                
                    
        #Guardian Atacar Escudo:
        if self.clase == "guardian":
            if enemigo.clase == "guerrero":
                daño = self.daño * 0.75
                if daño > enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo                    
                    print(f"Y decian que los Guardianes no tenian poder \n Pero con {daño} de daño quebraste en mil pedazos su escudo, \n  Ahora ve por su vida \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    if enemigo.vida <= 0:
                        enemigo.vida = 0
                        print(f"--Escudo Supremo-- A pesar de tu daño de {daño} de poder lograste acabar con su vida... \n Campeon de Campeones!!! \n Resististe esos golpes como un digno Campeon, sin importar la ventaja del daño de un Guerrero, ahora deberan demostrar respeto ante un Guardian   \n ")
                        return enemigo.vida
                    
                    if enemigo.vida > 0:
                        enemigo.escudo = 0
                        print(f"Aunque no solo dañaste su escudo, hiciste daño directo sobre su vida que ahora es de {enemigo.vida}\n")
                        return 
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Debes esforzarte mas si quieres matar a un Guerrero, \nSu vida sera baja pero tu daño {daño} de poder es mas bajo \n Aun asi dañaste su escudo y ahora su proteccion es de {enemigo.escudo}\n")
                    return enemigo.escudo
                
                if enemigo.escudo == daño:
                    enemigo.escudo = 0
                    print(f"Lograste romper el escudo de ese Guerrero con {daño} de daño \n No pudiste dañar su vida, pero sabes que los Guerreros no tienen mucha vida...")
                    return enemigo.escudo
                    
            if enemigo.clase == "mago":
                daño = self.daño * 1.25
                if daño > enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo 
                    print(f"Puedo ver la cara de preocupacion de ese Mago,\n tu daño de {daño} lo dejo sin escudo, esta indefenso, su oscuridad pronto vera la luz ! \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo 
                    enemigo.escudo = 0
                    
                    if enemigo.vida <= 0:
                    
                        print(f"--Escudo Supremo-- A pesar de tu daño de {daño} de poder lograste acabar con su vida\n Campeon de Campeones!!! \n Este Mago penso que podia escurrirse de tus ataques por su tamaño? Se equivoco, lo aplastaste como una cucaracha, van a pensarlo 2 veces antes de enfrentar un Guardian  \n")
                        return enemigo.vida
                    
                    if enemigo.vida > 0:
                        print(f"No solo esta preocupado, tiembla, esta asustado, dañaste su vida y ahora esta bajando!! \n Ahora su vida es de {enemigo.vida}\n")
                        return 
                
                if enemigo.escudo == daño:
                    enemigo.escudo = 0
                    print(f"Rompiste su escudo con {daño} de daño!! \n  De igual manera no fue suficiente para tambien lastimar su vida\n ")
                    return enemigo.escudo
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Ese Mago es muy escurridizo, \n Con {daño} de poder todavia no rompiste su escudo lo dañaste, ahora esta debilitado y bajo a {enemigo.escudo}\n")
                    return enemigo.escudo 
                
            if enemigo.clase == "guardian":
                daño = self.daño * 1
                if daño > enemigo.escudo:
                    enemigo.escudo = daño - enemigo.escudo
                    print(f"Magnifico ataque de {daño}, rompiste el escudo de otro Guardian \n Ahora esta mas desprotegido es tu momento de demostrar que Guardian es mas poderoso \n")
                    enemigo.vida = enemigo.vida - enemigo.escudo
                    if enemigo.vida <= 0:
                        enemigo.vida = 0
                        print(f"--Escudo Supremo-- Tu ataque no solo arruino su escudo sino tambien su vida... \n Campeon de Campeones!!! \n Ahora todos los Guardianes se arrodillaran ante ti \n ")
                        return enemigo.vida
                    if enemigo.vida > 0:
                        enemigo.escudo = 0
                        print(f"\n No solo rompiste su escudo, tambien dañaste su vida \n Ahora su vida es de {enemigo.vida}\n")
                        return 
                
                if enemigo.escudo > daño:
                    enemigo.escudo = enemigo.escudo - daño
                    print(f"Es duro enfrentarte uno de tu misma clase, no? \n Con tu ataque de {daño} de poder no rompiste su escudo pero lo dañaste \n ahora su escudo esta debilitado y es de {enemigo.escudo}\n")
                    return enemigo.escudo
                
                if enemigo.escudo == daño:
                    enemigo.escudo = 0
                    print(f"Con ese ataque de {daño} destruiste su escudo \n No fue suficiente para dañarle la vida, pero si para ponerlo contra las cuerdas \n")
                    return enemigo.escudo       
    
    def atacarVida(self,enemigo):
        #Guerrero Atacar Vida:
        if self.clase ==  "guerrero":
            #contra mago:
            if enemigo.clase == "mago":
                daño = self.daño * 0.75
                if daño >= enemigo.vida:
                    enemigo.vida = 0
                    print(f"--Golpe Final-- Tu daño de {daño} poder liquido la vida de tu rival... \n Campeon de Campeones!!! \n No temblaste a la hora de enfrentarte a un Mago, demostraste que un Guerrero es digno rival para enfrentar las artes oscuras \n ")
                    Ganador = self.nombreCampeon
                    return 
                
                if enemigo.vida > daño:
                    enemigo.vida = enemigo.vida - daño
                    print(f"Ese Mago esta asustado, sabe que esta mas cerca de su muerte ... \n Tu ataque de {daño} de poder lo deja en las cuerdas flojas... \n su vida bajo considerablemente, ahora es de {enemigo.vida}\n")
                    return enemigo.vida
            #contra guardian:        
            if enemigo.clase == "guardian":
                daño = self.daño * 1.25
                if daño >= enemigo.vida:
                    enemigo.vida = 0
                    print(f"--Golpe Final-- Tu daño de {daño} poder liquido la vida de tu rival... \n Campeon de Campeones!!! \n Ahora los Campeones Guardianes pensaran 2 veces si atreverse a enfrentar a un Campeon Guerrero, ni su gran escudo puede protegerlo contra tu poder \n  ")
                    Ganador = self.nombreCampeon
                    return
                
                if enemigo.vida > daño:
                    enemigo.vida = enemigo.vida - daño
                    print(f"El Campeon Guardian empieza a preocuparse, sabe que su nivel de vida es grande pero ve como va bajando... \n Tu ataque de {daño} de poder lo debilito... \n Ahora su vida es de {enemigo.vida}\n")
                    return enemigo.vida
                
            #contra guerrero:        
            if enemigo.clase == "guerrero":
                daño = self.daño * 1
                if daño >= enemigo.vida:
                    enemigo.vida = 0
                    print(f"--Golpe Final-- Tu ataque de {daño} poder finalizo con la vida de tu rival... \n Campeon de Campeones!!! \n Los Guerreros ahora saben quien es el mas fuerte entre ellos \n  ")
                    Ganador = self.nombreCampeon
                    return
                
                if enemigo.vida > daño:
                    enemigo.vida = enemigo.vida - daño
                    print(f"Ese Guerrero teme por su vida, sabes que esta bajando considerablemente \n Tu ataque de {daño} de daño lo arrima mas a su muerte \n Ahora su vida es de {enemigo.vida}\n")
                    return enemigo.vida
                
        #Mago Atacar vida:                    
        if self.clase == "mago": 
            
            ##Contra Guerrero:
            if enemigo.clase == "guerrero":
                daño = self.daño * 1.25
                if daño >= enemigo.vida:
                    enemigo.vida = 0
                    print(f"--Hechizo Liquidador-- Tu Magia de {daño} de poder acabo con su vida... \n Campeon de Campeones!!! \n Pobre Guerrero al creer que podia contra un Mago, ahora los otros Guerreros sabran porque deben temer a la Magia Oscura \n ")
                    Ganador = self.nombreCampeon
                    return 
                
                if enemigo.vida > daño:
                    enemigo.vida = enemigo.vida - daño
                    print(f"Tic Tac - Tic Tac ... Solo es cuestion de tiempo \n Tu Hechizo hizo {daño} de daño lo debjo viendo las estrellas... \n su vida agoniza, y ahora es de {enemigo.vida}\n")
                    return enemigo.vida
                
            ##Contra Guardian:        
            if enemigo.clase == "guardian":
                daño = self.daño * 0.75
                if daño >= enemigo.vida:
                    enemigo.vida = 0
                    print(f"--Hechizo Liquidador-- Tu Magia de {daño} de poder acabo con su vida\n Campeon de Campeones!!! \n Pensaron que un enorme Guardian derrotaria facilmente a un Mago? Nunca subestimes la inteligencia de un Mago y su Magia Oscura \n")
                    Ganador = self.nombreCampeon
                    return 
                
                if enemigo.vida > daño:
                    enemigo.vida = enemigo.vida - daño
                    print(f"Estas dandolo todo de ti, enfrentarse a un Guardian no es nada facil \n No te preocupes que tu ataque de {daño} de poder lastimo a ese grandote \n Mira bien, ahora su vida bajo a {enemigo.vida}\n")
                    return enemigo.vida
                
            ##Contra mago:   
            if enemigo.clase == "Mago":
                daño = self.daño * 1
                if daño >= enemigo.vida:
                    enemigo.vida = 0
                    print(f"--Hechizo Liquidador-- Tu Magia de {daño} de poder liquido con la vida de este Mago... \n Campeon de Campeones!!! \n Demostraste quien es el Rey de las artes oscuras, ningun Mago volver a enfrentarte \n ")
                    Ganador = self.nombreCampeon
                    return 
                
                if enemigo.vida > daño:
                    enemigo.vida = enemigo.vida - daño
                    print(f"Ese Mago esta asustado, sabe que esta mas cerca de su muerte ... \n Tu ataque de {daño} de poder lo deja en las cuerdas flojas... \n su vida bajo considerablemente, ahora es de {enemigo.vida}\n")
                    return enemigo.vida
        
        #Guardian Ataca vida:
        if self.clase == "guardian": 
            
            ##Contra Guerrero:
            if enemigo.clase == "guerrero":
                daño = self.daño * 0.75
                if daño >= enemigo.vida:
                    enemigo.vida = 0
                    print(f"--Escudo Supremo-- A pesar de tu daño de {daño} de poder lograste acabar con su vida... \n Campeon de Campeones!!! \n Resististe esos golpes como un digno Campeon, sin importar la ventaja del daño de un Guerrero, ahora deberan demostrar respeto ante un Guardian   \n ")
                    Ganador = self.nombreCampeon
                    return 
                
                if enemigo.vida > daño:
                    enemigo.vida = enemigo.vida - daño
                    print(f"Si bien tu daño es bajo, su vida tambien lo es \n Tu ataque hizo {daño} de daño ... \n pero tranquilo su vida va disminuyendo, ahora es de {enemigo.vida}\n")
                    return enemigo.vida
            
            ## Contra mago:        
            if enemigo.clase == "mago":
                daño = self.daño * 1.75
                if daño >= enemigo.vida:
                    enemigo.vida = 0
                    print(f"--Escudo Supremo-- A pesar de tu daño de {daño} de poder lograste acabar con su vida\n Campeon de Campeones!!! \n Este Mago penso que podia escurrirse de tus ataques por su tamaño? Se equivoco, lo aplastaste como una cucaracha, van a pensarlo 2 veces antes de enfrentar un Guardian  \n")
                    Ganador = self.nombreCampeon
                    return 
                
                if enemigo.vida > daño:
                    enemigo.vida = enemigo.vida - daño
                    print(f"Cuesta con este daño, pero resiste con tu enorme vida \n Tomalo con calma, que tus {daño} de daño lastiman su vida \n Solo ve su vida que ahora es de {enemigo.escudo}\n")
                    return enemigo.vida
                
            ##Contra Guardian:
            if enemigo.clase == "guardian":
                daño = self.daño * 1
                if daño >= enemigo.vida:
                    enemigo.vida = 0
                    print(f"--Escudo Supremo-- Subestimaron tu daño de {daño} de fuerza y asi lograste acabar con su vida... \n Campeon de Campeones!!! \n Eres el Guardian mas fuerte de los de tu clase   \n ")
                    Ganador = self.nombreCampeon
                    return 
                
                if enemigo.vida > daño:
                    enemigo.vida = enemigo.vida - daño
                    print(f"Si bien tu daño es bajo, su vida tambien lo es \n Tu ataque hizo {daño} de daño ... \n pero tranquilo su vida va disminuyendo, ahora es de {enemigo.vida}\n")
                    return enemigo.vida
    
    
    
    def matar(self,enemigo):
        pass   
               

## Defino si el ataque mata al enemigo, baja el escudo o ataca sobre la vida

def Atacar(Campeon,Enemigo):
    
    if Enemigo.escudo > 0:
        return Campeon.atacarEscudo(Enemigo)
        
        
    if Enemigo.escudo == 0:
        return Campeon.atacarVida(Enemigo)
        
    # if Enemigo.vida < Campeon.daño:
    #     return Campeon.matar(Enemigo)

        
# Pido ingresar los datos del campeon 1
Nombre_Usuario1 = input("Bienvenido a la lucha de campeones, ahora ingrese el nombre del dueño del Campeon : \n")
Campeon1 = input("Ahora ingrese el nombre de su valiente Campeon : \n")



clases = ["guerrero","mago","chiken", "guardian"]

 # Separacion.
print(""" 
      
      
      """)


# Defino la clase del campeon:
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
      - - - - - AHORA INGRESAREMOS AL RETADOR - - - - - - \n """)

#Separacion
print("""
      
      """)

Nombre_Usuario2 = input("Bienvenido Retador a la lucha de campeones, ahora ingrese el nombre del dueño del Campeon : \n")
Campeon2 = input("Perfecto, es hora de ingresar el nombre de su formidable Campeon : \n")

ClaseCampeon2 = Clase_Campeon()

print("""
      
      """)

vida, daño, escudo = VidaDañoEscudo(ClaseCampeon2)

Nombre_Usuario2 = campeon(Nombre_Usuario2, Campeon2, ClaseCampeon2, vida, daño, escudo)
Nombre_Usuario2.caracteristicas()


Campeones = [Nombre_Usuario1, Nombre_Usuario2]

time.sleep(10)

print("\n ####################################################### \n")
print("\n ---- De manera aleatoria veamos quien sera el primero en atacar----\n")
time.sleep(5)
primerAtaque = random.choice(Campeones) 
print(f"El primero en atacar sera {primerAtaque.nombreUsuario}\n")
time.sleep(5)
print("\n ####################################################### \n")

# Realizo la primera ronda
print("\n ------------------    EMPIEZA LA PRIMER RONDA ----------------------\n")

time.sleep(5)

# Identifico quien es el primero en atacar. 
if primerAtaque == Nombre_Usuario1:
    print(f"\n{Nombre_Usuario1.nombreCampeon} : \n")
    Atacar(Nombre_Usuario1, Nombre_Usuario2)
    segundoAtaque = Nombre_Usuario2  
    time.sleep(5) 
    print(" - - - - - - -")
    print(f"\n Y ahora es turno de {segundoAtaque.nombreUsuario} veamos como responde : \n ")
    time.sleep(5)
    Atacar(Nombre_Usuario2, Nombre_Usuario1)
    
elif primerAtaque == Nombre_Usuario2:
    print(f"{Nombre_Usuario2.nombreCampeon} : ")
    Atacar(Nombre_Usuario2, Nombre_Usuario1)
    segundoAtaque = Nombre_Usuario1
    time.sleep(5)
    print(" - - - - - - - -")
    print(f"\n Y ahora es turno de {segundoAtaque.nombreUsuario} veamos como responde : \n")
    time.sleep(5)
    Atacar(Nombre_Usuario1,Nombre_Usuario2)


# Actualizacion de personajes primera ronda
time.sleep(10)
print(f"\n  - - - - - - Veamos como quedaron nuestros campeones despues del primer combate : - - - - - -\n")
time.sleep(5)
print(f"\n Empecemos por el atacante numero 1 {primerAtaque.nombreUsuario} \n")
time.sleep(3)
Nombre_Usuario1.actualizacion()
time.sleep(10)
print(f"Continuemos con el atacante numero 2 {segundoAtaque.nombreUsuario} \n ")
time.sleep(3)
Nombre_Usuario2.actualizacion()
time.sleep(10)

print("\n              Continuemos con esta batalla\n")
time.sleep(5)


## Prueba lucha
Rondas = 1
while primerAtaque.vida > 0 and segundoAtaque.vida > 0:
    Rondas += 1
    print(f"\n################ Ronda {Rondas} ########################\n")
    time.sleep(3)
    print(f"\n -----Ataca {primerAtaque.nombreUsuario} ------\n")
    time.sleep(3)
    Atacar(primerAtaque, segundoAtaque)
    time.sleep(10)
    if segundoAtaque.vida == 0:
        winer = primerAtaque
        break
    
    print(f"\n -----Ataca {segundoAtaque.nombreUsuario} ------\n")
    time.sleep(3)
    Atacar(segundoAtaque, primerAtaque)
    time.sleep(10)
    if primerAtaque.vida == 0:
        winer = segundoAtaque
        break
    
time.sleep(5)    
print(f"\n¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ EL GANADOR ES {winer.nombreUsuario} !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
time.sleep(3)
print(f"Felicitaciones, tu Campeon {winer.nombreCampeon} es el vencedor de este reto ")    