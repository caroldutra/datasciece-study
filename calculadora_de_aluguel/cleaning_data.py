
import pandas as pd
import numpy as np
df = pd.read_csv("raw_data.csv")

# Removendo Duplicados
df = df.drop_duplicates(keep="first", subset=[coluna for coluna in df.columns if coluna!="crawled_at"]).reset_index(drop=True)

# Removendo Anúncios
filtro_de_anuncios = [_id.isnumeric() for _id in df["id"]]

#Resetando index
df = df[filtro_de_anuncios].reset_index(drop=True)

# Removendo strings de campos numericos
df["rooms_limpo"] = (df["rooms"]
                     .str.split(" ")
                     .str[0]
                     .str.replace("--","0")
                     .astype(int))

df["bathrooms_limpo"] = (df["bathrooms"]
                         .str.split(" ")
                         .str[0]
                         .str.replace("--","0")
                         .astype(int))

df["garages_limpo"] = (df["garages"]
                       .str.split(" ")
                       .str[0]
                       .str.replace("--","0")
                       .astype(int))

df["price_limpo"] = [int(w.split("R$ ")[1].replace(".","")) for w in df["price"]]

df["condo"] = df["condo"].fillna("MISSING")

df["condo_limpo"] = [int(w.split("R$ ")[1].replace(".","")) if w!="MISSING" else np.nan for w in df["condo"]]

df["area_limpo"] = df["area"].astype(int)

#Passando a coluna "crawled_at" para datetime
df["crawled_at"] = pd.to_datetime(df["crawled_at"], format="%Y-%m-%d %H:%M")

#Removaendo colunas inúteis
df = df.drop(columns=["area", "rooms", "bathrooms", "garages", "price", "condo"])

#Limpando bairro
df["crawler"] = df["crawler"].str.lower().str.replace(" ","_")
df["crawler"] = df["crawler"].str.replace("fregesia","freguesia")

# Amenities
df = pd.concat([df, df["amenities"].str.get_dummies("\n")], axis = 1)

# Criando novo arquivo com dados limpos
df.to_csv("clean_data.csv", index = False)
