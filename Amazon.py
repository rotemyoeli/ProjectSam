'''
To obtain an AWS access key and secret key, you will need to create an AWS account and generate a new access key and secret key in the AWS Management Console. Here are the steps to do so:

    1 Go to the AWS Management Console.

    2 Click on the "Sign in to the Console" button in the top right corner and sign in with your Amazon account.

    3 Once you're signed in, click on your account name in the top right corner and select "My Security Credentials" from the dropdown menu.

    4 Click on "Access keys (access key ID and secret access key)".

    5 Click on the "Create New Access Key" button.

    6 Download the access key file and keep it in a secure location, as you will not be able to download it again.

    7 Once you have your access key and secret key, you can use them in the Python code I provided earlier.

To obtain an AWS associate tag, you will need to sign up for the Amazon Associates Program. Here are the steps to do so:

    1 Go to the Amazon Associates Program website.

    2 Click on the "Join Now for Free" button.

    3 Sign in with your Amazon account or create a new account if you don't already have one.

    4 Follow the instructions to create your Amazon Associates account.

    5 Once you have your Amazon Associates account, you can generate an associate tag that you can use in the Python code I provided earlier.

'''

import bottlenose
from bs4 import BeautifulSoup

# set up Amazon Product Advertising API
amazon = bottlenose.Amazon(
    # replace with your own AWS access key
    AWS_ACCESS_KEY_ID='YOUR_ACCESS_KEY',
    # replace with your own AWS secret key
    AWS_SECRET_ACCESS_KEY='YOUR_SECRET_KEY',
    # replace with your own AWS associate tag
    AWS_ASSOCIATE_TAG='YOUR_ASSOCIATE_TAG',
)

# prompt user for parameters
search_term = input("What product are you looking for? ")
max_price = input("What is the maximum price you are willing to pay? ")

# search Amazon for products based on parameters
response = amazon.ItemSearch(
    SearchIndex='All',
    Keywords=search_term,
    MaximumPrice=max_price,
    Sort='price',
    ResponseGroup='ItemAttributes,Images',
)

# parse response and find best deal
soup = BeautifulSoup(response, 'xml')
items = soup.find_all('Item')
best_price = float('inf')
best_item = None
for item in items:
    item_price = float(item.ItemAttributes.ListPrice.Amount) / 100
    if item_price < best_price:
        best_price = item_price
        best_item = item

# print best deal
if best_item:
    print(f"The best deal for {search_term} is {best_item.ItemAttributes.Title.text} for ${best_price}.")
else:
    print(f"Sorry, no results found for {search_term} within your price range.")
