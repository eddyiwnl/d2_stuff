"""d2_buy_sell.py: Buys and dismantles armor for legendary shard farming."""
__author__ = "3ddy-iwnl-"

import mouse
import keyboard
import time

TIME_BETWEEN_CLICK = 1
TIME_BETWEEN_ACTION = 1.25
TIME_TO_BUY = 3.2
NUM_CHESTPIECE = 3

# Uncomment the below code for getting mouse position
#print(mouse.get_position())

# Move and click
def mouse_action(x,y):
    mouse.move(x,y,absolute=True,duration=0)
    time.sleep(TIME_BETWEEN_CLICK)
    mouse.click(button='left')
    time.sleep(TIME_BETWEEN_ACTION)

# Buy
def buy_stuff(x,y):
    mouse.move(x,y,absolute=True,duration=0)
    time.sleep(TIME_BETWEEN_CLICK)
    mouse.press(button='left')
    time.sleep(TIME_TO_BUY)
    mouse.release(button='left')
    time.sleep(0.5)

# Dismantle
def dismantle_stuff():
    keyboard.press('f')
    time.sleep(TIME_BETWEEN_ACTION)
    keyboard.release('f')
    time.sleep(TIME_BETWEEN_ACTION)

# Start from character preview screen
for i in range(2):
    # GET TO CHARACTER PREVIEW SCREEN WITHIN 3 SECONDS OF STARTING
    time.sleep(3)
    # Collections
    mouse_action(1102, 53)
    # Armor
    mouse_action(906, 364)
    # Leveling
    mouse_action(421, 822)
    # Right-arrow
    mouse_action(1811, 578)
    # Buy chestpiece NUM_CHESTPIECE times
    for i in range(NUM_CHESTPIECE):
        buy_stuff(928, 872)
    # Leave to collection
    keyboard.press_and_release('esc')
    time.sleep(1.25)
    # Leave to screen
    keyboard.press_and_release('f1')
    time.sleep(1.25)
    # Open inv
    keyboard.press_and_release('f1')
    time.sleep(1.25)
    # Hover chestplate
    mouse_action(1406, 518)
    # Move right to dismantle
    mouse.move(1503, 519,absolute=True,duration=0)
    time.sleep(TIME_BETWEEN_CLICK)
    # Dismantle chestpiece NUM_CHESTPIECE times
    for i in range(NUM_CHESTPIECE):
        dismantle_stuff()