import requests

url_categories = 'https://fakestoreapi.com/products/categories'
response_categories = requests.get(url_categories)
categories = response_categories.json()

categories_list = ''
for i in range(len(categories)):
    category = categories[i]
    categories_list = categories_list + '\n' + category
print(categories_list)

category_choice = input('\nВыберите интересующую Вас категорию\n')

category_validator = category_choice in categories_list
if not category_validator:
    print('выбранная категория не найдена')
    exit(0)

# В API существует описание запроса
# "Get products in a specific category
# fetch('https://fakestoreapi.com/products/category/jewelery')
#             .then(res=>res.json())
#             .then(json=>console.log(json))"
# Но, к сожалению, он работает только с категорией ювелирных изделий, потому пришлось использовать другой способ

url_products = 'https://fakestoreapi.com/products'
products_response = requests.get(url_products)
products = products_response.json()

products_list = ''
for i in range(len(products)):
    product = products[i]
    if product['category'] == category_choice:
        product_article = f'{product["title"]}\n\t{product["description"]}\n\tprice: {product["price"]}\n\trating:\n\t\trate:{product["rating"]["rate"]}\n\t\tcount:{product["rating"]["count"]}\n\n'
        products_list = products_list + product_article

print(products_list)