import pandas as pd

df = pd.read_excel("datasets/real_estate_data.xlsx")

li_property_names = df['PropertyName'].tolist()

final_sim = pd.read_csv('datasets/final_sim.csv').to_numpy()


def recommend_properties_with_finalSimValue(x:str):
    ind = li_property_names.index(x)
    sims = final_sim[ind].tolist()
    numbered_sims = list(enumerate(sims))
    closer = sorted(numbered_sims, key=lambda x: x[1], reverse=True)[1:6]
    indices = []
    for idx, _ in closer:
        indices.append(idx)
    return df[['PropertyName']].loc[indices]