import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'/Users/filippo/get_mcf_data/4FGL_J2202.7+4216_weekly_9_11_2023.csv',sep=',')
#print(df.columns)
#print(df.head())


ax =df['Julian Date']
ey=df['Photon Flux Error(photons cm-2 s-1)']
ay =df['Photon Flux [0.1-100 GeV](photons cm-2 s-1)']
ay_ln=np.log(ay)



#plot continuo
#plt.plot(ax,ay,color='darkblue')

#plot con asterisco
#plt.plot(ax, ay, '*', color='darkblue')

#plt.xlabel('Julian Time')
#plt.ylabel('Photon Flux')
flusso_fotoni=plt.errorbar(ax, ay_ln, yerr=ey, fmt='o' )
plt.savefig('/Users/filippo/get_mcf_data/flussofotoni_logaritmico.png')

plt.show()
