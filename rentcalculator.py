import tkinter as tk
from tkinter import ttk, messagebox

RUPEE = "₹"

class RentDistributionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rent Distribution Calculator")
        self.root.geometry("420x420")
        self.root.configure(bg="#eef2f7")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.build_ui()

    # ---------- UI ----------
    def build_ui(self):
        card = tk.Frame(self.root, bg="white")
        card.place(relx=0.5, rely=0.5, anchor="center", width=360, height=360)

        ttk.Label(
            card,
            text="🏠 Rent Distribution",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=15)

        self.rent = self.create_field(card, "Total Monthly Rent (₹)")
        self.utilities = self.create_field(card, "Utilities Cost (₹)")
        self.people = self.create_field(card, "Number of People")

        ttk.Button(
            card,
            text="Distribute Rent",
            command=self.calculate
        ).pack(pady=15)

        self.result = ttk.Label(
            card,
            text="",
            font=("Segoe UI", 13, "bold"),
            foreground="#0f766e"
        )
        self.result.pack(pady=10)

    def create_field(self, parent, label):
        frame = tk.Frame(parent, bg="white")
        frame.pack(pady=6, padx=25, fill="x")

        ttk.Label(frame, text=label).pack(anchor="w")
        entry = ttk.Entry(frame)
        entry.pack(fill="x")
        return entry

    # ---------- Logic ----------
    def calculate(self):
        try:
            rent = float(self.rent.get())
            utilities = float(self.utilities.get())
            people = int(self.people.get())

            if people <= 0:
                raise ValueError

            total = rent + utilities
            per_person = total / people

            self.result.config(
                text=(
                    f"📌 Total Cost: {RUPEE}{total:,.2f}\n"
                    f"👤 Rent Per Person: {RUPEE}{per_person:,.2f}"
                )
            )

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter valid values.\nNumber of people must be greater than zero."
            )

# ---------- Run ----------
if __name__ == "__main__":
    root = tk.Tk()
    RentDistributionApp(root)
    root.mainloop()
