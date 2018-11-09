import numpy as np
import pandas as pd
df = pd.read_csv('BL-Flickr-Images-Book.csv')
df.head()
df.columns
to_drop=['Edition Statement',
...            'Corporate Author',
...            'Corporate Contributors',
...            'Former owner',
...            'Engraver',
...            'Contributors',
...            'Issuance type',
...            'Shelfmarks']
df.drop(to_drop,inplace=True,axis=1)
df=df.set_index('Identifier',inplace=True)
df.loc[206]
df.get_dtype_counts()
ex=df['Date of Publication'].str.extract(r'^(\d{4})',expand=False)
ex.head()
df['Date of Publication']=pd.to_numeric(ex)
df['Date of Publication'].dtype
df['Date of Publication'].isnull().sum()
pub=df['Place of Publication']
london=pub.str.contains('London')
london[:10]
oxford=pub.str.contains('Oxford')
df['Place of Publication']=np.where(london,'London',
                                    np.where(oxford,'Oxford',
                                             pub.str.replace('-',' ')))


ut=[]
with open('university_towns.txt') as file:
    for i in file:
        if'[edit]' in i:
            state=i
        else:
            ut.append((state,i))
ut[:5]
towns_df=pd.DataFrame(ut,columns=['state','region'])
def get_citystate(item):
    if '(' in item:
        return item[:item.find('(')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item

towns_df=towns_df.applymap(get_citystate)
towns_df.head()
                    
olympics_df=pd.read_csv('olympics.csv',header=1)
olympics_df.head()
olympics_df.columns
new_names={'Unnamed: 0':'Country',
           '? Summer':'Summer Olympics',
           '01 !':'Gold',
           '02 !':'Silver',
           '03 !':'Bronze',
           'Total':'Total',
           '? Winter':'Winter Olympics',
           '01 !.1':'Gold',
           '02 !.1':'Silver',
           '03 !.1':'Bronze',
           'Total.1':'Total',
           '? Games':'#Games',
           '01 !.2':'Gold',
           '02 !.2':'Silver',
           '03 !.2':'Bronze'}
olympics_df.rename(columns=new_names,inplace=True)
