# Model_Einstein
Ce programme a été réalisé dans le cadre d'un cours sur la physique du solide. Dans l'optique d'approfondir ma compréhension de cette matière. 
J'ai été mis au défi par mon professeur. Le défi consistait à réaliser une simulation du modèle d'Einstein en utilisant Python. 
Plus précisément à simuler le comportement d'une matrice d'atome identique, ayant chacun 12 niveaux d'énergie possible. 
Le comportement des dits atomes est influencé par l'augmentation de la température. 

(pour le model d'Enstein voir page wikipédia)
La simulation est faite en calculant pour chaque valeur de KbT/hw l'energie moyenne (de chaque particules) en utilisant la valeur de la fonction de partition d'un ressort (voir model d'Einstein)
On calcul la probabilité de chaques micro état (définie par le mode de l'atome) en utilisant l'energie moyenne (voir physique statistique approche micro canonique), on stocke ca dans une liste et on réitère 12 fois. 
On obtient alors une liste avec le pourcentage de chance de chaque niveau d'energie selon la température
Ensuite on se ballade dans un array 2D de 60 par 60 et à chaques indice on lance la sousfonction qui nous donne le niveau d'énergie de l'atome selon la température.
Cette sous fonction marche en allant chercher le pourcentage de chance de chaque niveau dans la liste. On teste du plus haut niveau d'énergie au plus bas (car la statistiqe est décroissant avec l'augmentation du niveau)
Pour animé la simulation on crée une image de l'array 2D et on la sauvegarde pour chaques valeurs de KbT/hw, ensuite on crée un gif avec les images
On stocke aussi les valeurs de chaques niveau d'énergie pour KbT/hw et on crée un diagramme à barre.
