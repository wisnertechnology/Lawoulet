#coding:utf-8
import pickle
import random
import sys
import os

                        #  PATI 1
# create a sign in  class for user
class itilizate:
    #sa se konstrikte klas itilizate nou an
    def __init__(self, epsedo, sko):
        #self.epsedo = input(antre yon epsedo)
        self.epsedo = epsedo
        self.total_sko = sko
        
  
########################################################


#declare some variable
user_chance = 5
sko = 0
total_sko = 0
sko_pa_pati = 0
random_value = 2
#tes
sko_baz = 0
#tes
belJwe02 = 0
kontinye_ou_non = True
  
###################################################################################################################### 

                                #PATI 2
                                
#anregistrer objea nan yon fichye pickle
def anrejistre_obje(jwe, non_fichyea):
    with open(non_fichyea,"wb") as fichye1:
        pickle.dump(jwe, fichye1)

# chaje oubyen fe yon kopi objea nan fichye pickle laaa
def kopi_objet(non_fichyea):
    with open(non_fichyea, "rb") as fichye1:
        objet_kopye = pickle.load(fichye1)
        return objet_kopye
        
        
        
        
# fonksyon pou kreye obje oubyen enstans klass laaa epi anrejistrel nan fichye Pickle laaa
def kreye_ak_anrejistre_obje(non_fichyea):
        #tes
    global sko
    #global jwe
    epsedo = input("\n\n\n\n\nantre yon epsedo :      ")
    #teste si vale itlizatea rantre pa gen espas ak ekri an miniskil paske sinon lap bay problem
    while True:
        if ' ' in epsedo and not epsedo.islower():
            print("atansyon epsedoa dwe ekri an miniskil e pa dwe gen espas ladann")
            epsedo = input("\n\nantre yon epsedo :      ")    
    
        elif not epsedo.islower():
            print("atansyon epsedoa dwe ekri an miniskil")
            epsedo = input("\n\nantre yon epsedo :      ")
            
        elif ' ' in epsedo:
            print("epsedo ou rantrea pa dwe gen espas ladann\n")
            epsedo = input("\n\nantre yon epsedo :      ")

        else: 
            break
    jwe = itilizate(epsedo, sko)
    
                                
                                
    anrejistre_obje(jwe, "les_utilisateurs.txt") 
    return jwe

#kounyea annou kreye ak anrejistre obje nou an
#kreye_ak_anrejistre_obje("les_utilisateurs.txt") 



# kounyea annou itilize fonnksyon nou an pou nou kapab fe kopi obje nou an nan fichye pickle
objet_kopye = kopi_objet("les_utilisateurs.txt")


#objet_kopye.epsedo = "gachelyn"
#print(objet_kopye.epsedo)







#sa se fonksyon tretman an
def fonksyon_tret():
    global user_chance
    global total_sko
    global sko_pa_pati
    global sko
    print("Ou gen {} chans".format(user_chance))
    while user_chance >= 0:


        #sa se vale machin nan
        random_value = random.randint(1,50)
        #print("the random value is {}".format(random_value))

        user_value = input("---------------------- antre yon vale -----------------\n")
        user_value = int(user_value)
        if 1<= user_value <= 50:
            #la mwen caster vale itilizatea sot rantre a an antye poum kapab fe konparezon
            



            if user_value != random_value:
                if user_value > random_value:
                    print("vale ou rantrea trop\n")
                    print("nonb ki te kachea se te {}\n\n".format(random_value))
                    #we decrement the user_chance variable
                    user_chance -= 1
                else:
                    print("vale ou rantrea tropiti\n")
                    print("nonb ki te kachea se te {}\n\n".format(random_value))
                    #we decrement the user_chance variable
                    user_chance -= 1
                    
            elif user_value == random_value and user_chance == 1:
                print("Bravo :) , ou jwenn vre valea")
                sko_pa_pati = 1 * 30
                total_sko = total_sko + sko_pa_pati
                print("Ou fe {}pwen nan pati saaa\n\n".format(sko_pa_pati))                    
                    
            elif user_value == random_value and user_chance > 0:
                print("Bravo :) , ou jwenn vre valea")
                sko_pa_pati = (user_chance - 1) * 30
                total_sko = total_sko + sko_pa_pati
                print("Ou fe {}pwen nan pati saaa\n\n".format(sko_pa_pati))

            else:
                print("Bravo :) , ou jwenn vre valea")
                sko_pa_pati = 1 * 30
                total_sko = total_sko + sko_pa_pati
                print("Ou fe {}pwen nan pati saaa\n\n".format(sko_pa_pati))
                
                # Show to the user his chance number
            print("Ou ret {}chans".format(user_chance))
            
                #afekte yon nouvo sko pou itilizate kap jwea    
                
            
        else:
            print("vale ou rantrea pa nan enteval vale jwet laaa\n")
            print("Ou toujou gen {} chans".format(user_chance))
        
    
    
    if user_chance == 0:
        print("ou fin itilize tout chans ou yo, mesi paske ou te chwazi jwe ak nou!!!!!!")
                         
                
    #tes       
    print("TOTAL PWEN ou se : {} ".format(total_sko)) 
    #return total_sko
    
    
    
    
    
    
    
    
   
      #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#   
    
    
    
                                        #PATI 3
                                        
