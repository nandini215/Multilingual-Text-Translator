#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install googletrans==4.0.0-rc1


# In[2]:


pip install pytesseract googletrans==4.0.0-rc1 Pillow PyMuPDF


# In[3]:


pip install deep-translator


# In[4]:


def translate_text(language):
    try:
        src_text = source_text.get("1.0", tk.END).strip()[:1000]  # Limiting text length for testing
        
        if not src_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        translated = GoogleTranslator(source='auto', target=language).translate(src_text)
        dest_text.delete("1.0", tk.END)
        dest_text.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))


# In[5]:


def translate_text(language):
    try:
        src_text = source_text.get("1.0", tk.END).strip()[:1000]  # Limiting text length for testing
        
        if not src_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        print(f"Translating text: {src_text}")  # Debug log
        translated = GoogleTranslator(source='auto', target=language).translate(src_text)
        print(f"Translated text: {translated}")  # Debug log
        
        dest_text.delete("1.0", tk.END)
        dest_text.insert(tk.END, translated)
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug log
        messagebox.showerror("Translation Error", str(e))


# In[6]:


def translate_text(language):
    try:
        src_text = source_text.get("1.0", tk.END).strip()
        
        if not src_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        # Split text into chunks of 1000 characters
        chunk_size = 1000
        chunks = [src_text[i:i+chunk_size] for i in range(0, len(src_text), chunk_size)]
        
        translated_text = ""
        for chunk in chunks:
            print(f"Translating chunk: {chunk}")  # Debug log
            translated_chunk = GoogleTranslator(source='auto', target=language).translate(chunk)
            print(f"Translated chunk: {translated_chunk}")  # Debug log
            translated_text += translated_chunk + " "
        
        dest_text.delete("1.0", tk.END)
        dest_text.insert(tk.END, translated_text)
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug log
        messagebox.showerror("Translation Error", str(e))


# In[7]:


import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import pytesseract
import fitz  # PyMuPDF
from deep_translator import GoogleTranslator

# Ensure you have the Tesseract executable path correctly set
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if needed

# Function to perform translation
def translate_text(language):
    try:
        src_text = source_text.get("1.0", tk.END).strip()
        
        if not src_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        # Split text into chunks of 1000 characters
        chunk_size = 1000
        chunks = [src_text[i:i+chunk_size] for i in range(0, len(src_text), chunk_size)]
        
        translated_text = ""
        for chunk in chunks:
            translated_chunk = GoogleTranslator(source='auto', target=language).translate(chunk)
            translated_text += translated_chunk + " "
        
        dest_text.delete("1.0", tk.END)
        dest_text.insert(tk.END, translated_text.strip())
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Function to load image and extract text
def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        try:
            image = Image.open(file_path)
            extracted_text = pytesseract.image_to_string(image)
            source_text.delete("1.0", tk.END)
            source_text.insert(tk.END, extracted_text)
        except Exception as e:
            messagebox.showerror("Image Error", str(e))

# Function to load PDF and extract text
def load_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        try:
            doc = fitz.open(file_path)
            pdf_text = ""
            for page in doc:
                pdf_text += page.get_text()
            if not pdf_text.strip():
                raise ValueError("No text found in the PDF file")
            source_text.delete("1.0", tk.END)
            source_text.insert(tk.END, pdf_text)
        except Exception as e:
            messagebox.showerror("PDF Error", str(e))

# Initialize the main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("800x700")
root.configure(bg="#f0f4f7")

# Custom font and style
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 14, 'bold'), background='#f0f4f7')
style.configure('TButton', font=('Helvetica', 12, 'bold'), padding=10)
style.configure('TFrame', background='#f0f4f7')

# Frame for source text and buttons
source_frame = ttk.Frame(root, style='TFrame')
source_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Source Text Label and Text Box
source_lbl = ttk.Label(source_frame, text="Source Text", style='TLabel')
source_lbl.pack(pady=5)
source_text = tk.Text(source_frame, height=10, width=70, font=('Helvetica', 12), wrap=tk.WORD, borderwidth=2, relief="solid", bg='#ffffff', fg='#333333')
source_text.pack(pady=5)

# Frame for buttons
button_frame = ttk.Frame(source_frame, style='TFrame')
button_frame.pack(pady=5)

load_image_btn = ttk.Button(button_frame, text="Load Image", command=load_image, style='TButton', cursor="hand2", width=15)
load_image_btn.pack(side=tk.LEFT, padx=5)

load_pdf_btn = ttk.Button(button_frame, text="Load PDF", command=load_pdf, style='TButton', cursor="hand2", width=15)
load_pdf_btn.pack(side=tk.LEFT, padx=5)

# Frame for translation buttons
translate_button_frame = ttk.Frame(source_frame, style='TFrame')
translate_button_frame.pack(pady=10)

translate_hindi_btn = ttk.Button(translate_button_frame, text="Translate to Hindi", command=lambda: translate_text('hi'), style='TButton', cursor="hand2", width=20)
translate_hindi_btn.pack(side=tk.LEFT, padx=5)

translate_kannada_btn = ttk.Button(translate_button_frame, text="Translate to Kannada", command=lambda: translate_text('kn'), style='TButton', cursor="hand2", width=20)
translate_kannada_btn.pack(side=tk.LEFT, padx=5)

# Frame for translated text
dest_frame = ttk.Frame(root, style='TFrame')
dest_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Destination Text Label and Text Box
dest_lbl = ttk.Label(dest_frame, text="Translated Text", style='TLabel')
dest_lbl.pack(pady=5)
dest_text = tk.Text(dest_frame, height=10, width=70, font=('Helvetica', 12), wrap=tk.WORD, borderwidth=2, relief="solid", bg='#ffffff', fg='#333333')
dest_text.pack(pady=5)

# Run the main event loop
root.mainloop() 


# In[ ]:




