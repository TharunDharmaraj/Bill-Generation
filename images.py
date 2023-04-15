# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from num2words import num2words
from imgix import UrlBuilder
import img2pdf


def image(message_details):
    # Open an Image
    img = Image.open('Bill_of_Sale_best.jpg')

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)

    # Custom font style and font size
    myFont = ImageFont.truetype('Arialn.ttf', 50)

    # Initialization
    year = message_details[0]   # "2022"
    make = message_details[1]   # "Toyota"
    model = message_details[2]  # "Model Name 127XB"
    price_in_word = num2words(message_details[3])
    price_in_number = message_details[3]
    date = message_details[4]   # "12 Nov 2022"

    # YEAR
    I1.text((200, 1260), year, font=myFont, fill=(0, 0, 0))
    # make
    I1.text((610, 1260), make, font=myFont, fill=(0, 0, 0))
    # model
    I1.text((1160, 1260), model, font=myFont, fill=(0, 0, 0))
    # price in word
    I1.text((150, 2010), price_in_word + " only/-",
            font=myFont, fill=(0, 0, 0))
    # price in number
    I1.text((2080, 2020), price_in_number + "/-", font=myFont, fill=(0, 0, 0))
    date
    I1.text((550, 2575), date, font=myFont, fill=(0, 0, 0))

    # Display edited image
    img.show()

    # Save the edited image
    img.save("new.png")

    from imgur import upload_image
    image_url = upload_image('new.png')

    return image_url
