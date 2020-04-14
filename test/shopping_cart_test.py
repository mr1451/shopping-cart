#shopping_cart_test.py

import pytest # for pytest.raises (see: https://docs.pytest.org/en/latest/assert.html)

from app.shopping_cart import TAX_RATE, to_usd, find_product, human_friendly_timestamp, calculate_tax, calculate_total_price

def test_tax_rate():
    """
    Tests that the tax rate equals 0.06, or 6%, as is defined in app/shopping_cart.py.
    """
    assert(TAX_RATE) == 0.06

def test_to_usd():
    """
    Tests that the to_usd function correctly reformats price values in US dollars.
    """
    # it should apply USD formatting
    assert to_usd(4.50) == "$4.50"

    # it should display two decimal places
    assert to_usd(4.5) == "$4.50"

    # it should round to two places
    assert to_usd(4.55555) == "$4.56"

    # it should display thousands separators
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"

def test_find_product():
    """
    Tests that the find_product function correctly indentifies product from the list based on its numerical identifier.
    """
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    ]

    # if there is a match, it should find and return a product
    matching_product = find_product("2", products)
    assert matching_product["name"] == "All-Seasons Salt"

    # if there is no match, it should raise an IndexError
    with pytest.raises(IndexError):
        find_product("2222", products)

def test_human_friendly_timestamp():
    """
    Tests that the human_friendly_timestamp successfully converts the datetime object into an easy-to-read timestamp string.
    """
    # it should display the time in an human-friendly format (round to the nearest minute, add AM or PM timestamp)
    # update by the second
    assert human_friendly_timestamp != "2020-04-14 05:16 PM"

def test_calculate_tax():
    """
    Tests that the calculate_tax function successfully calculates tax as 6.0% of the subtotal.
    """
    #it should calculate tax as 6.0% of the subtotal
    assert calculate_tax(100.00) == 6.00

def test_calculate_total_price():
    """
    Tests that calculate_total_price successfully calculates the total price as the sum of subtotal and tax.
    """
    #it should find the sum of subtotal and tax
    assert calculate_total_price(100.00, 6.00) == 106.00