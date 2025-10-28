# """
# Manages a simple inventory system.

# This module allows adding, removing, and querying item quantities,
# as well as loading and saving the inventory to a JSON file.
# """

# import json
# import logging
# from datetime import datetime

# # Configure logging for the entire module.
# # This replaces all 'print' calls and fixes the 'unused import' error.
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# def add_item(stock_data, item, qty, logs=None):
#     """
#     Adds a specified quantity of an item to the stock data.

#     :param stock_data: The dictionary holding stock levels.
#     :param item: The name of the item (str).
#     :param qty: The quantity to add (int).
#     :param logs: A list to append log messages to.
#     """
#     # Fix for W0102: Dangerous default value []
#     if logs is None:
#         logs = []

#     # Fix for Manual Find: Input validation for logical error
#     if not isinstance(item, str) or not isinstance(qty, int):
#         logging.warning("Invalid types passed to add_item: item=%s (%s), qty=%s (%s)",
#                         item, type(item).__name__, qty, type(qty).__name__)
#         return

#     if not item:
#         logging.warning("Attempted to add an empty item.")
#         return

#     stock_data[item] = stock_data.get(item, 0) + qty

#     # Fix for C0209: Use of f-string
#     log_message = f"{datetime.now()}: Added {qty} of {item}"
#     logs.append(log_message)
#     logging.info(log_message)


# def remove_item(stock_data, item, qty):
#     """
#     Removes a specified quantity of an item from the stock data.

#     :param stock_data: The dictionary holding stock levels.
#     :param item: The name of the item to remove (str).
#     :param qty: The quantity to remove (int).
#     """
#     try:
#         current_qty = stock_data.get(item)
#         if current_qty is None:
#             # Re-raise KeyError to be caught by the except block
#             raise KeyError(f"Item '{item}' not in stock.")
        
#         stock_data[item] -= qty
#         if stock_data[item] <= 0:
#             del stock_data[item]
#             logging.info("Removed item %s from stock (quantity reached 0).", item)
#     # Fix for W0702, B110, E722: Bare 'except'
#     except KeyError as e:
#         logging.warning("Attempted to remove non-existent item: %s", e)
#     except TypeError:
#         logging.error("Invalid quantity (%s) for item %s.", qty, item)


# def get_qty(stock_data, item):
#     """
#     Gets the current quantity of a specific item.

#     :param stock_data: The dictionary holding stock levels.
#     :param item: The name of the item to query (str).
#     :return: The quantity of the item (int), or 0 if not found.
#     """
#     # Fix: Make function robust, prevents crash if item doesn't exist.
#     return stock_data.get(item, 0)


# def load_data(file="inventory.json"):
#     """
#     Loads inventory data from a JSON file.

#     :param file: The name of the file to load from.
#     :return: A dictionary with the stock data.
#     """
#     # Fix for W0603: Removed 'global' statement.
#     try:
#         # Fix for R1732: Use 'with'
#         # Fix for W1514: Specify encoding
#         with open(file, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         logging.warning("Inventory file %s not found. Starting with empty inventory.", file)
#         return {}
#     except json.JSONDecodeError:
#         logging.error("Could not decode JSON from %s. Starting with empty inventory.", file)
#         return {}


# def save_data(stock_data, file="inventory.json"):
#     """
#     Saves the inventory data to a JSON file.

#     :param stock_data: The dictionary holding stock levels.
#     :param file: The name of the file to save to.
#     """
#     try:
#         # Fix for R1732: Use 'with'
#         # Fix for W1514: Specify encoding
#         with open(file, "w", encoding="utf-8") as f:
#             json.dump(stock_data, f, indent=4)
#         logging.info("Inventory data saved to %s.", file)
#     except IOError as e:
#         logging.error("Could not save data to %s: %s", file, e)


# def print_data(stock_data):
#     """
#     Prints a report of all items and their quantities.

#     :param stock_data: The dictionary holding stock levels.
#     """
#     logging.info("--- Items Report ---")
#     if not stock_data:
#         logging.info("Inventory is empty.")
#         return
#     # Fix for Manual Find: Use descriptive var 'item', 'qty' and .items()
#     for item, qty in stock_data.items():
#         logging.info("%s -> %s", item, qty)
#     logging.info("--------------------")


# def check_low_items(stock_data, threshold=5):
#     """
#     Finds all items with a quantity below the threshold.

#     :param stock_data: The dictionary holding stock levels.
#     :param threshold: The low-stock threshold.
#     :return: A list of items below the threshold.
#     """
#     result = []
#     # Fix for Manual Find: Use descriptive var 'item', 'qty' and .items()
#     for item, qty in stock_data.items():
#         if qty < threshold:
#             result.append(item)
#     return result


# def main():
#     """
#     Main function to run the inventory system logic.
#     """
#     logs = []
#     # Fix for W0603: Initialize stock_data from load_data() return value
#     stock_data = load_data()

#     # Call all functions with snake_case and pass stock_data
#     add_item(stock_data, "apple", 10, logs)
#     add_item(stock_data, "banana", -2, logs)
#     # This invalid call is now safely handled by validation in add_item
#     add_item(stock_data, 123, "ten", logs)
#     remove_item(stock_data, "apple", 3)
#     # This non-existent item is now safely handled by 'except KeyError'
#     remove_item(stock_data, "orange", 1)

#     logging.info("Apple stock: %s", get_qty(stock_data, "apple"))
#     low_items = check_low_items(stock_data)
#     logging.info("Low items: %s", low_items)

