# Create Module  (# After Run It will be have Pycache Folder Main Sale Module)
# from Sale import *  Bad practic Valible may dupicate
from Sale import calc_shipping, calc_tax  # Format 1 (Function)
import Sale  # Format 2 (Object)
calc_shipping()
calc_tax()
Sale.calc_shipping()
Sale.calc_tax()
