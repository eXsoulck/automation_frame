
def test_adding_to_cart(inventory_page):
    inventory_page.add_to_cart()
    assert inventory_page.shopping_cart_value() == "1"


def test_sorting_products_z_to_a(inventory_page):
    default_order = inventory_page.get_items_manes()
    inventory_page.sorting_z_to_a()
    revers_order = inventory_page.get_items_manes()
    assert revers_order == sorted(default_order, reverse=True)


def test_sorting_price_hi_to_lo(inventory_page):
    default_order = inventory_page.get_items_price()
    inventory_page.price_hig_to_low()
    hi_to_lo_price = inventory_page.get_items_price()
    assert hi_to_lo_price == sorted(default_order, reverse=True)


def test_menu_button(inventory_page):
    result = inventory_page.menu_button_click()
    assert result == "false"
