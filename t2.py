import math
import random
import tkinter as tk
from tkinter import messagebox


# Function to generate OTP
def generateOTP():
    digits = "8287563409"
    OTP = ""

    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


# Function to handle button click event
def generate_and_display_otp():
    otp = generateOTP()
    otp_label.config(text="Generated OTP: " + otp)


# Function to validate entered OTP
def validate_otp():
    entered_otp = otp_entry.get()
    generated_otp = otp_label.cget("text").split(": ")[1]

    if entered_otp == generated_otp:
        messagebox.showinfo("OTP Validation", "OTP is valid!")
    else:
        messagebox.showerror("OTP Validation", "Invalid OTP!")


# Create the main window
root = tk.Tk()
root.title("OTP Generator")
root.geometry("400x300")  # Set the geometry of the window

# Change the background color to lavender
root.configure(bg="lavender")

# Create and place widgets
generate_button = tk.Button(root, text="Generate OTP", command=generate_and_display_otp)
generate_button.pack(pady=15)

otp_label = tk.Label(root, text="Generated OTP: ")
otp_label.pack()

otp_entry_label = tk.Label(root, text="Enter OTP:")
otp_entry_label.pack(pady=10)

otp_entry = tk.Entry(root)
otp_entry.pack(pady=5)

validate_button = tk.Button(root, text="Validate OTP", command=validate_otp)
validate_button.pack(pady=15)

# Start the tkinter event loop
root.mainloop()

