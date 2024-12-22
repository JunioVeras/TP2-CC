from flask import Flask, request, jsonify
import pickle

# Importar dados do pickle do modelo e acessar as regras, versão e data do modelo
with open('/app/data/model.pkl', 'rb') as f:
    loaded_data = pickle.load(f)

rules = loaded_data["rules"]
version = loaded_data["version"]
date = loaded_data["date"]

# Função que recebe músicas, regras e a confiança mínima para retornar a playlist de recomendação
def add_songs_based_on_rules(songs, rules=rules, min_confidence=0.7):
    recommended_songs = set() 
    for antecedent, consequent, confidence in rules:
        if confidence >= min_confidence and antecedent.issubset(songs): 
            recommended_songs.update(consequent)
    return list(recommended_songs)

app = Flask(__name__)

# Endpoint de recomendação da API, recebe uma lista de músicas e retorna recomendações de músicas baseadas na entrada
@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    
    if "songs" not in data:
        return jsonify({"error": "No 'songs' field found"}), 400
    songs = data["songs"]

    recommended_songs = add_songs_based_on_rules(songs)

    return jsonify({"songs": recommended_songs, "version": version, "model_date": date})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=52039)