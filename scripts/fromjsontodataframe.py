import os
import json
import pandas as pd

def process_json_to_dataframe(directory):
   all_data = []
   
   for filename in os.listdir(directory):
       if filename.endswith('.json'):
           file_path = os.path.join(directory, filename)
           
           try:
               with open(file_path, 'r', encoding='utf-8') as file:
                   data = json.load(file)
                   
                   cars = data.get('cars', [])
                   
                   for car in cars:
                       extracted_data = {
                            "Car Model": car.get('title').get('name') if car.get('title') and isinstance(car.get('title'), dict) and 'name' in car.get('title') else None,
                            "Condition": car.get('stocktype').get('name') if car.get('stocktype') and isinstance(car.get('stocktype'), dict) and 'name' in car.get('stocktype') else None,
                            "Mileage": car.get('mileage').get('name') if car.get('mileage') and isinstance(car.get('mileage'), dict) and 'name' in car.get('mileage') else None,
                            "Price (USD)": car.get('price').get('name') if car.get('price') and isinstance(car.get('price'), dict) and 'name' in car.get('price') else None,
                            "Monthly Payment": car.get('monthlypayment').get('name') if car.get('monthlypayment') and isinstance(car.get('monthlypayment'), dict) and 'name' in car.get('monthlypayment') else None,
                            "Dealer Name": car.get('vehicledealer').get('name') if car.get('vehicledealer') and isinstance(car.get('vehicledealer'), dict) and 'name' in car.get('vehicledealer') else None,
                        }
    
                       all_data.append(extracted_data)
           
           except Exception as e:
               print(f"Erreur dans {filename}: {e}")
   
   df = pd.DataFrame(all_data)
   return df

# Exemple d'utilisation
directory_path = "C:\\Users\\elect\\Desktop\\ds_cars_proj\\data"
df = process_json_to_dataframe(directory_path)
df.to_csv("combined_data.csv", index=False, encoding='utf-8')
print("Données sauvegardées")