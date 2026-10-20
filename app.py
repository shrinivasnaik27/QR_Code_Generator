
import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk


class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("500x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f8")

        self.qr_image = None
        self.preview_image = None

        tk.Label(
            root,
            text="QR Code Generator",
            font=("Arial", 23, "bold"),
            bg="#f0f4f8",
            fg="#17365d"
        ).pack(pady=(25, 8))

        tk.Label(
            root,
            text="Convert text or a URL into a QR code",
            font=("Arial", 11),
            bg="#f0f4f8",
            fg="#555555"
        ).pack(pady=(0, 20))

        tk.Label(
            root,
            text="Enter text or URL:",
            font=("Arial", 12, "bold"),
            bg="#f0f4f8"
        ).pack(anchor="w", padx=40)

        self.entry = tk.Entry(
            root,
            font=("Arial", 12),
            width=42,
            relief="solid",
            bd=1
        )
        self.entry.pack(padx=40, pady=10, ipady=8)

        self.generate_button = tk.Button(
            root,
            text="Generate QR Code",
            command=self.generate_qr,
            font=("Arial", 12, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=10
        )
        self.generate_button.pack(pady=10)

        self.preview_label = tk.Label(
            root,
            text="Your QR code will appear here",
            font=("Arial", 11),
            bg="#ffffff",
            fg="#777777",
            width=30,
            height=10
        )
        self.preview_label.pack(pady=15)

        self.save_button = tk.Button(
            root,
            text="Save QR Code as PNG",
            command=self.save_qr,
            font=("Arial", 11, "bold"),
            bg="#16a34a",
            fg="white",
            activebackground="#15803d",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=9,
            state="disabled"
        )
        self.save_button.pack(pady=5)

        tk.Label(
            root,
            text="Created with Python and Tkinter",
            font=("Arial", 9),
            bg="#f0f4f8",
            fg="#777777"
        ).pack(side="bottom", pady=15)

        self.root.bind("<Return>", lambda event: self.generate_qr())

    def generate_qr(self):
        data = self.entry.get().strip()

        if not data:
            messagebox.showwarning(
                "Input Required",
                "Please enter some text or a URL."
            )
            return

        try:
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4
            )

            qr.add_data(data)
            qr.make(fit=True)

            self.qr_image = qr.make_image(
                fill_color="black",
                back_color="white"
            ).convert("RGB")

            preview = self.qr_image.copy()
            preview.thumbnail((230, 230))

            self.preview_image = ImageTk.PhotoImage(preview)
            self.preview_label.configure(
                image=self.preview_image,
                text="",
                width=230,
                height=230
            )

            self.save_button.configure(state="normal")

        except Exception as error:
            messagebox.showerror(
                "Generation Error",
                f"Could not generate QR code:\n{error}"
            )

    def save_qr(self):
        if self.qr_image is None:
            messagebox.showwarning(
                "No QR Code",
                "Generate a QR code first."
            )
            return

        file_path = filedialog.asksaveasfilename(
            title="Save QR Code",
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")],
            initialfile="my_qr_code.png"
        )

        if file_path:
            try:
                self.qr_image.save(file_path, format="PNG")
                messagebox.showinfo(
                    "Success",
                    f"QR code saved successfully!\n{file_path}"
                )
            except Exception as error:
                messagebox.showerror(
                    "Save Error",
                    f"Could not save the image:\n{error}"
                )


if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()
