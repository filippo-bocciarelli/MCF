import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'/Users/filippo/get_mcf_data/4LAC_DR2_sel.csv',sep=',')
df_no0=df.loc[df['nu_syn']!=0]
x_log=np.log(df_no0['Flux1000'])
x_log10=np.log10(df_no0['Flux1000'])
x_nusyn=np.log10(df_no0['nu_syn'])
#print(x_nusyn)


x=df['Flux1000']
lunghezza=print(len(df_no0['CLASS']))
for i in range(0,lunghezza+1):
	if df_no0['CLASS'][i]=='bll':
		df_bl l+=df.loc[df_no0['CLASS']]

#df_fsrq= df.loc[(df_no0['CLASS']=='fsrq')]

#print(type(df_bll))

#print(df)
#print(df.columns)
#print(df['CLASS'].head())

#plt.title("Sorgenti astrofisiche")
#plt.xlabel('log10_flusso fotoni')
#plt.ylabel('PL_index')
#plt.scatter(x_nusyn,df_bll, color='darkblue', s=3, label='piccoli')
#plt.scatter(x_nusyn,df_fsrq, color='darkred', s=3, label='piccoli')


#plt.show()
