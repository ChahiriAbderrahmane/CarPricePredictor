import os
import json

def convert_txt_to_json_extension(directory):
    for filename in os.listdir(directory):
        # Chemin complet du fichier
        file_path = os.path.join(directory, filename)
        
        # Vérifier si c'est un fichier avec une extension .txt
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            try:
                # Lire le contenu du fichier pour vérifier le format JSON
                with open(file_path, 'r', encoding='utf-8') as file:
                    json.load(file)  # Valider que le contenu est au format JSON
                
                # Nouveau nom avec extension .json
                new_filename = f"{os.path.splitext(filename)[0]}.json"
                new_file_path = os.path.join(directory, new_filename)
                
                # Renommer le fichier
                os.rename(file_path, new_file_path)
                print(f"Renommé : {filename} -> {new_filename}")
            
            except json.JSONDecodeError:
                print(f"Erreur : {filename} n'est pas un fichier JSON valide.")
            except Exception as e:
                print(f"Erreur inattendue pour {filename} : {e}")

# Exemple d'utilisation
repertoire = "C:\\Users\\elect\\Desktop\\ds_cars_proj\\data"
convert_txt_to_json_extension(repertoire)
