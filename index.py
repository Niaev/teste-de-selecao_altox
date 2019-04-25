"""
Simplified molecular-input line-entry system (SMILES)

Desenvolvido por: Tiago Neiva Andrade
para: Teste de Seleção para vaga de Estagiário Python da Altox Lab
"""

# Imports
from rdkit import Chem
from rdkit.Chem import Draw

# Teste
print(Draw.MolToImage(Chem.MolFromSmiles("CCOCCNSC=O"))) # PIL.Image.Image