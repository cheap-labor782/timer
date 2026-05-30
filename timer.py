import tkinter as tk

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pro Stopwatch")
        self.root.geometry("320x500")
        self.root.configure(bg='black')  # 設定視窗背景為黑色

        # 若要顯示碼表小圖示，請準備一個 stopwatch.ico 檔案放在同目錄
        # try:
        #     self.root.iconbitmap("stopwatch.ico")
        # except:
        #     pass

        self.running = False
        self.elapsed_time = 0

        # 設定字型與顏色
        style = {"bg": "black", "fg": "white", "font": ("Consolas", 40)}
        
        self.label = tk.Label(root, text="00:00:00", **style)
        self.label.pack(pady=30)

        # 按鈕美化
        btn_style = {"bg": "#333333", "fg": "white", "activebackground": "#555555", "width": 8}
        self.btn_frame = tk.Frame(root, bg="black")
        self.btn_frame.pack()

        tk.Button(self.btn_frame, text="Start", command=self.start, **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="Pause", command=self.pause, **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="Reset", command=self.reset, **btn_style).pack(side=tk.LEFT, padx=5)
        
        tk.Button(root, text="Record (M)", command=self.record, bg="#0066cc", fg="white", width=25, height=2).pack(pady=20)

        self.listbox = tk.Listbox(root, bg="#1a1a1a", fg="white", borderwidth=0, highlightthickness=0, width=40)
        self.listbox.pack(pady=10)

        # 鍵盤綁定
        self.root.bind('<s>', lambda e: self.start())
        self.root.bind('<p>', lambda e: self.pause())
        self.root.bind('<r>', lambda e: self.reset())
        self.root.bind('<m>', lambda e: self.record())

        self.update_timer()

    def format_time(self, ms):
        s, m, h = (ms // 1000) % 60, (ms // (1000 * 60)) % 60, (ms // (1000 * 60 * 60))
        return f"{h:02d}:{m:02d}:{s:02d}"

    def update_timer(self):
        if self.running:
            self.elapsed_time += 100
            self.label.config(text=self.format_time(self.elapsed_time))
        self.root.after(100, self.update_timer)

    def start(self): self.running = True
    def pause(self): self.running = False
    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.label.config(text="00:00:00")
        self.listbox.delete(0, tk.END)

    def record(self):
        if self.running:
            self.listbox.insert(0, f"Lap: {self.format_time(self.elapsed_time)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
    