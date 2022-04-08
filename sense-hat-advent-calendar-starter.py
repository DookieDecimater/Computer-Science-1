from sense_hat import SenseHat
from time import sleep, strftime
from time import strftime


sense = SenseHat()

# ------------------------------------------------
# DATA
# ------------------------------------------------

# Colours
colours = {

  'r' : [255, 0, 0],
  # Add orange, yellow, green, blue, indigo, violet here
  'o' : [255, 100, 0],
  'n' : [135, 80, 22],
  'w' : [255, 255, 255],
  'y' : [255, 230, 0],
  'g' : [12, 131, 0],
  'b' : [0, 70, 190],
  'i' : [92, 54, 201],
  'v' : [102, 0, 213],
  's' : [232, 166, 129],
  'e' : [0, 0, 0]  # e stands for empty/black

}

# Pictures
with open("pictures.txt", "r") as f:
    all_pics = f.readlines()
   

# ------------------------------------------------
# FUNCTIONS
# ------------------------------------------------
# Display a given picture string on the sense HAT
# ------------------------------------------------
def display_pic(pic_string):


  # Get rid of newline and split the line into a list
    pic_string = pic_string.strip("\n")
    pic_string = pic_string.split(",")


  # Look up each letter in the dictionary of colours and add it to the list
    pic_list = []
    for letter in pic_string:
        pic_list.append(colours[letter])

  # Display the pixel colours from the file
    sense.set_pixels(pic_list)

day
# ------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------
while True:
    
    sense.clear()
    sleep(3)
    display_pic(all_pics[8])
        
    day = int(strftime("%d"))    # Results in '23'
    month = strftime("%d/%m/%y")  # Results in 'October'
    whole_date = strftime("%d/%m/%y")   # Results in '23/10/17'
    print(day)

    event = sense.stick.wait_for_event()
    if event.action == "pressed" and event.direction == "middle":
        today = int(strftime("%d"))
        month = strftime("%B")
        sense.show_message(str(day))
  
    if month == 'December' and day < 25:
        sense.show_message(str(day)) #converts day into a string
        display_pic(allpics[day])
        sleep(5)
  