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

from src.visualizations import (
    desenhar_bst
)

bst = BinarySearchTree()

for municipio in municipios:
    bst.insert(municipio)

desenhar_bst(
    bst.root
)