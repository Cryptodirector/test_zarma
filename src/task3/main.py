import json
import csv


class MergeData:
    def __init__(self, file_csv, file_json) -> None:
        self.file_csv = file_csv
        self.file_json = file_json

    def run(self):

        # Считать данные из csv

        products = {}
        with open(self.file_csv, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product_id = row['product_id']
                products[product_id] = {
                    'product_name': row['product_name']
                }



        # Считываеи данные из json
        sales = []
        with open(self.file_json, 'r') as file:
            sales = json.load(file)


        # Объединяем

        comb = []

        for sale in sales:
            product_id = sale['product_id']
            if str(product_id) in products:
                combined_entry = {
                    'product_id': product_id,
                    'product_name': products[str(product_id)]['product_name'],
                    'sale_id': sale['sale_id'],
                    'amount': sale['amount']
                }
                comb.append(
                    combined_entry
                )

        # На выходе получаем новый json
        
        with open('new_json.json', 'w') as f:
            json.dump(comb, f)


merge_data = MergeData(
    'products.csv',
    'data.json'
)
merge_data.run()
