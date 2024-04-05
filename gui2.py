from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"your_path\images")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1396x890")
window.configure(bg="#000003")

canvas = Canvas(
    window,
    bg="#000003",
    height=890,
    width=1396,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_bgimg = PhotoImage(
    file=relative_to_assets("bgimg.png"))
bgimg = canvas.create_image(
    698.0,
    458.0,
    image=image_bgimg
)

canvas.create_rectangle(
    14.0,
    109.0,
    1346.0,
    522.0,
    fill="#3878F0",
    outline="")

canvas.create_rectangle(
    306.0,
    541.0,
    1154.0,
    632.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    365.0,
    530.0,
    anchor="nw",
    text="\nBest of luck in mastering this code-breaking adventure!",
    fill="#8B141B",
    font=("RalewayRoman Regular", 30 * -1)
)

button_bgimg = PhotoImage(
    file=relative_to_assets("backhome1.png"))
backhome = Button(
    image=button_bgimg,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,  # Close the Tkinter window
    relief="flat"
)
backhome.place(
    x=537.0,
    y=662.0,
    width=270.0,
    height=80.0
)

canvas.create_text(
    78.0,
    108.0,
    anchor="nw",
    text="\n \nIndulge in this sophisticated blend of intellect and strategy - The Bulls and Cows Game of discovering\n the mystery 4-digit number! \n\nCraft precise 4-digit guesses sans repetition and aim to score 4 bulls.\nBulls denote correct digits in precise positions\nCows denote correct digits in alternate places. \nIn the journey of unveiling the discreet 4-digit number, remember to give it not more than 10 attempts ,\n surpassing which the elusive number is revealed and the show ends. \n",
    fill="#FFFFFF",
    font=("Rakkas Regular", 28*-1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("rules.png"))
rules = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("rules clicked"),
    relief="flat"
)
rules.place(
    x=575.0,
    y=31.438232421875,
    width=190.0,
    height=57.561767578125
)
window.resizable(True, True)
window.mainloop()