#meni principal
def meni_pwogram():
    print("\n\n\n\t\t\t\t ************** WELCOME TO THE PYTHON PROGRAM ***************\n\n\n")
    
    print(" A: Si ou ta renmen kreye yon itilizate pou jwe peze 1\n")
    print(" B: Si ou ta renmen kontinye jwe avek yon itilizate ou t genyn deja sousistem nan peze 2\n")
    #print(" C: Si ou vle kontinye peze 'y' oubyen 'Y'\n")
    #print(" D: Si ou vle kanpe jwet laaa peze 'k' oubyen 'K'\n")
    print(" C: Si ou vle kontinye peze nenpot chif \n")
    print(" D: Si ou vle kanpe jwet laaa peze 'k' oubyen 'K'\n")


def sou_meni():
    print("\n\n\n\t\t\t\t\t C: Si ou vle kontinye peze nenpot chif \n")
    print("\n\n\n\t\t\t\t\t D: Si ou vle kanpe jwet laaa peze 'k' oubyen 'K'\n")







#fonksyon pou opsyon
def chwazi_opsyon():
    global total_sko
    global objet_kopye
    global belJwe02
    global user_chance
    chwa = True
    
    while chwa:
        meni_pwogram()
        opsyon = input("\n\nfe chwa youn nan opsyon yo svp ::::::   ")
        #opsyon_2 = str(opsyon)
        #opsyon = int(opsyon)
        
        if opsyon == '1':
            global user_chance
            total_sko = 0
            user_chance = 5
            belJwe02 = kreye_ak_anrejistre_obje("les_utilisateurs.txt")
                
            fonksyon_tret()
            objet_kopye.total_sko = total_sko
            objet_kopye.epsedo = belJwe02.epsedo
            anrejistre_obje(objet_kopye, "les_utilisateurs.txt")
            objet_kopye = kopi_objet("les_utilisateurs.txt")
            print(objet_kopye.total_sko)
            #tes
            print(objet_kopye.epsedo)
            os.system('cls' if os.name == 'nt' else 'clear')
            #continue
        elif opsyon == '2':
             
            verifikasyon_epsedo = input("\n\nantre epsedo itilizate ou gen dejaaa!!!\n\n")

            if objet_kopye.epsedo == verifikasyon_epsedo:
                anrejistre_obje(objet_kopye, "les_utilisateurs.txt")
                objet_kopye = kopi_objet("les_utilisateurs.txt")
                print(objet_kopye.total_sko)
                total_sko = objet_kopye.total_sko
                print("\n\n\n\t\t\t\t\tNOU KONTAN PASKE OU TOUNEN NAN JWET LAAA ANKO SOU NON ITILIZATE OU TE GENYEN AN")
                print("\t\t\t\t\t denye_sko oua sete : {}".format(objet_kopye.total_sko) )
                user_chance = 5
                total_sko = 0
                fonksyon_tret()
                #print(total_sko) 
                ###########################
                #fonksyon_tret()
                #objet_kopye.total_sko = total_sko
                anrejistre_obje(objet_kopye, "les_utilisateurs.txt")
                objet_kopye = kopi_objet("les_utilisateurs.txt")
                #print("Sko total ou kounyea se {}".format(objet_kopye.total_sko))
                    
                objet_kopye.total_sko += total_sko
                anrejistre_obje(objet_kopye, "les_utilisateurs.txt")
                objet_kopye = kopi_objet("les_utilisateurs.txt")
                print("Sko total ou kounyea se {}".format(objet_kopye.total_sko))
                os.system('cls' if os.name == 'nt' else 'clear')
        
                    
            else:
                print("epsedo saa pa nan baz done nou, rantre yon bon epsedo silvouple")
                os.system('cls' if os.name == 'nt' else 'clear')
                
                #opsyon = input("\n\nfe chwa youn nan opsyon yo svp ::::::   ")
                #opsyon_2 = opsyon
                #continue
            #if opsyon.lower() =="y" or opsyon.upper() == "Y":
        #elif opsyon == "y" or opsyon == "Y":
            #print("mesi paske ou chwazi kontinye jwe ak nou")
            #continue
        elif opsyon =="k" or opsyon == "k":
                sys.exit()       
        else:
            print()
                
    
 #erde
#meni_pwogram()
#opsyon = input("\n\nKi opsyon ou chwazi  ::\t\t")
#opsyon = int(opsyon)

chwazi_opsyon()