import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk


def generate_qrcode():
    url = entry_url.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Make and save qr code
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save("qrcode.png")

    # Display qr code
    qr_image_tk = ImageTk.PhotoImage(Image.open("qrcode.png"))
    qr_label.config(image=qr_image_tk)
    qr_label.image = qr_image_tk
    messagebox.showinfo("Success", "QR code generated successfully!")


# Create main window
root = tk.Tk()
root.title("Qr code generator")
root.geometry("400x500")
root.configure(bg="#f0f4f7")

# Url input
label_url = ttk.Label(root, text="Enter URL: ", background="#f0f4f7")
label_url.pack(pady=10)
entry_url = ttk.Entry(root, font=("Helvetica", 12), width=40)
entry_url.pack(pady=10)

# Generate Button
button_generate = ttk.Button(
    root, text="Generate QR code", command=generate_qrcode, style="TButton")
button_generate.pack(pady=20)

# Label to display QRcode
qr_label = ttk.Label(root, background="#f0f4f7")
qr_label.pack(pady=10)

# Result label
label_result = ttk.Label(root, text="", font=(
    "Helvetica", 14), background="#f0f4f7", foreground="#333")
label_result.pack(pady=20)

# Styling
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=5)
style.map("TButton",
          background=[("active", "#0056b3"), ("!active", "#007bff")],
          foreground=[("active", "white"), ("!active", "white")])

root.mainloop()
