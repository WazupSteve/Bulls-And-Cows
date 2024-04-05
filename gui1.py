from pathlib import Path
import subprocess


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"your_path\images")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def open_gui2():
    # Use subprocess to run the gui2.py script
    subprocess.run(["python", "gui2.py"])
def open_gui3():
    # Use subprocess to run the gui3.py script
    subprocess.run(["python", "gui3.py"])


window = Tk()

window.geometry("1280x832")
window.configure(bg = "#F2DFC9")


canvas = Canvas(
    window,
    bg = "#F2DFC9",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_backimg = PhotoImage(
    file=relative_to_assets("backimg.png"))
backimg = canvas.create_image(
    640.0,
    396.0,
    image=image_backimg
)

button_backimg = PhotoImage(
    
    file=relative_to_assets("start.png"))
start = Button(
    image=button_backimg,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:open_gui3() ,
    relief="flat"
)
start.place(
    x=937.0,
    y=238.0,
    width=181.0,
    height=90.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("rules2.png"))
rules2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui2() ,
    relief="flat"
)
rules2.place(
    x=940.0,
    y=392.0,
    width=184.0,
    height=90.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("quit3.png"))
quit3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=window.quit,  # Use window.quit to close the Tkinter window
    relief="flat"
)
quit3.place(
    x=944.0,
    y=545.0,
    width=181.0,
    height=90.0
)

canvas.create_text(
    257.0,
    25.0,
    anchor="nw",
    text="BULLS & COWS",
    fill="#000000",
    font=("TrainOne Regular", 50 * -1)
)
window.resizable(True,True)
window.mainloop()
