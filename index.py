"""
Simplified molecular-input line-entry system (SMILES)

Desenvolvido por: Tiago Neiva Andrade
para: Teste de Seleção para vaga de Estagiário Python da Altox Lab

Fontes de apoio: https://stackoverflow.com/questions/31826335/how-to-convert-pil-image-image-object-to-base64-string
                 http://flask.pocoo.org/docs/1.0/quickstart/#routing
"""

# imports
import base64
from io import BytesIO

from rdkit import Chem
from rdkit.Chem import Draw

from flask import Flask

# instância flask - web app
web_app = Flask(__name__)

# rota /drawMolecule/
@web_app.route("/drawMolecule/<molecula>")
def drawMolecule(molecula):
    
    # buffer
    bff = BytesIO()
    
    # desenha a imagem
    draw_im = Draw.MolToImage(Chem.MolFromSmiles(molecula))
    draw_im.save(bff, format="PNG")
    
    # base64 encode
    im_to_b64 = base64.b64encode(bff.getvalue())
    
    return "<img src=\"data:image/png;base64, " + str(im_to_b64)[2:-1] + "\">"