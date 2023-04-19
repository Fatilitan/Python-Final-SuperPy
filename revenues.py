# Imports
import csv
from datetime import date, timedelta, datetime
import os
import matplotlib.pyplot as plt
from rich.table import Table
from rich.console import Console

# File paths.
base_path = os.getcwd()
csv_path = os.path.join(base_path, 'csv')
txt_path = os.path.join(base_path, 'txt')

sold_path = os.path.join(csv_path, 'sold.csv')
bought_path = os.path.join(csv_path, 'bought.csv')
date_txt_path = os.path.join(txt_path, 'date.txt')

# get the current date
current_date = date.today()

# neem de datum vanuit de txt file
def get_time():
    with open(date_txt_path, 'r') as dates_file:
        for lines in dates_file.readlines():
            return lines

# functie om de datum wat als "vandaag" gezien word te veranderen.
def advance_time(days_amount):
    newest_date = get_time()
    convert_date = datetime.strptime(str(newest_date), f'%Y-%m-%d').date()
    new_date = convert_date + timedelta(days_amount)
    with open(date_txt_path, 'w') as dates_file:
        dates_file.write(str(new_date))
        print(new_date)
    return new_date

# functie om de totale omzet van de afgelopen, ingevoerde dagen (days_amount) te krijgen.
def get_revenue(days_amount):
    with open(sold_path, 'r') as sold_file:
        sold_reader = csv.reader(sold_file)

        report_date = current_date - timedelta(days_amount)

        revenue = 0

        # for loop die door alle rows van sold_reader loopt en de hoeveelheid verkochte producten vermenigvuldigd met de verkoopprijs.
        for row in sold_reader:
            if row[0] == 'id':
                continue
            convert_row_date = datetime.strptime(row[4], f'%Y-%m-%d').date()
            if report_date >= convert_row_date:
                continue
            product_revenue = int(row[3])*float(row[5])
            revenue += product_revenue

        return Console().print(f'The revenue over the last {days_amount} days is "€{round(revenue, 2)}"')

# functie om de totale omzet per dag van de afgelopen, ingevoerde dagen (days_amount) te krijgen.
def show_revenue(days_amount):
    with open(sold_path, 'r') as sold_file:
        sold_reader = csv.reader(sold_file)

        report_date = current_date - timedelta(days_amount)

        date_and_revenue = {}

        for row in sold_reader:
            if row[0] == 'id':
                continue
            convert_row_date = datetime.strptime(row[4], f'%Y-%m-%d').date()
            if report_date >= convert_row_date:
                continue
            revenue = int(row[3]) * float(row[5])
            date = row[4]
            if date in date_and_revenue:
                date_and_revenue[date] += revenue
            else:
                date_and_revenue.update({date: revenue})

        # x- & y-as klaarmaken voor de grafiek
        dates = list(date_and_revenue.keys())
        revenue = list(date_and_revenue.values())
        # x- & y-as plotten in de grafiek
        plt.plot(dates, revenue)
        plt.show()

# functie om de totale winst van de afgelopen, ingevoerde dagen (days_amount) te krijgen.
def show_profit(days_amount):
    with open(sold_path, 'r') as sold_file:
        sold_reader = csv.reader(sold_file)

        report_date = current_date - timedelta(days_amount)
        revenue = 0

        # for loop die door alle rows van sold_reader loopt en de hoeveelheid verkochte producten vermenigvuldigd met de verkoopprijs.
        for row in sold_reader:
            if row[0] == 'id':
                continue
            convert_row_date = datetime.strptime(row[4], f'%Y-%m-%d').date()
            if report_date >= convert_row_date:
                continue
            revenue += int(row[3]) * float(row[5])
        
        corrected_price = round(revenue * 0.04, 2) # Winstmarge voor de winkel is 4%
        
        return Console().print(f'The total profit over the last {days_amount} days is "€{corrected_price}"')

# functie die toont hoeveel producten er nog in de inventaris zitten van de afgelopen, ingevoerde dagen. Als het product overdatum is dan wordt het door de functie niet meegeteld. 
def show_product_amount(product):
    with open(bought_path, 'r') as bought_file:
        bougt_reader = csv.reader(bought_file)

        amount = 0

        # for loop die door alle rows van sold_reader loopt en de hoeveelheid verkochte producten vermenigvuldigd met de verkoopprijs.
        for row in bougt_reader:
            if row[0] == 'id':
                continue
            convert_row_date = datetime.strptime(row[5], f'%Y-%m-%d').date()
            if current_date >= convert_row_date:
                continue
            if product in row:
                amount += int(row[3])
        
        return Console().print(f'The product "{product}" has {amount} units in stock')

# functie die alle info over een product toont in de inventaris over de afgelopen, ingevoerde dagen.
def show_product_inventory(days_amount, product):
    with open(bought_path, 'r') as bought_file:
        bougt_reader = csv.reader(bought_file)

        report_date = current_date - timedelta(days_amount)

        product_list = [['id','product_name','buy_price','amount','buy_date','experation_date']]
        
        # tabel voor in de console alvast stylen
        table = Table(title=f'{product} inventory')
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
            convert_row_date = datetime.strptime(row[4], f'%Y-%m-%d').date()
            if report_date >= convert_row_date:
                continue
            if product in row:
                product_list.append(row)

        # de items in product_list toevoegen aan de tabel ("table")
        for i in product_list:
            if i[0] == 'id':
                continue
            else:
                table.add_row(i[0], i[1], i[2], i[3], i[4], i[5])

        return Console().print(table)

# functie die alle info over een product toont in de inventaris over de afgelopen, ingevoerde dagen.  
def show_sold_products(days_amount):
    with open(sold_path, 'r') as sold_file:
        sold_reader = csv.reader(sold_file)

        report_date = current_date - timedelta(days_amount)

        product_list = [['id','bought_id','product_name','amount','sell_date','sell_price']]
        
        # tabel voor in de console alvast stylen
        table = Table(title=f'selling log last {days_amount} days')
        table.add_column(product_list[0][0], style='cyan')
        table.add_column(product_list[0][1], style='purple')
        table.add_column(product_list[0][2], style='green')
        table.add_column(product_list[0][3], style='yellow')
        table.add_column(product_list[0][4], style='deep_sky_blue3')
        table.add_column(product_list[0][5], style='dark_orange3')

        # for loop die door alle rows van sold_reader loopt en de rows toevoegd aan "product_list"
        for row in sold_reader:
            if row[0] == 'id':
                continue
            convert_row_date = datetime.strptime(row[4], f'%Y-%m-%d').date()
            if report_date >= convert_row_date:
                continue
            product_list.append(row)

        # de items in product_list toevoegen aan de tabel ("table")
        for i in product_list:
            if i[0] == 'id':
                continue
            else:
                table.add_row(i[0], i[1], i[2], i[3], i[4], i[5])

        return Console().print(table)