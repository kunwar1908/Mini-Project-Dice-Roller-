import random
import time
import tkinter as tk

def roll_dice():
	dice_faces = [
		'''
		-------
		|     |
		|  o  |
		|     |
		-------''',
		'''
		-------
		| o   |
		|     |
		|   o |
		-------''',
		'''
		-------
		| o   |
		|  o  |
		|   o |
		-------''',
		'''
		-------
		| o o |
		|     |
		| o o |
		-------''',
		'''
		-------
		| o o |
		|  o  |
		| o o |
		-------''',
		'''
		-------
		| o o |
		| o o |
		| o o |
		-------'''
	]

	# Roll the dice
	dice_roll = random.randint(1, 6)

	# Show the motion visually
	for _ in range(10):
		dice_label.config(text=random.choice(dice_faces), fg=random.choice(colors))
		root.update()
		time.sleep(0.1)

	# Show the final dice face
	dice_label.config(text=dice_faces[dice_roll - 1], fg='black')

# Create the main application window
root = tk.Tk()
root.title("Dice Roller")
root.configure(bg='lightblue')

# Define some colors
colors = ['red', 'green', 'blue', 'purple', 'orange']

# Create a label to display the dice face
dice_label = tk.Label(root, text='', font=('Courier', 18), justify='left', bg='lightblue')
dice_label.pack(pady=20)

# Create a button to roll the dice
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice, bg='yellow', fg='black', font=('Helvetica', 12, 'bold'))
roll_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()