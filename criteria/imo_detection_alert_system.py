import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="your username",
  password="your password",
  database="db"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROm Schedule")
myresult = mycursor.fetchall()
print(myresult)
for x in myresult:
  print(x)

import pytesseract
import pushbullet
from PIL import Image

# Initialize Pushbullet with your API key
pb = pushbullet.Pushbullet('Your API KEY')

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = 'c:/Program Files/Tesseract-OCR/tesseract.exe'

def get_text(img):
    text = ""
    image = Image.open(img)
    text = pytesseract.image_to_string(image)
    if text == "":
        return "no text"
    else:
        return text

text = get_text("c:/Users/Admin/Downloads/imo1.jpg")

# Process the text to extract digits and create IMO number
res = list(filter(lambda x: x.isdigit(), text.split()))
res = [int(s) for s in res]
imo = "".join(map(str, res))
IMO = "IMO" + imo
print(IMO)

# Assuming you have defined myresult somewhere in your code
# Initialize the flag variable
flag = 0

# Check if the IMO number is not in any of the items in myresult
for i in myresult:
    if IMO not in i:
        flag = 1

# Send a notification if the flag is set
if flag == 1:
    push = pb.push_note('UNAUTHORIZED ACCESS', 'SEND CONCERNED OFFICIALS IMMEDIATELY')
    print("Notification sent: UNAUTHORIZED ACCESS")