#     save_data(stock_data)
#     # We can reload to prove it saved
#     stock_data_reloaded = load_data()
#     print_data(stock_data_reloaded)

#     # Fix for B307, W0123: Removed dangerous 'eval()' call
#     # eval("print('eval used')")


# # Fix: Add standard Python entry point guard
# if __name__ == "__main__":
#     main()


"""
Manages a simple inventory system.

This module allows adding, removing, and querying item quantities,
as well as loading and saving the inventory to a JSON file.
"""

import json
import logging
from datetime import datetime

# Configure logging for the entire module.
# This replaces all 'print' calls and fixes the 'unused import' error.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def add_item(stock_data, item, qty, logs=None):
    """
    Adds a specified quantity of an item to the stock data.

    :param stock_data: The dictionary holding stock levels.
    :param item: The name of the item (str).
    :param qty: The quantity to add (int).
    :param logs: A list to append log messages to.
    """
    # Fix for W0102: Dangerous default value []
    if logs is None:
        logs = []

    # Fix for Manual Find: Input validation for logical error
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid types passed to add_item: item=%s (%s), qty=%s (%s)",
                        item, type(item).__name__, qty, type(qty).__name__)
        return

    if not item:
        logging.warning("Attempted to add an empty item.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty

    # Fix for C0209: Use of f-string
    log_message = f"{datetime.now()}: Added {qty} of {item}"
    logs.append(log_message)
    logging.info(log_message)


def remove_item(stock_data, item, qty):
    """
    Removes a specified quantity of an item from the stock data.

    :param stock_data: The dictionary holding stock levels.
    :param item: The name of the item to remove (str).
    :param qty: The quantity to remove (int).
    """
    try:
        current_qty = stock_data.get(item)
        if current_qty is None:
            # Re-raise KeyError to be caught by the except block
            raise KeyError(f"Item '{item}' not in stock.")

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Removed item %s from stock (quantity reached 0).", item)
    # Fix for W0702, B110, E722: Bare 'except'
    except KeyError as e:
        logging.warning("Attempted to remove non-existent item: %s", e)
    except TypeError:
        logging.error("Invalid quantity (%s) for item %s.", qty, item)


def get_qty(stock_data, item):
    """
    Gets the current quantity of a specific item.

    :param stock_data: The dictionary holding stock levels.
    :param item: The name of the item to query (str).
    :return: The quantity of the item (int), or 0 if not found.
    """
    # Fix: Make function robust, prevents crash if item doesn't exist.
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Loads inventory data from a JSON file.

    :param file: The name of the file to load from.
    :return: A dictionary with the stock data.
    """
    # Fix for W0603: Removed 'global' statement.
    try:
        # Fix for R1732: Use 'with'
        # Fix for W1514: Specify encoding
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("Inventory file %s not found. Starting with empty inventory.", file)
        return {}
    except json.JSONDecodeError:
        logging.error("Could not decode JSON from %s. Starting with empty inventory.", file)
        return {}


def save_data(stock_data, file="inventory.json"):
    """
    Saves the inventory data to a JSON file.

    :param stock_data: The dictionary holding stock levels.
    :param file: The name of the file to save to.
    """
    try:
        # Fix for R1732: Use 'with'
        # Fix for W1514: Specify encoding
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Inventory data saved to %s.", file)
    except IOError as e:
        logging.error("Could not save data to %s: %s", file, e)


def print_data(stock_data):
    """
    Prints a report of all items and their quantities.

    :param stock_data: The dictionary holding stock levels.
    """
    logging.info("--- Items Report ---")
    if not stock_data:
        logging.info("Inventory is empty.")
        return
    # Fix for Manual Find: Use descriptive var 'item', 'qty' and .items()
    for item, qty in stock_data.items():
        logging.info("%s -> %s", item, qty)
    logging.info("--------------------")


def check_low_items(stock_data, threshold=5):
    """
    Finds all items with a quantity below the threshold.

    :param stock_data: The dictionary holding stock levels.
    :param threshold: The low-stock threshold.
    :return: A list of items below the threshold.
    """
    result = []
    # Fix for Manual Find: Use descriptive var 'item', 'qty' and .items()
    for item, qty in stock_data.items():
        if qty < threshold:
            result.append(item)
    return result


def main():
    """
    Main function to run the inventory system logic.
    """
    logs = []
    # Fix for W0603: Initialize stock_data from load_data() return value
    stock_data = load_data()

    # Call all functions with snake_case and pass stock_data
    add_item(stock_data, "apple", 10, logs)
    add_item(stock_data, "banana", -2, logs)
    # This invalid call is now safely handled by validation in add_item
    add_item(stock_data, 123, "ten", logs)
    remove_item(stock_data, "apple", 3)
    # This non-existent item is now safely handled by 'except KeyError'
    remove_item(stock_data, "orange", 1)

    logging.info("Apple stock: %s", get_qty(stock_data, "apple"))
    low_items = check_low_items(stock_data)
    logging.info("Low items: %s", low_items)

    save_data(stock_data)
    # We can reload to prove it saved
    stock_data_reloaded = load_data()
    print_data(stock_data_reloaded)

    # Fix for B307, W0123: Removed dangerous 'eval()' call
    # eval("print('eval used')")


# Fix: Add standard Python entry point guard
if __name__ == "__main__":
    main()

# Fix for C0304: Final newline missing