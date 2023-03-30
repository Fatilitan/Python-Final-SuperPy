# Imports
from csvscripts import Products

# Geactiveerde producten die de klant kan kopen & verkopen, als de klant andere producten willen verkopen moeten ze het hier neer zetten

# fruits
orange = Products('orange', 0.8, 'fruits')
banana = Products('banana', 0.7, 'fruits')
pineapple = Products('pineapple', 1.7, 'fruits')
apple = Products('apple', 0.6, 'fruits')
grapes = Products('grapes', 2.1, 'fruits')
kiwi = Products('clementine', 0.7, 'fruits')
clementine = Products('clementine', 0.3, 'fruits')
mango = Products('mango', 3.3, 'fruits')
cantaloupe = Products('cantaloupe', 2.8, 'fruits')
melon = Products('melon', 2.6, 'fruits')
tomato = Products('tomato', 0.7, 'fruits')

# vegetables
cucumber = Products('cucumber', 0.9, 'vegetables')
cabbage = Products('cabbage', 0.7, 'vegetables')
greenbeans = Products('greenbeans', 0.8, 'vegetables')
broccoli = Products('broccoli', 1.4, 'vegetables')
potato = Products('potato', 0.5, 'vegetables')
pumpkin = Products('pumpkin', 4.4, 'vegetables')
beetroot = Products('beetroot', 0.5, 'vegetables')
carrot = Products('carrot', 1.4, 'vegetables')
spinach = Products('spinach', 0.9, 'vegetables')
corn = Products('corn', 0.8, 'vegetables')
onion = Products('onion', 0.6, 'vegetables')
zucchini = Products('zucchini', 1.2, 'vegetables')

# carbs
pasta = Products('pasta', 2.5, 'carbs')
spaghetti = Products('spaghetti', 2.5, 'carbs')
noodles = Products('noodles', 2.2, 'carbs')
bread = Products('bread', 1.4, 'carbs')
pita = Products('pita', 1.0, 'carbs')
tortilla = Products('tortilla', 1.4, 'carbs')
rice = Products('rice', 1.0, 'carbs')
cornflakes = Products('cornflakes', 1.2, 'carbs')

# meats
chicken = Products('chicken', 3.5, 'meats')
beef = Products('beef', 7.4, 'meats')
lamb = Products('lamb', 7.2, 'meats')
elk = Products('elk', 8.2, 'meats')
goat = Products('goat', 5.5, 'meats')
duck = Products('duck', 6.2, 'meats')
veal = Products('veal', 6.5, 'meats')
turkey = Products('turkey', 5.5, 'meats')
pork = Products('pork', 5.2, 'meats')

# fish
salmon = Products('salmon', 8.0, 'fish')
cod = Products('cod', 7.4, 'fish')
herring = Products('herring', 7.2, 'fish')
mackerel = Products('mackerel', 3.6, 'fish')
sardines = Products('sardines', 3.2, 'fish')
tuna = Products('tuna', 5.5, 'fish')
pollock = Products('pollock', 5.2, 'fish')
shrimp = Products('shrimp', 5.2, 'fish')
char = Products('char', 6.8, 'fish')
bass = Products('bass', 6.6, 'fish')

# sweets
chocolate = Products('chocolate', 1.5, 'sweets')
cookies = Products('cookies', 2.3, 'sweets')
cake = Products('cake', 3.0, 'sweets')
donut = Products('donut', 1.2, 'sweets')
caramels = Products('caramels', 3.2, 'sweets')
winegums = Products('winegums', 2.4, 'sweets')

# snacks
chips = Products('chips', 1.3, 'snacks')
crisps = Products('crisps', 1.3, 'snacks')
crackers = Products('crackers', 1.2, 'snacks')
cashewnuts = Products('cashewnuts', 2.8, 'snacks')

products_list = [orange, banana, pineapple, apple, grapes, kiwi, clementine, mango, cantaloupe, melon, tomato, cucumber, cabbage, greenbeans, broccoli, potato, pumpkin, beetroot, carrot, spinach, corn, onion, zucchini, pasta, spaghetti, noodles, bread, pita, tortilla, rice, cornflakes, chicken, beef, lamb, elk, goat, duck, veal, turkey, pork, salmon, cod, herring, mackerel, sardines, tuna, pollock, shrimp, char, bass, chocolate, cookies, cake, donut, caramels, winegums, chips, crisps, crackers, cashewnuts]