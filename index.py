"""
Simplified molecular-input line-entry system (SMILES)

Desenvolvido por: Tiago Neiva Andrade
para: Teste de Seleção para vaga de Estagiário Python da Altox Lab
"""

# Imports
from rdkit import Chem

# Teste
print(Chem.MolFromSmiles("CCOCCNSC=0"))