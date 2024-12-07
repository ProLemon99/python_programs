from io import BytesIO
from PIL import Image
import requests

# Get the response from the API
response = requests.get('https://zenquotes.io/api/image')

# Check if the request was successful
if response.status_code == 200:
    # Open the image from the binary content
    image_data = BytesIO(response.content)
    image = Image.open(image_data)
    image.show()
else:
    print('Failed to fetch image. Status code:', response.status_code)