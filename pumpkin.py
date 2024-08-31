import json
import os
os.environ["HEADLESS"] = "True"
from pathlib import Path
from src.layouts import NormalLayout
from src.templates import BorderlessVectorTemplate
from src.utils.adobe import PhotoshopHandler
# from src import (
#         APP, CFG, CON, CONSOLE, ENV,
#         PLUGINS, TEMPLATES, TEMPLATE_MAP, TEMPLATE_DEFAULTS)

# Initialize the Photoshop application handler
photoshop_app = PhotoshopHandler()

# Define the path to your template PSD file
template_path = Path("C:\\Users\\Sam\\Documents\\FblthpFoundries\\fblthp\\Proxyshop\\templates\\borderless-vector.psd")  # Adjust the path as needed

# Define the Scryfall data for your card
scryfall_data = json.loads(open("C:\\Users\\Sam\\Documents\\FblthpFoundries\\fblthp\\wonder.json").read())

# Load the path to your card's image file
art_file_path = Path("C:/Users/Sam/Desktop/art pool/ER/lands/sadf.jpg")  # Adjust the path as needed



# Instantiate the layout object
card_layout = NormalLayout(
    scryfall=scryfall_data,
    file={
        'file': art_file_path,
        'name': scryfall_data['name'],
        'artist': scryfall_data['artist'],
        'set': scryfall_data['set'],
        'creator': None
    }
)
card_layout.template_file = template_path
# Instantiate the template directly
template_object = BorderlessVectorTemplate(card_layout)

# Start the rendering process

# Assuming the template object has an execute method
current_render = template_object  # Directly use the instantiated template object
result = current_render.execute()

if result:
    print(f"Rendering completed successfully!")
else:
    print(f"Rendering failed: Unknown error")
