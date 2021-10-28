def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    return {key: items.count(key) for key in items}


def add_items(inventory, items):
    """
    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    unique_items = set(items)

    for item in unique_items:
        if item in inventory:
            inventory[item] += items.count(item)
        else: 
            inventory[item] = items.count(item)
    
    return inventory

def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    unique_items = set(items)

    for item in unique_items:
        if(inventory[item] - items.count(item)) < 0:
            inventory[item] = 0
        else:
            inventory[item] -= items.count(item)

    
    return inventory


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    inventory.pop(item, inventory)
    return inventory


def list_inventory(inventory):
    """
    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(key, inventory[key]) for key in inventory if inventory[key] > 0]
