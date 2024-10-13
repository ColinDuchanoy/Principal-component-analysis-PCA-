# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 09:50:26 2022

@author: colin
"""

import ACP as acp
import numpy as np
import matplotlib.pyplot as plt

#%%Bases de donnée iris

Ebrut=np.genfromtxt("iris.csv" , dtype=str , delimiter=',') #données brutes
labelscolonne=Ebrut[ 0 , : -1]
labelsligne=Ebrut[1 : , -1]
E=Ebrut[1 : , : -1].astype('float')

plt.close('all') #permet de fermer toutes les fenêtres matplotlib ouvertes
acp.ACP(E, labelsligne, labelscolonne,k=2)
acp.ACP2D(E, labelsligne, labelscolonne)
acp.ACP3D(E, labelsligne, labelscolonne)

A=acp.Kmoy(E, k=3, epsilon=10**-1)
for i in range(3):
    acp.ACP2D(A[i], labelsligne, labelscolonne)


#%%Base de donnée Pizzamod

Ebrut=np.genfromtxt("Pizzamod.csv" , dtype=str , delimiter=',') #données brutes
labelscolonne=Ebrut[ 0 , 1: ]
labelsligne=Ebrut[1 : , 0]
E=Ebrut[1 : , 1: ].astype('float')

plt.close('all') #permet de fermer toutes les fenêtres matplotlib ouvertes
acp.ACP(E, labelsligne, labelscolonne,k=2)
acp.ACP2D(E, labelsligne, labelscolonne)
acp.ACP3D(E, labelsligne, labelscolonne)


#%%Bases de donnée Howellmod

Ebrut=np.genfromtxt("Howellmod.csv" , dtype=str , delimiter=',') #données brutes
labelscolonne=Ebrut[ 0 , 1: ]
labelsligne=Ebrut[1 : , 0]
E=Ebrut[1 : , 1: ].astype('float')

plt.close('all') #permet de fermer toutes les fenêtres matplotlib ouvertes
acp.ACP(E, labelsligne, labelscolonne,k=2)
acp.ACP2D(E, labelsligne, labelscolonne)
acp.ACP3D(E, labelsligne, labelscolonne)


#%%Bases de donnée winequality-red

Ebrut=np.genfromtxt("winequality-red.csv" , dtype=str , delimiter=',') #données brutes
labelscolonne=Ebrut[ 0 , : -1]
labelsligne=Ebrut[1 : , -1]
E=Ebrut[1 : , : -1].astype('float')

plt.close('all') #permet de fermer toutes les fenêtres matplotlib ouvertes
acp.ACP(E, labelsligne, labelscolonne,k=2,)
acp.ACP2D(E, labelsligne, labelscolonne)
acp.ACP3D(E, labelsligne, labelscolonne)


#%%Bases de donnée Breast_cancer_data
Ebrut=np.genfromtxt("Breast_cancer_data.csv" , dtype=str , delimiter=',') #données brutes
labelscolonne=Ebrut[ 0 , :-1 ]
labelsligne=Ebrut[1 : , -1 ]
E=Ebrut[1 : , :-1 ].astype('float')

plt.close('all') #permet de fermer toutes les fenêtres matplotlib ouvertes
acp.ACP(E, labelsligne, labelscolonne,k=2)
acp.ACP2D(E, labelsligne, labelscolonne)
acp.ACP3D(E, labelsligne, labelscolonne)