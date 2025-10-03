import os
import tkinter as tk
from tkinter import messagebox

# ================= Playlist Class =================
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def save_to_file(self):
        # check validation
        if self.name == "":
            messagebox.showerror("Error", "Playlist name cannot be empty")
            return
        if len(self.songs) == 0:
            messagebox.showerror("Error", "Playlist must have at least one song")
            return


        # create folder if not exists
        if not os.path.exists("playlists"):
            os.mkdir("playlists")

        filename = "playlists/playlist_" + self.name + ".txt"

        # avoid duplicate playlist
        if os.path.exists(filename):
            messagebox.showerror("Error", "Playlist already exists")
            return


        f = open(filename, "w")
        for song in self.songs:
            f.write(song + "\n")
        f.close()


# ================= GUI Application =================
class MusicBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MusicBox")
        self.root.geometry("500x400")

        # playlist name entry
        tk.Label(root, text="Playlist Name").pack()
        self.txt_name = tk.Entry(root, width=40)
        self.txt_name.pack()

        # song input text
        tk.Label(root, text="Enter Songs (one per line)").pack()
        self.txt_songs = tk.Text(root, height=8, width=40)
        self.txt_songs.pack()

        # buttons
        tk.Button(root, text="Save Playlist", command=self.save_playlist).pack(pady=5)
        tk.Button(root, text="View Playlists", command=self.view_playlists).pack(pady=5)

        # listbox
        self.lst_playlists = tk.Listbox(root, width=40, height=8)
        self.lst_playlists.pack()
        self.lst_playlists.bind("<<ListboxSelect>>", self.show_songs)

        # label for showing songs
        self.lbl_songs = tk.Label(root, text="")
        self.lbl_songs.place(x=50, y=200)

    # save playlist
    def save_playlist(self):
        try:
            name = self.txt_name.get()
            songs = self.txt_songs.get("1.0", tk.END).split("\n")
            songs = [s for s in songs if s.strip() != ""]

            p = Playlist(name, songs)
            p.save_to_file()
            messagebox.showinfo("Success", "Playlist saved successfully")

            self.txt_name.delete(0, tk.END)
            self.txt_songs.delete("1.0", tk.END)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # view playlists
    def view_playlists(self):
        self.lst_playlists.delete(0, tk.END)
        if os.path.exists("playlists"):
            files = os.listdir("playlists")
            for file in files:
                if file.endswith(".txt"):
                    self.lst_playlists.insert(tk.END, file)
        else:
            messagebox.showinfo("Info", "No playlists found")

    # show songs inside playlist
    def show_songs(self, event):
        try:
            selected = self.lst_playlists.get(self.lst_playlists.curselection())
            path = os.path.join("playlists", selected)
            f = open(path, "r")
            data = f.read()
            f.close()
            self.lbl_songs.config(text=data)
        except:
            self.lbl_songs.config(text="Error loading playlist")


# ================= Run Application =================
root = tk.Tk()
app = MusicBoxApp(root)
root.mainloop()
