from fpgrowth_py import fpgrowth
from datetime import datetime
import pandas as pd
import pickle
import os

url = os.getenv("GIT_REPO_URL")

if url:
    df_playlists = pd.read_csv(url)
else:
    print("A variável de ambiente GIT_REPO_URL não está definida.")

# Criação da lista de playlists para utilização do algoritmo fp-growth
playlists = df_playlists.groupby('pid')['track_name'].apply(list).tolist()

# Métricas a serem fixadas
min_support = 0.1
min_confidence = 0.5
version = "1.0"
date = datetime.now().strftime("%d-%m-%Y")

# Utilização do FP-growth para criação dos itemsets frequentes e das regras de associação
frequent_itemsets, rules = fpgrowth(playlists, minSupRatio=min_support, minConf=min_confidence)

# Criação do arquivo pickle com as regras e outros metadados
pickle_data = {
    "rules": rules,
    "version": version,
    "date": date
}

with open('/ml/data/model.pkl', 'wb') as f:
    pickle.dump(pickle_data, f)

print("Modelo de recomendação gerado e salvo com sucesso!")