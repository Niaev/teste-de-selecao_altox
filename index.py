"""
Simplified molecular-input line-entry system (SMILES)

Desenvolvido por: Tiago Neiva Andrade
para: Teste de Seleção para vaga de Estagiário Python da Altox Lab
"""

# Imports
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import Draw

molecula = "O=C(C)Oc1ccccc1C(=O)O"
im_dir = "./images/"
im_type = ".png"
im_path = im_dir + molecula + im_type
imagem = Path(im_path)

if imagem.exists() == False:
    draw_im = Draw.MolToImage(Chem.MolFromSmiles(molecula))
    draw_im.save(im_path)