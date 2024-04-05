import tkinter as tk
from pathlib import Path
from game import make_number, play_game

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"your_path\images")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class GuiApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x818")
        self.root.configure(bg="#3FA49C")

        make_number()

        self.canvas = tk.Canvas(
            root,
            bg="#3FA49C",
            height=818,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.image_bgimage = tk.PhotoImage(file=relative_to_assets("bgimage.png"))
        self.bgimage = self.canvas.create_image(
            652.0,
            458.0,
            image=self.image_bgimage
        )

        self.canvas.create_text(
            227.0,
            219.0,
            anchor="nw",
            text="Make your guess:",
            fill="#000000",
            font=("Rakkas Regular", 50 * -1)
        )

        self.entry_bgimage = tk.PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            863.0,
            256.5,
            image=self.entry_bgimage
        )
        self.entry_1 = tk.Entry(
            bd=0,
            bg="#EAAC45",
            fg="#000716",
            highlightthickness=0,
            font=("Rakkas Regular", 30)
        )
        self.entry_1.place(
            x=712.0,
            y=219.0,
            width=302.0,
            height=73.0
        )

        self.button_bgimage = tk.PhotoImage(file=relative_to_assets("enterinput.png"))
        self.enterinput = tk.Button(
            image=self.button_bgimage,
            borderwidth=0,
            highlightthickness=0,
            command=self.play_game,
            relief="flat"
        )
        self.enterinput.place(
            x=749.0,
            y=348.0,
            width=227.0,
            height=72.0
        )

        self.button_image_2 = tk.PhotoImage(file=relative_to_assets("backhome.png"))
        self.backhome = tk.Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.go_back_home,
            relief="flat"
        )
        self.backhome.place(
            x=287.0,
            y=469.0,
            width=251.0,
            height=80.0
        )

        self.root.resizable(True, True)
        self.root.mainloop()

    def play_game(self):
        user_input = self.entry_1.get()
        play_game(user_input)
        # Clear the entry field after taking the input
        self.entry_1.delete(0, 'end')

    def go_back_home(self):
        # Add any logic you need when going back home
        print("backhome clicked")
        self.root.destroy()  # Close the Tkinter window


if __name__ == '__main__':
    root = tk.Tk()
    app = GuiApp(root)
