# Imports
import argparse
from revenues import *
from csvscripts import *
from products import *

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

def main():
    # Een global parser maken & een subparser
    global_parser = argparse.ArgumentParser(prog="superpy")
    subparsers = global_parser.add_subparsers(
        dest='commands', title="commands", help="add superpy subcommands", required=True
    )

    # parsers toevoegen aan de subparsers
    get_revenue_parser = subparsers.add_parser('get-revenue', help='add the amount of days it will collect the revenue from')
    show_revenue_parser = subparsers.add_parser('show-revenue', help='add the amount of days it will collect the revenue from')
    show_profit_parser = subparsers.add_parser('show-profit', help='add the amount of days it will collect the revenue from')
    show_product_amount_parser = subparsers.add_parser('show-product-amount', help='add the name of the product you want the inventory amount of')
    show_product_inventory_parser = subparsers.add_parser('show-product-inventory', help='add the amount of days it will collect the revenue from, and the name of the product you want to see the inventory of')
    show_sold_products_parser = subparsers.add_parser('show-sold-products', help='add the amount of days it will collect the revenue from')
    advance_time_parser = subparsers.add_parser('advance-time', help='add the amount of days you want to advance')
    buy_products_parser = subparsers.add_parser('buy-products', help='add the amount of days it will collect the revenue from')
    sell_products_parser = subparsers.add_parser('sell-products', help='add the amount of days it will collect the revenue from')
    read_inventory_parser = subparsers.add_parser('read-inventory', help='read the inventory')

    # argumenten toevoegen aan de parsers
    get_revenue_parser.add_argument('--days', help='insert a number of days', type=int)
    show_revenue_parser.add_argument('--days', help='insert a number of days', type=int)
    show_profit_parser.add_argument('--days', help='insert a number of days', type=int)
    show_product_amount_parser.add_argument('--days', help='insert a number of days', type=int)
    show_product_amount_parser.add_argument('--product', help='insert name of product', type=str)
    show_product_inventory_parser.add_argument('--days', help='insert a number of days', type=int)
    show_product_inventory_parser.add_argument('--product', help='insert name of product', type=str)
    show_sold_products_parser.add_argument('--days', help='insert a number of days', type=int)
    advance_time_parser.add_argument('--days', help='insert a number of days', type=int)
    buy_products_parser.add_argument('--amount', help='instert the amount of products', type=int)
    buy_products_parser.add_argument('--product', help='instert the product name', type=str)
    sell_products_parser.add_argument('--amount', help='instert the amount of products', type=int)
    sell_products_parser.add_argument('--product', help='instert the product name', type=str)

    args = global_parser.parse_args()

    # functies callen door middel van argparse
    if args.commands == 'get-revenue':
        get_revenue(args.days)
    if args.commands == 'show-revenue':
        show_revenue(args.days)
    if args.commands == 'show-profit':
        show_profit(args.days)
    if args.commands == 'show-product-amount':
        show_product_amount(args.product)
    if args.commands == 'show-product-inventory':
        show_product_inventory(args.days, args.product)
    if args.commands == 'show-sold-products':
        show_sold_products(args.days)
    if args.commands == 'advance-time':
        current_date = advance_time(args.days)

    if args.commands == 'buy-products': # python csvscripts.py buy-products --amount 10 --product beets --buy_price 1.0 --product_type fruits
        for i in products_list:
            if i.name == args.product:
                i.buy_products(args.amount)
                break
            else:
                raise ValueError('The product is not in deliverable by your wholesaler')

    if args.commands == 'sell-products': # python csvscripts.py sell-products --amount 10 --product orange
        for i in products_list:
            if i.name == args.product:
                i.sell_products(args.amount)
                break
            else:
                raise ValueError('The product is not in deliverable by your wholesaler')

    if args.commands == 'read-inventory':
        read_inventory()

if __name__ == "__main__":
    main()