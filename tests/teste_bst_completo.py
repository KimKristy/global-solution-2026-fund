import sys
import os

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, ROOT_DIR)

from src.data_structures import (
    BinarySearchTree
)

from data.raw.municipios_rs import (
    municipios
)

bst = BinarySearchTree()

for municipio in municipios:
    bst.insert(municipio)

print("\nIN ORDER")
print(bst.in_order())

print("\nALTURA")
print(bst.height())

print("\nRISCO ENTRE 0.70 E 0.90")
print(
    bst.search_range(
        0.70,
        0.90
    )
)

bst.remove(0.55)

print("\nAPÓS REMOÇÃO")
print(
    bst.in_order()
)