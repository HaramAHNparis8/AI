from random import randint
#etat initial: (1,1,1,1)
#état but :(2,2,2,2)

# contraintes: états interdits
# (1,2,2,1), (1,2,1,2), (1,2,2,2)
# (2,1,1,2), (2,1,2,1), (2,1,1,1)

# actions: passage d'un état à un autre
# (1,1,1,1) -> (2,2,1,1) : le fermier traverse avec la poule
# (2,2,1,1) -> (1,2,1,1) : le fermier revient tout seul

def verifie_interdit(tab): # vérifiez si le tableau est le cas intérdit
     
     etat_interdit = [[1,2,2,1],[1,2,1,2],[1,2,2,2],[2,2,1,1],[2,1,2,1],[2,1,1,1]]
     for i in range(len(etat_interdit)):
         
         if tab == etat_interdit[i]:
             
             return True

def exo1_random():
    etat_init = [1,1,1,1]
    etat_but = [2,2,2,2]


    while(1):
        pos = randint(0,3)
        if etat_init[0] == 1:

            print(etat_init)
            etat_init[pos] = 2

        elif etat_init[0] == 2:
             
             print(etat_init)
             etat_init[pos] = 1
        if verifie_interdit(etat_init) == True:
           continue

        if etat_init == etat_but:
            break
        
   
       

# print(verifie_interdit([2,1,1,1]))
exo1()


