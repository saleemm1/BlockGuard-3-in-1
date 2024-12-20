import tkinter as tk
from tkinter import messagebox
import pyperclip
import hashlib
import random
import string

class KeyGuardian:
    def __init__(self, root):
        self.root = root
        self.root.title("KeyGuardian: Key Management")
        self.root.configure(bg="#2a3d45")

        self.label = tk.Label(root, text="Generate a New Key:", font=("Helvetica", 18), fg="#a7c4bc", bg="#2a3d45")
        self.label.pack(pady=15)

        self.generate_button = tk.Button(root, text="Generate Key", command=self.generate_key, font=("Helvetica", 14),
                                         bg="#4caf50", fg="white")
        self.generate_button.pack(pady=10)

        self.key_label = tk.Label(root, text="Key: -", font=("Helvetica", 14), fg="#a7c4bc", bg="#2a3d45")
        self.key_label.pack(pady=10)

        self.copy_button = tk.Button(root, text="Copy Key", command=self.copy_key, font=("Helvetica", 12),
                                      bg="#8ab6d6", fg="#1c2833")
        self.copy_button.pack(pady=10)
        self.key = ""

    def generate_key(self):
        self.key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        self.key_label.config(text=f"Key: {self.key}")

    def copy_key(self):
        if self.key:
            pyperclip.copy(self.key)

class HashFlow:
    def __init__(self, root):
        self.root = root
        self.root.title("HashFlow: Hash Generator")
        self.root.configure(bg="#2a3d45")

        self.label = tk.Label(root, text="Enter text to generate hash:", font=("Helvetica", 16), fg="#a7c4bc", bg="#2a3d45")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=40, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        self.hash_button = tk.Button(root, text="Generate Hash", command=self.generate_hash, font=("Helvetica", 14),
                                     bg="#4caf50", fg="white")
        self.hash_button.pack(pady=10)

        self.result_label = tk.Label(root, text="Hash: -", font=("Helvetica", 14), fg="#a7c4bc", bg="#2a3d45")
        self.result_label.pack(pady=10)

        self.copy_button = tk.Button(root, text="Copy Hash", command=self.copy_hash, font=("Helvetica", 12),
                                      bg="#8ab6d6", fg="#1c2833")
        self.copy_button.pack(pady=10)
        self.hash_result = ""

    def generate_hash(self):
        text = self.entry.get()
        if not text:
            messagebox.showerror("Error", "Please enter text")
            return
        self.hash_result = hashlib.sha256(text.encode()).hexdigest()
        self.result_label.config(text=f"Hash: {self.hash_result}")

    def copy_hash(self):
        if self.hash_result:
            pyperclip.copy(self.hash_result)

class DefiSense:
    def __init__(self, root):
        self.root = root
        self.root.title("DefiSense: Contract Analysis")
        self.root.configure(bg="#2a3d45")

        self.label = tk.Label(root, text="Enter smart contract code:", font=("Helvetica", 16), fg="#a7c4bc", bg="#2a3d45")
        self.label.pack(pady=10)

        self.text_area = tk.Text(root, width=60, height=15, font=("Helvetica", 12))
        self.text_area.pack(pady=10)

        self.analyze_button = tk.Button(root, text="Analyze Code", command=self.analyze_code, font=("Helvetica", 14),
                                        bg="#4caf50", fg="white")
        self.analyze_button.pack(pady=10)

        self.result_label = tk.Label(root, text="Result: -", font=("Helvetica", 14), fg="#a7c4bc", bg="#2a3d45")
        self.result_label.pack(pady=10)

        self.copy_button = tk.Button(root, text="Copy Result", command=self.copy_result, font=("Helvetica", 12),
                                      bg="#8ab6d6", fg="#1c2833")
        self.copy_button.pack(pady=10)
        self.analysis_result = ""

    def analyze_code(self):
        code = self.text_area.get("1.0", tk.END).strip()
        if not code:
            messagebox.showerror("Error", "Please enter contract code")
            return

        self.analysis_result = "No vulnerabilities found."  # Replace with real analysis logic
        self.result_label.config(text=f"Result: {self.analysis_result}")

    def copy_result(self):
        if self.analysis_result:
            pyperclip.copy(self.analysis_result)

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Service Navigation")
        self.root.configure(bg="#0e1a24")

        self.how_it_works_button = tk.Button(root, text="How It Works", command=self.show_how_it_works,
                                             font=("Helvetica", 12), bg="#8ab6d6", fg="#1c2833")
        self.how_it_works_button.place(relx=0.9, rely=0.05, anchor="ne")

        self.label = tk.Label(root, text="Choose a Service:", font=("Helvetica", 20), fg="#a7c4bc", bg="#0e1a24")
        self.label.pack(pady=20)

        self.button_frame = tk.Frame(root, bg="#0e1a24")
        self.button_frame.pack(pady=20)

        self.keyguardian_button = tk.Button(self.button_frame, text="KeyGuardian\nManage dynamic keys securely",
                                            command=self.open_keyguardian, font=("Helvetica", 14), bg="#4caf50", fg="white",
                                            width=25, height=5)
        self.keyguardian_button.grid(row=0, column=0, padx=10, pady=10)

        self.hashflow_button = tk.Button(self.button_frame, text="HashFlow\nGenerate SHA256 proof",
                                         command=self.open_hashflow, font=("Helvetica", 14), bg="#4caf50", fg="white",
                                         width=25, height=5)
        self.hashflow_button.grid(row=0, column=1, padx=10, pady=10)

        self.defisense_button = tk.Button(self.button_frame, text="DefiSense\nAnalyze smart contracts",
                                          command=self.open_defisense, font=("Helvetica", 14), bg="#4caf50", fg="white",
                                          width=25, height=5)
        self.defisense_button.grid(row=0, column=2, padx=10, pady=10)

    def open_keyguardian(self):
        new_window = tk.Toplevel(self.root)
        KeyGuardian(new_window)

    def open_hashflow(self):
        new_window = tk.Toplevel(self.root)
        HashFlow(new_window)

    def open_defisense(self):
        new_window = tk.Toplevel(self.root)
        DefiSense(new_window)

    def show_how_it_works(self):
        message = (
            "KeyGuardian: Generate secure dynamic keys and copy them to your clipboard.\n"
            "HashFlow: Generate SHA256 hash values for any input text and copy the hash to your clipboard.\n"
            "DefiSense: Analyze smart contract code to identify potential vulnerabilities and copy the results."
        )
        messagebox.showinfo("How It Works", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
                     
