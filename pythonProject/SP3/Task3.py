import tkinter as tk
import converters

def display_resize():
    window = tk.Tk()

    window.title('Video Converter')
    width = 200
    height = 200
    window.geometry(f"{width}x{height}")
    C = 2
    for i in range(C):
        window.columnconfigure(i, weight=width // C)
    R = 2
    for i in range(R):
        window.rowconfigure(i, weight=height // R)

    # resize to 160
    button160 = tk.Button(
        window,
        text=f"160",
        bg="white",
        fg="black",
        command=lambda: converters.SP3.resize("BBB", "BBB_160", 160, 120),
    )
    button160.grid(row=0, column=0)

    # resize to 360
    button360 = tk.Button(
        window,
        text=f"360",
        bg="white",
        fg="black",
        command=lambda: converters.SP3.resize("BBB", "BBB_360", 360, 240),
    )
    button360.grid(row=0, column=1)

    # resize to 480
    button480 = tk.Button(
        window,
        text=f"480",
        bg="white",
        fg="black",
        command=lambda: converters.SP3.resize("BBB", "BBB_480", 640, 480),
    )
    button480.grid(row=1, column=0)

    # resize to 720
    button720 = tk.Button(
        window,
        text=f"720",
        bg="white",
        fg="black",
        command=lambda: converters.SP3.resize("BBB", "BBB_720", 1280, 720),
    )
    button720.grid(row=1, column=1)

    window.mainloop()

def display_coverter():
    window = tk.Tk()

    window.title('Video Converter')
    width = 200
    height = 200
    window.geometry(f"{width}x{height}")
    C = 2
    for i in range(C):
        window.columnconfigure(i, weight=width // C)
    R = 2
    for i in range(R):
        window.rowconfigure(i, weight=height // R)

    # convert to vp8
    vp8_button = tk.Button(
        window,
        text=f"vp8",
        bg="white",
        fg="black",
        command=lambda: converters.SP3.convert("BBB","vp8"),
    )
    vp8_button.grid(row=0, column=0)

    # convert to vp9
    vp9_button = tk.Button(
        window,
        text=f"vp9",
        bg="white",
        fg="black",
        command=lambda: converters.SP3.convert("BBB","vp9"),
    )
    vp9_button.grid(row=0, column=1)

    # convert to h265
    h265_button = tk.Button(
        window,
        text=f"h265",
        bg="white",
        fg="black",
        command=lambda: converters.SP3.convert("BBB","h265"),
    )
    h265_button.grid(row=1, column=0)

    # convert to av1
    av1_button = tk.Button(
        window,
        text=f"av1",
        bg="white",
        fg="black",
        command=lambda: converters.SP3.convert("BBB","av1"),
    )
    av1_button.grid(row=1, column=1)

    window.mainloop()

if __name__ == "__main__":
    main_window = tk.Tk()
    main_window.title('SP3')
    main_window.geometry(f"400x300")

    lbl = tk.Label(main_window, text="Here you can either resize or ")
    lbl.pack(pady=5)
    lbl = tk.Label(main_window, text="convert the classic BBB video :)")
    lbl.pack(pady=5)
    resize_button = tk.Button(main_window,
                              text="Resize",
                              bg='#b4d2e0',
                              width=15,
                              height=3,
                              command=display_resize)
    resize_button.pack(pady=10)
    convert_button = tk.Button(main_window,
                               text="Convert",
                               bg='#b4d2e0',
                               width=15,
                               height=3,
                               command=display_coverter)
    convert_button.pack(pady=10)

    main_window.mainloop()