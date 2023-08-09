import pyautogui
import time
import keyboard

def press_key(key):
    pyautogui.press(key)

def move_disk(source, destination):    
    press_key(source)  # Press the source key to select a disk
    press_key(destination)  # Press the destination key to move the disk


def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        move_disk(source, destination)
    else:
        tower_of_hanoi(n - 1, source, destination, auxiliary)
        move_disk(source, destination)
        tower_of_hanoi(n - 1, auxiliary, source, destination)


def main():

    num_discs = 5  # Number of disks
    
    print("Press 'r' key to start the Tower of Hanoi game.")
    keyboard.wait("r")  # Wait for 'r' key press
    
    tower_of_hanoi(num_discs, "1", "2", "3")

if __name__ == "__main__":
    main()
