# all code made by ChatGPT

import itertools
import time
import threading
import pyautogui

# Create a list of all the English alphabet letters
alphabet = list("abcdefghijklmnopqrstuvwxyz")

# Generate all possible combinations of three letters
combinations = list(itertools.combinations(alphabet, 3))

# Initialize target coordinates
target_x, target_y = None, None

# Initialize a flag to start and stop the process
running = False

# Function to set the target coordinates
def set_target(event, x, y, flags, param):
    global target_x, target_y
    if event == cv2.EVENT_LBUTTONDOWN:
        target_x, target_y = x, y

# Function to start and stop the process
def toggle_process():
    global running
    while True:
        if running:
            for combo in combinations:
                if not running:
                    break
                text_to_type = "".join(combo)
                pyautogui.moveTo(target_x, target_y)
                pyautogui.click()
                pyautogui.write(text_to_type)
                pyautogui.press('enter')
                time.sleep(0.5)
        else:
            time.sleep(1)

# Create a window and set a mouse callback
cv2.namedWindow("Set Target")
cv2.setMouseCallback("Set Target", set_target)

# Create a thread to toggle the process
toggle_thread = threading.Thread(target=toggle_process)

# Start the toggle thread
toggle_thread.start()

while True:
    cv2.imshow("Set Target", np.zeros((100, 100), dtype=np.uint8))
    key = cv2.waitKey(10)
    if key == ord('q'):
        running = not running
    elif key == 27:
        break

# Stop the toggle thread when done
running = False
toggle_thread.join()

cv2.destroyAllWindows()