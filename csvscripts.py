# Imports
import pandas as pd
import numpy as np
import csv
from datetime import date, timedelta, datetime
import os
from rich.table import Table
from rich.console import Console

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

# File paths.
base_path = os.getcwd()
csv_path = os.path.join(base_path, 'csv')

# get current dates
current_date = date.today()

# Inventory printen
def read_inventory():
    with open(rf'{csv_path}\bought.csv', 'r') as bought_file:
        bougt_reader = csv.reader(bought_file)

        product_list = [['id','product_name','buy_price','amount','buy_date','experation_date']]
        
        # tabel voor in de console alvast stylen
        table = Table(title='product inventory')
        table.add_column(product_list[0][0], style='cyan')
        table.add_column(product_list[0][1], style='purple')
        table.add_column(product_list[0][2], style='green')
        table.add_column(product_list[0][3], style='yellow')
        table.add_column(product_list[0][4], style='deep_sky_blue3')
        table.add_column(product_list[0][5], style='dark_orange3')

        # for loop die door alle rows van sold_reader loopt en de rows toevoegd aan "product_list" die de parameter "product" bevatten
        for row in bougt_reader:
            if row[0] == 'id':
                continue
            product_list.append(row)

        # de items in product_list toevoegen aan de tabel ("table")
        for i in product_list:
            if i[0] == 'id':
                continue
            else:
                table.add_row(i[0], i[1], i[2], i[3], i[4], i[5])

    bought_file.close()
    return Console().print(table)

# classes voor producten
class Products():
    def __init__(self, name, buy_price, product_type):
        self.name = name
        self.buy_price = buy_price
        self.product_type = product_type

    def buy_products(self, amount):

        with open(rf'{csv_path}\bought.csv', 'r') as product_file:
            bought_reader = csv.reader(product_file)

            # for-loop om te kijken of er al een product in de csv-file zit die de zelfde naam EN koopdatum heeft.
            # deze for-loop kijkt slaat de id in een variabele op zodat de volgende row in de csv-file een juiste id heeft.
            row_count = 0
            action = 'add new line' 
            for row in bought_reader:
                row_count += 1
                if self.name in row and str(current_date) == str(row[4]):
                    action = 'add to product line'
                    store_amount = row[3]
            id_count = row_count

            with open(rf'{csv_path}\bought.csv', 'a', newline='') as bought_file:
                bought_writer = csv.writer(bought_file, delimiter=',')
                line = []

                # Deze code creeërt een dynamische vervaldatum op basis van het product-type
                if self.product_type == 'vegetables' or self.product_type == 'fish' or self.product_type == 'fruits':
                    expiration_date = current_date + timedelta(days=+10)
                elif self.product_type == 'carbs' or self.product_type == 'sweets':
                    expiration_date = current_date + timedelta(days=+600)
                elif self.product_type == 'snacks':
                    expiration_date = current_date + timedelta(days=+1200)
                elif self.product_type == 'meats':
                    expiration_date = current_date + timedelta(days=+18)

                if action == 'add new line':
                    line.append(id_count)
                    line.append(self.name)
                    line.append(self.buy_price)
                    line.append(amount)
                    line.append(current_date)
                    line.append(expiration_date)
                    bought_writer.writerow(line)
                else:
                    # Als de klant producten koopt die al in de csv-file staan (zelfde naam & koop-datum), dan wordt de hoeveelheid (amount) verhoogd i.p.v. een hele nieuwe regel aanmaken.
                    new_amount = int(store_amount) + amount
                    bought_reader_pd = pd.read_csv(rf'{csv_path}\bought.csv')
                    bought_reader_pd['amount'] = np.where((bought_reader_pd['product_name'] == self.name)
                                                          & (bought_reader_pd['buy_date'] == str(current_date)),
                                                          new_amount, bought_reader_pd['amount'])
                    bought_reader_pd.to_csv(rf'{csv_path}\bought.csv', index=False)
            bought_file.close()
        product_file.close()

        return print(f'"{self.name}" has been bought & added to the inventory')

        # Functie om de inventory te updaten na dat een product is verkocht.
    def update_inventory(self, id, amount):
        inventory_pd = pd.read_csv(rf'{csv_path}\bought.csv')
        with open(rf'{csv_path}\bought.csv', 'r') as bought_file:
            bought_reader = csv.reader(bought_file)

            for row in bought_reader:
                if row[0] == str(id):
                    bought_amount = int(row[3])
        bought_file.close()

        new_amount = bought_amount - amount
        inventory_pd['amount'] = np.where(inventory_pd['id'] == id, new_amount, inventory_pd['amount'])
        inventory_pd.to_csv(rf'{csv_path}\bought.csv', index=False)
    
    def sell_products(self, amount):
        with open(rf'{csv_path}\bought.csv', 'r') as bought_file:
            bought_reader = csv.reader(bought_file)

            # for-loop om te kijken of het product wat verkocht moet worden in bought.csv staat
            # deze for-loop kijkt slaat de id in een variabele op zodat de volgende row in de csv-file een juiste id heeft.
            # Deze for-loop zorgt ook dat de klant NIET een product verkoopt die al overdatum is.
            in_bought_file = 'no'
            for row in bought_reader:
                if self.name in row:
                    expiration_date = row[5]
                    convert_date = datetime.strptime(expiration_date, f'%Y-%m-%d').date()
                    if int(row[3]) <= 0:
                        continue
                    if current_date < convert_date:
                        store_id = row[0]
                        in_bought_file = 'yes'

        bought_file.close()

        with open(rf'{csv_path}\sold.csv', 'r') as sold_file:
            sold_reader = csv.reader(sold_file)

            # Je kan niet een product verkopen die je als winkel niet hebt ingekocht. Dus als het product niet in bought.csv krijgt de console een error.
            if in_bought_file == 'no':
                raise ValueError('Product does not exist in inventory.')

            # for-loop om te kijken of er al een product in de csv-file zit die de zelfde naam EN koopdatum heeft.
            # deze for-loop kijkt slaat de id in een variabele op zodat de volgende row in de csv-file een juiste id heeft.
            row_count = 0
            action = 'add new line' 
            for row in sold_reader:
                row_count += 1
                if self.name in row and str(current_date) == str(row[4]):
                    action = 'add to product line'
                    store_amount = row[3]
            id_count = row_count

        sold_file.close()

        with open(rf'{csv_path}\sold.csv', 'a', newline='') as sold_file:
            sold_writer = csv.writer(sold_file, delimiter=',')
            line = []

            sell_price = round(self.buy_price * 1.04, 2) # Winstmarge voor de winkel is 4%

            if action == 'add new line':
                line.append(id_count)
                line.append(store_id)
                line.append(self.name)
                line.append(amount)
                line.append(current_date)
                line.append(sell_price)

                sold_writer.writerow(line)
            else:
                # Als de klant producten verkoopt die al in de csv-file staan (zelfde naam & koop-datum), dan wordt de hoeveelheid (amount) verhoogd i.p.v. een hele nieuwe regel aanmaken.
                new_amount = int(store_amount) + amount
                sold_reader_pd = pd.read_csv(rf'{csv_path}\sold.csv')
                sold_reader_pd['amount'] = np.where((sold_reader_pd['product_name'] == self.name)
                                                        & (sold_reader_pd['sell_date'] == str(current_date)),
                                                        new_amount, sold_reader_pd['amount'])
                sold_reader_pd.to_csv(rf'{csv_path}\sold.csv', index=False)
            self.update_inventory(int(store_id), amount)
        sold_file.close()

        return print(f'"{self.name}" has been sold at the price of: "€{round(sell_price*amount, 2)}"')