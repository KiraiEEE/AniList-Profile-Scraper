import requests
from bs4 import BeautifulSoup
from io import BytesIO
import tkinter as tk
from PIL import ImageTk, Image

def scrape_profile(username):
    url = f"https://anilist.co/user/{username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    name = soup.find('h1', {'class': 'name'})
    if not name:
        raise ValueError(f"Profile not found for user '{username}'")
    name = name.text.strip()

    img = soup.find('img', {'class': 'avatar'})['src']
    response_img = requests.get(img)
    img = Image.open(BytesIO(response_img.content))

    return name, img

def on_button_click():
    username = entry.get()
    try:
        name, img = scrape_profile(username)
        photo = ImageTk.PhotoImage(img)

        name_label.config(text=name)
        name_label.pack()

        img_label.config(image=photo)
        img_label.image = photo
        img_label.pack()

    except ValueError as e:
        result_label.config(text=str(e))
        result_label.pack()

root = tk.Tk()
root.configure(bg='#331832')

root.geometry("400x400")
root.title("AniList.co プロファイル スクレーパー")

title_label = tk.Label(root, text="AniList.co プロファイル スクレーパー", font=("Yu Gothic UI Light", 20), fg="#D9B3E6", bg='#331832')
title_label.pack(pady=10)

input_label = tk.Label(root, text="ユーザー名 : ", font=("Yu Gothic UI Light", 12), fg="#D9B3E6", bg='#331832')
input_label.pack()

entry = tk.Entry(root, font=("Yu Gothic UI Light", 12), bg='#331832', fg='#D9B3E6')
entry.pack(pady=5)

button = tk.Button(root, text="行け！>>", font=("Yu Gothic UI Bold", 12), bg='#9556a3', fg='#111111', command=on_button_click)
button.pack(pady=10)

name_label = tk.Label(root, font=("Yu Gothic UI Light", 16), fg="#D9B3E6", bg='#331832')
img_label = tk.Label(root, bg='#331832')

result_label = tk.Label(root, font=("Yu Gothic UI Light", 12), fg="#D9B3E6", bg='#331832')

root.mainloop()
