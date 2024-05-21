from PIL import Image
# pip install pillow
from pathlib import Path
import tkinter as tk
# pip install tkinter
from tkinter import filedialog, messagebox

base_dir = Path(__file__).parent

def select_images() -> list:
    file_types = [('Images', '*.png;*.jpg;*.jpeg')]
    file_paths = filedialog.askopenfilenames(title="Select images", filetypes=file_types)
    return list(file_paths)

def save_file_path() -> str:
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    return file_path

def convert_to_pdf(imgs_paths, output_path):
    if not imgs_paths:
        return
    try:
        with Image.open(imgs_paths[0]) as img:
            img_1 = img.convert("RGB")
            imgs_to_pdf = [img_1]

            if len(imgs_paths) == 1 and output_path:
                img_1.save(output_path, "PDF")
                messagebox.showinfo("Success", "PDF was created!")
            else:
                for imgs in imgs_paths[1:]:
                    with Image.open(imgs) as other_img:
                        imgs_to_pdf.append(other_img.convert("RGB"))
                if output_path:
                    imgs_to_pdf[0].save(output_path, "PDF", save_all=True, append_images=imgs_to_pdf[1:])
                    messagebox.showinfo("Success", "PDF was created!")
                else:
                    messagebox.showwarning("Canceled", "Saving operation was canceled")
    except Exception as e:
        messagebox.showerror("Error", f"An error as occured: {str(e)}")


def main():
    root = tk.Tk()
    root.title("Convert images to PDF")
    root.geometry("300x200")

    select_button = tk.Button(root, text="Select Images", command=lambda: convert_to_pdf(select_images(), save_file_path()))
    select_button.pack(pady=60)

    root.mainloop()

if __name__ == "__main__":
    main()

    
    



