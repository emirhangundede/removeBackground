from rembg import remove
from PIL import Image
import easygui as eg
input_path = eg.fileopenbox(title='İmage')
output_path = eg.filesavebox(title='Out')
input = Image.open(input_path)
output = remove(input)
output.save(output_path)