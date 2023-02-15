import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
Debts = pd.read_csv("ids_last_5y.csv")

Debts = Debts[['Country Name','2018','2019','2020','2021','2022']]
print(Debts)
#renaming columns
Debts = Debts.rename(columns={'Country Name':'Country_Name','2018':'Debt_in_2018','2019':'Debt_in_2019','2020':'Debt_in_2020',\
                      '2021':'Debt_in_2021','2022':'Debt_in_2022'})
Debts = Debts.loc[~Debts['Debt_in_2018'].isna()]
Debts = Debts.loc[~Debts['Debt_in_2019'].isna()]
Debts = Debts.loc[~Debts['Debt_in_2020'].isna()]
Debts = Debts.loc[~Debts['Debt_in_2021'].isna()]
Debts = Debts.loc[~Debts['Debt_in_2022'].isna()]
print(Debts.dtypes)

Debts['Debt_in_2018'] = Debts['Debt_in_2018']/100000
Debts['Debt_in_2019'] = Debts['Debt_in_2019']/100000
Debts['Debt_in_2020'] = Debts['Debt_in_2020']/100000
Debts['Debt_in_2021'] = Debts['Debt_in_2021']/100000
Debts['Debt_in_2022'] = Debts['Debt_in_2022']/100000

Debts['Debt_in_2018'] = Debts['Debt_in_2018'].astype('int')
Debts['Debt_in_2019'] = Debts['Debt_in_2019'].astype('int')
Debts['Debt_in_2020'] = Debts['Debt_in_2020'].astype('int')
Debts['Debt_in_2021'] = Debts['Debt_in_2021'].astype('int')
Debts['Debt_in_2022'] = Debts['Debt_in_2022'].astype('int')
print(Debts['Debt_in_2018'])



Poor = Debts[(Debts.Debt_in_2018 >= -800000) & (Debts.Debt_in_2019 >= -800000)& \
             (Debts.Debt_in_2020 >= -800000)&(Debts.Debt_in_2021 >= -800000)&\
    (Debts.Debt_in_2022 >= -800000)].count()[0]
Developing = Debts[(Debts.Debt_in_2018 >= -80000) & (Debts.Debt_in_2019 >= -80000)& \
             (Debts.Debt_in_2020 >= -80000)&(Debts.Debt_in_2021 >= -80000)&\
    (Debts.Debt_in_2022 >= -80000)].count()[0]
Developed = Debts[(Debts.Debt_in_2018 >= -8000) & (Debts.Debt_in_2019 >= -8000)& \
             ((Debts.Debt_in_2020 >= -8000))&((Debts.Debt_in_2021 >= -8000))&\
    (Debts.Debt_in_2022 >= -8000)].count()[0]
weights = [Poor,Developing,Developed]
label = ['Poor Countries', 'Developing Countries','Developed Countries']
explode = (0,0,0)

plt.title('Debt of poor countries')

plt.pie(weights, labels=label, explode=explode, pctdistance=0.8,autopct='%.2f %%')
plt.show()


Poor = Debts[(Debts.Debt_in_2018 >= 800000) & (Debts.Debt_in_2019 >= 800000)& \
             (Debts.Debt_in_2020 >= 800000)&(Debts.Debt_in_2021 >= 800000)&\
    (Debts.Debt_in_2022 >= 800000)].count()[0]
Developing = Debts[(Debts.Debt_in_2018 >= 80000) & (Debts.Debt_in_2019 >= 80000)& \
             (Debts.Debt_in_2020 >= 80000)&(Debts.Debt_in_2021 >= 80000)&\
    (Debts.Debt_in_2022 >= 80000)].count()[0]
Developed = Debts[(Debts.Debt_in_2018 >= 8000) & (Debts.Debt_in_2019 >= 8000)& \
             ((Debts.Debt_in_2020 >= 8000))&((Debts.Debt_in_2021 >= 8000))&\
    (Debts.Debt_in_2022 >= 8000)].count()[0]

weights = [Poor,Developing,Developed]
label = ['Poor Countries', 'Developing Countries','Developed Countries']
explode = (0,0,0)

plt.title('IDA grants')

plt.pie(weights, labels=label, explode=explode, pctdistance=0.8,autopct='%.2f %%')
plt.show()




