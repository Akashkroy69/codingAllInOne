import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import requests
from io import BytesIO

def generate_image():
    user_input = entry.get()

    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a description!")
        return
    
   
    apt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjFjYWEwYzUzMTJhOGEyNWE4MmU1ZTM5MmVmYWQ3ZmNiIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDQtMjRUMTI6MjE6MjUuMzQwNzY3In0.LJUYwE91CONnKQQoeqKdP4xCIm5qmR1X1BJhKFNYGtU"
    
    url = "https://api.monsterapi.ai/v1/generate/txt2img"
    headers = {"Authorization": f"Bearer {apt_token}"}

    response = requests.post(url, json={"prompt": user_input, "safe_filter": True}, headers=headers)

    if response.status_code == 200:
        process_id = response.json().get("process_id")
        status_data = None
        
        while True:
            status_data = requests.get(f"https://api.monsterapi.ai/v1/status/{process_id}", headers=headers).json()
            status = status_data.get("status")
            
            if status == "COMPLETED":
                image_url = status_data['result']['output'][0]
                img_data = requests.get(image_url).content
                img = Image.open(BytesIO(img_data))

                img_tk = ImageTk.PhotoImage(img)
                label_img.config(image=img_tk)
                label_img.image = img_tk
                global generated_image
                generated_image = img
                break
            elif status == "FAILED":
                messagebox.showerror("Error", "Image generation failed.")
                break
    else:
        messagebox.showerror("Error", f"Failed to contact the API. Status code: {response.status_code}")

def save_image():
    if 'generated_image' in globals():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg;*.jpeg"), ("All Files", "*.*")])
        
        if file_path:
            generated_image.save(file_path)
            messagebox.showinfo("Success", f"Image saved at {file_path}")
    else:
        messagebox.showwarning("No Image", "No image to save. Please generate an image first.")

# Setting up Tkinter GUI
root = tk.Tk()
root.title("AI Image Generator")

root.geometry("1000x800")
root.configure(bg="black")

# Create a label for the input
label = tk.Label(root, text="Enter a description for the image:")
label.pack(pady=10)

# Create an entry widget to input the description
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create a button to trigger the image generation
button_generate = tk.Button(root, text="Generate Image", command=generate_image)
button_generate.pack(pady=20)

# Create a button to save the generated image
button_save = tk.Button(root, text="Save Image", command=save_image)
button_save.pack(pady=10)

# Label to display the generated image
label_img = tk.Label(root)
label_img.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
