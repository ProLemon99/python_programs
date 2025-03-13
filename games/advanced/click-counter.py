import tkinter as tk
import time

class ClickCounterApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.clicks = 0
        self.start_time = None
        self.best_cps = 0
        self.current_cps = 0
        self.last_click_time = None  # Tracks the last time the user clicked
        self.create_widgets()
        self.update_cps_display()  # Start CPS decay process

    def create_widgets(self):
        # Make the window responsive
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Button
        self.button = tk.Button(
            self, text="Click Me!", font=("Arial", 16), width=15, height=2, command=self.update_count
        )
        self.button.grid(row=0, column=0, pady=10, padx=10)

        # Click count label
        self.click_label = tk.Label(self, text="Total Clicks: 0", font=("Arial", 14))
        self.click_label.grid(row=1, column=0, pady=5)

        # CPS Label
        self.cps_label = tk.Label(self, text="Clicks Per Second: 0.00", font=("Arial", 12))
        self.cps_label.grid(row=2, column=0, pady=5)

        # Best CPS Label
        self.best_cps_label = tk.Label(self, text="Best CPS: 0.00", font=("Arial", 12))
        self.best_cps_label.grid(row=3, column=0, pady=5)

        # Reset Button
        self.reset_button = tk.Button(self, text="Reset", font=("Arial", 12), command=self.reset_counter)
        self.reset_button.grid(row=4, column=0, pady=10)

    def update_count(self):
        self.clicks += 1
        current_time = time.time()

        if self.start_time is None:
            self.start_time = current_time  # Start time on first click

        self.last_click_time = current_time  # Update last click timestamp

        elapsed_time = current_time - self.start_time
        self.current_cps = self.clicks / elapsed_time if elapsed_time > 0 else 0

        # Update best CPS if current is higher
        if self.current_cps > self.best_cps:
            self.best_cps = self.current_cps

        # Update UI
        self.click_label.config(text=f"Total Clicks: {self.clicks}")
        self.cps_label.config(text=f"Clicks Per Second: {self.current_cps:.2f}")
        self.best_cps_label.config(text=f"Best CPS: {self.best_cps:.2f}")

    def update_cps_display(self):
        """Gradually decreases CPS if the player stops clicking."""
        if self.last_click_time:
            time_since_last_click = time.time() - self.last_click_time

            # If the user hasn't clicked for 1 second, start decreasing CPS
            if time_since_last_click > 1:
                self.current_cps *= 0.9  # Reduce CPS by 10% every frame
                if self.current_cps < 0.1:  # If CPS gets really low, reset it to 0
                    self.current_cps = 0

        self.cps_label.config(text=f"Clicks Per Second: {self.current_cps:.2f}")

        # Call this function every 100ms to update the CPS display
        self.after(100, self.update_cps_display)

    def reset_counter(self):
        self.clicks = 0
        self.start_time = None
        self.best_cps = 0
        self.current_cps = 0
        self.last_click_time = None

        self.click_label.config(text="Total Clicks: 0")
        self.cps_label.config(text="Clicks Per Second: 0.00")
        self.best_cps_label.config(text="Best CPS: 0.00")

# Initialize Tkinter
root = tk.Tk()
root.title("Click Counter")
root.geometry("400x300")  # Adjusted size for better layout

# Center the frame
app = ClickCounterApp(root)
app.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()