# Print out a double half pyramid of a specified height

# Modules
from cs50 import get_int

# Global variables
height = -1

# Get a valid height from user in range [1-8]
while True:
	height = get_int("Height: ")
	if height > 0 and height < 9:
		break;

i = 0
while i < height:

	# Print first half of pyramid
	j = 0
	while j < height:
		if j >= height - i - 1:
			print("#", end="")
		else:
			print(" ", end="")
		j += 1

	# Print second half of pyramid
	print("    ", end="")
	j = 0
	while j < height:
		if j <= i:
			print("#", end="")
		else:
			print(" ", end="")
		j += 1

	print()
	i += 1

