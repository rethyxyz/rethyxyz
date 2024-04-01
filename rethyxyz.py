import tkinter as tk
from time import sleep

class IntroAnimation:
    def __init__(self, master, project_name):
        self.master = master
        self.master.overrideredirect(True)  # This removes the title bar
        self.window_width = 400
        self.window_height = 200
        self.border_size = 1  # Size of the border
        
        # Calculate position x, y to center the window
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width - self.window_width - 2*self.border_size) / 2)
        y = int((screen_height - self.window_height - 2*self.border_size) / 2)
        
        self.master.geometry(f"{self.window_width + 2*self.border_size}x{self.window_height + 2*self.border_size}+{x}+{y}")
        self.master.configure(background='lightgrey')  # Background color of the master, acts as the border color

        # Creating a frame that will contain the canvas, this acts as the main content area
        self.content_frame = tk.Frame(self.master, background='black')
        self.content_frame.pack(padx=self.border_size, pady=self.border_size)  # Padding acts as the border width

        self.canvas = tk.Canvas(self.content_frame, width=self.window_width, height=self.window_height, bg='black', highlightthickness=0)
        self.canvas.pack()

        # Starting font size and style for the animated text
        self.font_size = 20
        self.font_style = "Helvetica 20"
        self.text = self.canvas.create_text(200, 100, text="rethy.xyz", font=self.font_style, fill="white")

        # Project name text
        self.project_text = self.canvas.create_text(200, 160, text=project_name, font="Helvetica 12", fill="white")

        # Static copyright date text
        self.copy_text = self.canvas.create_text(200, 180, text="2018-2024 © Brody Rethy", font="Helvetica 10", fill="white")

    def run_animation(self):
        for _ in range(10):  # Fewer iterations for a concise demo
            self.font_style = "Helvetica " + str(self.font_size) + (" italic" if _ % 2 == 0 else "")
            self.canvas.itemconfig(self.text, font=self.font_style)
            
            self.font_size += 2
            self.canvas.itemconfig(self.text, font=self.font_style)

            self.master.update()
            sleep(0.2)
        
        self.master.destroy()

def show_intro(project_name):
    root = tk.Tk()
    intro = IntroAnimation(root, project_name)
    root.after(0, intro.run_animation)
    root.mainloop()

if __name__ == "__main__":
    # Example project name passed as argument
    show_intro("Project Name Here")

