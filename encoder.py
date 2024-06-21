import tkinter as tk
import pyperclip

root = tk.Tk()
root.title("Text Encoder/Decoder")

action_var = tk.StringVar(value="Encode")  # Set default action

action_frame = tk.Frame(root)
action_frame.pack()

encode_radio = tk.Radiobutton(action_frame, text="Encode", variable=action_var, value="Encode")
encode_radio.pack(side=tk.LEFT)
decode_radio = tk.Radiobutton(action_frame, text="Decode", variable=action_var, value="Decode")
decode_radio.pack(side=tk.LEFT)

key_label = tk.Label(root, text="Key (4 digits):")
key_label.pack()
key_entry = tk.Entry(root)
key_entry.pack()

text_label = tk.Label(root, text="Text:")
text_label.pack()
text_entry = tk.Text(root, height=5)
text_entry.pack()

result_label = tk.Label(root, text="")
result_label.pack()

encode_button = tk.Button(root, text="Process", command=lambda: handle_action())
encode_button.pack()

def handle_action():
    action = action_var.get()
    key = key_entry.get()
    text = text_entry.get("1.0", "end-1c")  # Get entire text from text box

    try:
        processed_text = "Text copied to clipboard! \n"
        if action == "Encode":
            for char in text:
                offset = (ord(char) + sum(int(digit) for digit in key)) % 256
                processed_text += chr(offset)
        elif action == "Decode":
            for char in text:
                offset = (ord(char) - sum(int(digit) for digit in key)) % 256
                processed_text += chr(offset)
        else:
            raise ValueError("Invalid action")
    except ValueError as e:
        result_label.config(text=str(e))
    else:
        result_label.config(text=f"{action.capitalize()}d text:\n{processed_text}")
        pyperclip.copy(processed_text)  # Copy the processed text to clipboard

root.mainloop()