Argentina = Debts.loc[Debts.Country_Name == "Argentina"]['Debt_in_2020']
Brazil = Debts.loc[Debts.Country_Name == "Brazil"]['Debt_in_2020']
Mexico = Debts.loc[Debts.Country_Name == "Mexico"]['Debt_in_2020']

bp = plt.boxplot([Argentina, Brazil, Mexico], labels=['Argentina', 'Brazil', 'Mexico'], patch_artist=True,
                 medianprops={'linewidth': 2})

plt.title('Countries Net Balance in 2020')
plt.ylabel('2020 Overall Balance')

for box in bp['boxes']:
    # change outline color
    box.set(color='#4286f4', linewidth=2)
    # change fill color
    box.set(facecolor='#e0e0e0')
    # change hatch
    # box.set(hatch = '/')

plt.show()


Egypt = Debts.loc[Debts.Country_Name == "Egypt, Arab Rep."]['Debt_in_2020']
Nigeria = Debts.loc[Debts.Country_Name == "Nigeria"]['Debt_in_2020']
India = Debts.loc[Debts.Country_Name == "India"]['Debt_in_2020']

bp = plt.boxplot([Egypt, Nigeria, India], labels=['Egypt, Arab Rep.', 'Nigeria', 'India'], patch_artist=True,
                 medianprops={'linewidth': 2})

plt.title('Countries Net Balance in 2020')
plt.ylabel('2020 Overall Balance')

for box in bp['boxes']:
    # change outline color
    box.set(color='#4286f4', linewidth=2)
    # change fill color
    box.set(facecolor='#e0e0e0')
    # change hatch
    # box.set(hatch = '/')

plt.show()

IDA_total= Debts.loc[Debts.Country_Name == "IDA total"]['Debt_in_2020']
IDA = Debts.loc[Debts.Country_Name == "IDA only"]['Debt_in_2020']

bp = plt.boxplot([IDA_total,IDA], labels=['IDA total', 'IDA only'], patch_artist=True,
                 medianprops={'linewidth': 2})

plt.title('Debt Total vs. Debt only')
plt.ylabel('Debt numbers')

for box in bp['boxes']:
    # change outline color
    box.set(color='#4286f4', linewidth=2)
    # change fill color
    box.set(facecolor='#e0e0e0')
    # change hatch
    # box.set(hatch = '/')

plt.show()


Upper_Middle= Debts.loc[Debts.Country_Name == "Upper middle income"]['Debt_in_2020']
Lower = Debts.loc[Debts.Country_Name == "Low income"]['Debt_in_2020']
Lowest = Debts.loc[Debts.Country_Name == "Least developed countries: UN classification"]['Debt_in_2020']
bp = plt.boxplot([Upper_Middle,Lower,Lowest],
                 labels=['Upper middle income'
                     , 'Low income'
                     ,'Least developed countries: UN classification']
                 , patch_artist=True,
                 medianprops={'linewidth': 2})

plt.title('Overall Balance in 2020')
plt.ylabel('Balance in 2020')

for box in bp['boxes']:
    # change outline color
    box.set(color='#4286f4', linewidth=2)
    # change fill color
    box.set(facecolor='#e0e0e0')
    # change hatch
    # box.set(hatch = '/')

plt.show()


Upper_Middle= Debts.loc[Debts.Country_Name == "Upper middle income"]['Debt_in_2021']
Lower = Debts.loc[Debts.Country_Name == "Low income"]['Debt_in_2021']
Lowest = Debts.loc[Debts.Country_Name == "Least developed countries: UN classification"]['Debt_in_2021']
bp = plt.boxplot([Upper_Middle,Lower,Lowest],
                 labels=['Upper middle income'
                     , 'Low income'
                     ,'Least developed countries: UN classification']
                 , patch_artist=True,
                 medianprops={'linewidth': 2})

plt.title('Overall Balance in 2021')
plt.ylabel('Balance in 2021')

for box in bp['boxes']:
    # change outline color
    box.set(color='#4286f4', linewidth=2)
    # change fill color
    box.set(facecolor='#e0e0e0')
    # change hatch
    # box.set(hatch = '/')

plt.show()
