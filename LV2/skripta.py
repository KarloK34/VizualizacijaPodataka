import json

def clean_data(data):
    cleaned_data = []

    for record in data:
        # Filtriranje None vrijednosti u svakom objektu
        cleaned_record = {key: value for key, value in record.items() if value is not None}
        cleaned_data.append(cleaned_record)

    return cleaned_data

def clean_json_file(input_file_path, output_file_path):
    # Učitavanje JSON podataka iz ulazne datoteke
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    # Čišćenje podataka
    cleaned_data = clean_data(data)

    # Spremanje očišćenih podataka u izlaznu datoteku
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        json.dump(cleaned_data, outfile, ensure_ascii=False, indent=4)

    print(f"Očišćeni podaci su spremljeni u {output_file_path}")

# Poziv funkcije s ulaznim i izlaznim file-ovima
input_file = 'podaci.json'  # Zamijenite s pravim putem do vašeg JSON file-a
output_file = 'ocisceni_podaci.json'  # Ime novog file-a s očišćenim podacima

clean_json_file(input_file, output_file)
