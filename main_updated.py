import tkinter as tk
from tkinter import messagebox
from zxcvbn import zxcvbn

# ✅ Function to analyze password using zxcvbn
def analyze_password(password):
    result = zxcvbn(password)
    score = result['score']  # score from 0 to 4
    feedback = result['feedback']
    return score, feedback

# ✅ Function to generate wordlist based on name, birth, pet
def generate_wordlist(name, birth, pet):
    base = [name, birth, pet]
    variations = []
    for word in base:
        if word:
            variations.extend([
                word,
                word.lower(),
                word.upper(),
                word.capitalize(),
                word + "123",
                word + "2025",
                word + "@",
                word + "!",
                word.replace("a", "@").replace("s", "$")  # leetspeak
            ])
    return list(set(variations))  # remove duplicates

# ✅ Save the generated wordlist to a file
def save_wordlist(wordlist, filename="wordlist.txt"):
    with open(filename, "w") as f:
        for word in wordlist:
            f.write(word + "\n")

# ✅ Button function: Check strength
def check_strength():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password")
        return
    score, feedback = analyze_password(password)
    result = f"Score: {score}/4\nSuggestions: {'; '.join(feedback['suggestions'])}"
    result_label.config(text=result)

# ✅ Button function: Generate wordlist
def generate_and_save():
    name = name_entry.get()
    birth = birth_entry.get()
    pet = pet_entry.get()
    wordlist = generate_wordlist(name, birth, pet)
    save_wordlist(wordlist)
    messagebox.showinfo("Success", "✅ Wordlist saved as 'wordlist.txt'")

# ✅ GUI setup using tkinter
root = tk.Tk()
root.title("Password Strength Analyzer + Wordlist Generator")
root.geometry("400x400")
root.resizable(False, False)

# Widgets
tk.Label(root, text="🔐 Enter Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*", width=40)
password_entry.pack()

tk.Button(root, text="Check Password Strength", command=check_strength).pack(pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

tk.Label(root, text="👤 Name:").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="📅 Birth Year:").pack(pady=5)
birth_entry = tk.Entry(root, width=40)
birth_entry.pack()

tk.Label(root, text="🐾 Pet Name:").pack(pady=5)
pet_entry = tk.Entry(root, width=40)
pet_entry.pack()

tk.Button(root, text="Generate Wordlist", command=generate_and_save).pack(pady=20)

root.mainloop()
