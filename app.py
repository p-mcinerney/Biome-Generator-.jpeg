from PIL import Image
import random

colors_library = {"black": (0, 0, 0), "white": (255, 255, 255), "red": (255, 0, 0), "blue": (0, 0, 255), "green": (0, 255, 0)}
colors = ["black", "white", "red", "blue", "green"]


def new_pixel(last):
    last_weights = {"black": [10, 5, 3, 2, 1], "white": [5, 10, 3, 2, 1], "red": [5, 5, 5, 2, 1], "blue": [5, 5, 3, 3, 1], "green": [5, 5, 5, 5, 3]}
    color = random.choices(colors, weights=last_weights[last], k=1)[0]
    return color

def new_file_id():
    # check if the id is already in use
    # make new id
    with open("id.txt", "r") as file:
        last_id = int(file.readline())
        new_id = last_id + 1
        
    with open("id.txt", "w") as file:
        file.write(str(new_id))

    return new_id
        
            

                


width, height = 100, 100
image = Image.new("RGB", (100, 100), "white")

last_pixel = random.choice(colors)
totals = {"black": 0, "white": 0, "red": 0, "blue": 0, "green": 0}
totals[last_pixel] += 1

for x in range(width):
    for y in range(height):
        new_color = new_pixel(last_pixel)
        totals[new_color] += 1
        pixel = colors_library[new_color]
        image.putpixel((x, y), pixel)
        last_pixel = new_color



image.save(f"images/{new_file_id()}.jpeg", "JPEG")
print(f"<----------Totals---------->\nBlack ===== {totals["black"]}\nWhite ===== {totals["white"]}\nRed ===== {totals["red"]}\nBlue ===== {totals["blue"]}\nGreen ===== {totals["green"]}")