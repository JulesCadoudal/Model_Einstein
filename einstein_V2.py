#######################################
#   Programme de Jules CADOUDAL       #
#   Simulation du model d'Einstein    #
#   03/02/2020                        #
#######################################

from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import random 
"""
(pour le model d'Enstein voir page wikipédia)
La simulation est faite en calculant pour chaque valeur de KbT/hw l'energie moyenne (de chaque particules) en utilisant la valeur de la fonction de partition d'un ressort (voir model d'Einstein)
On calcul la probabilité de chaques micro état (définie par le mode de l'atome) en utilisant l'energie moyenne (voir physique statistique approche micro canonique), on stocke ca dans une liste et on réitère 12 fois. 
On obtient alors une liste avec le pourcentage de chance de chaque niveau d'energie selon la température
Ensuite on se ballade dans un array 2D de 60 par 60 et à chaques indice on lance la sousfonction qui nous donne le niveau d'énergie de l'atome selon la température.
Cette sous fonction marche en allant chercher le pourcentage de chance de chaque niveau dans la liste. On teste du plus haut niveau d'énergie au plus bas (car la statistiqe est décroissant avec l'augmentation du niveau)
Pour animé la simulation on crée une image de l'array 2D et on la sauvegarde pour chaques valeurs de KbT/hw, ensuite on crée un gif avec les images
On stocke aussi les valeurs de chaques niveau d'énergie pour KbT/hw et on crée un diagramme à barre. 
"""
#Initialisation des divers constantes et listes
v=51
Matrice=np.empty((v,v))
constante=1
k=1.38*10**-23
constante=0.001  #la constante est KbT/hw
indice=0

# cette partie réitaire la simulation un certain nombre de fois (définie par range) en augmentant la valeur de la constante
for i in range(200):
    constante+=0.01
    indice+=1
    percent=[]
    Nbn=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    Nbnn=[]
    def partition(constante): #La fonction rend la valeur de la fonction de partition selon la valeur de constante
        return(1/(2*np.sinh(0.5*(1/constante))))
    for i in range(13):
        percent.append(((np.exp((-1/constante)*(0.5+i)))/(partition(constante))))  #ici on calcule la probabilité de chaque micro état selon la température et on stocke ca dans une liste
    def reset(percent): #Fonction qui teste TRUE selon une probabilité qui lui est communiqué 
        if random.uniform(0,1) <percent:
            return True
        else :
            return False

    def n(percent): #Fonction qui donne le niveau d'energie d'un atome en appelant la donction reset
        n=13
        for i in range(12,-1,-1):
            n-=1
            if percent[i]>=1:
                break
            if reset(percent[i])==True:
                break
        return(n)

    for j in range (v):  #on se balade dans l'array 2D et on donne un niveau d'énergie à chaques atomes, on stocke cette valeurs dans la liste Nbn 
        for i in range(v):
            N=n(percent)
            Matrice[j][i]=N
            Nbn[N]+=1
    for i in range(0,12):
        Nbnn.append(Nbn[i+1])

    plt.bar([1,2,3,4,5,6,7,8,9,10,11,12],Nbnn,color="red") #cette partie crée les diagramme barre pour chaques valeurs de la constante
    plt.title("KbT/hw = {0}".format(constante))
    plt.axis([1, 12, 1, 1000])
    plt.xlabel("Niveau d'énergie")
    plt.ylabel("Nombre d'atome au niveau d'energie")
    plt.savefig("{0}.png".format(indice))
    #plt.show()

    plt.figure(figsize=(10, 10))#cette partie crée l'image de la matrice d'atome 
    color_map = plt.imshow(Matrice,vmin=0, vmax=12,)
    color_map.set_cmap("OrRd")
    plt.title('kt/hw = {0}'.format(constante))
    plt.colorbar()
    plt.savefig("A{0}.png".format(indice))
    #plt.show() 

def cv(constante):#cette parti trace la variation de Cv selon KbT 
    return(((0.5/constante)**2)/((np.sinh(0.5/constante))**2))
def kt(constante):
    return(2*(np.tanh(0.5/constante))*constante)
const=np.linspace(0.001,3,1000)

#img = plt.imread("C:\\Users\\jcado\\Pictures\\Baow.png") cette partie avait pour but de mettre une image de mon chien en font 
#plt.imshow(img, extent=[0, 3, 0, 3])
plt.plot(const,cv(const), '--', linewidth=5, color='firebrick')
plt.title("Méthode d'Einstein")
plt.xlabel('kt/hw')
plt.ylabel('C/Nk')
plt.show()