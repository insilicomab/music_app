import tkinter
import tkinter.filedialog
from tkinter import ANCHOR, END

import pygame.mixer as pymix


# アイテムを追加する関数
def add_item():
    file_type = [("", "*")]  # すべてのファイルを閲覧
    file_name = tkinter.filedialog.askopenfilename(filetypes=file_type, initialdir="./")
    my_listbox.insert(END, file_name)  # END: 末尾


# アイテムを選択削除する関数
def remove_item():
    my_listbox.delete(ANCHOR)  # ANCHOR: 選択したもの


# 一括削除する関数
def clear_list():
    my_listbox.delete(0, END)


# 音声を再生する関数
def play():
    global music_player
    # すでに再生中の音声を終了する
    pymix.quit()

    # 再生するファイルのパスを取得
    n = my_listbox.curselection()
    sound_file = my_listbox.get(n)
    print(f"{n}番目の曲")
    print(f"再生ファイル：{sound_file}")

    # 音声再生
    pymix.init()
    sounds = pymix.Sound(sound_file)
    music_player = sounds.play()
    music_player.set_volume(0.1)  # 0.01刻みで0.00～1.00まで選択可能


# 音声を一時停止する関数
def stop():
    pymix.pause()


# 音声再生を再開する関数
def restart():
    pymix.unpause()


# 音量を調整する関数
def adjust_volume(volume):
    music_player.set_volume(float(volume))


if __name__ == "__main__":
    # ウィンドウの作成
    root = tkinter.Tk()
    root.title("音楽再生アプリ")
    root.iconbitmap("music.ico")
    root.geometry("500x600")
    root.resizable(False, False)

    # フォントの定義
    basic_font = ("Times New Roman", 12)
    list_font = ("Times New Roman", 15)

    # フレームの作成
    input_frame = tkinter.Frame(root)
    output_frame = tkinter.Frame(root)
    button_frame = tkinter.Frame(root)
    vol_frame = tkinter.Frame(root)
    input_frame.pack()
    output_frame.pack()
    button_frame.pack()
    vol_frame.pack()

    # ファイルに関するボタンを作成
    list_add_button = tkinter.Button(
        input_frame, text="追加", borderwidth=2, font=basic_font, command=add_item
    )
    list_remove_button = tkinter.Button(
        input_frame, text="選択削除", borderwidth=2, font=basic_font, command=remove_item
    )
    list_clear_button = tkinter.Button(
        input_frame, text="一括削除", borderwidth=2, font=basic_font, command=clear_list
    )
    list_add_button.grid(row=0, column=0, padx=2, pady=15, ipadx=5)
    list_remove_button.grid(row=0, column=1, padx=2, pady=15, ipadx=5)
    list_clear_button.grid(row=0, column=2, padx=2, pady=15, ipadx=5)

    # スクロールバーの追加
    my_scrollbar = tkinter.Scrollbar(output_frame, orient="vertical")

    # 音楽リストの作成
    my_listbox = tkinter.Listbox(
        output_frame,
        width=45,
        height=15,
        yscrollcommand=my_scrollbar.set,
        borderwidth=3,
        font=list_font,
    )  # yscrollcommand: Scrollbarオブジェクトのsetでスクロールバーを設定
    my_listbox.grid(row=0, column=0)

    # スクロールバーの配置
    my_scrollbar.config(command=my_listbox.yview)
    my_scrollbar.grid(row=0, column=1, sticky="NS")  # sticky: Nは上、Sは下

    # 音楽再生に関するボタン作成
    play_button = tkinter.Button(
        button_frame, text="再生", borderwidth=2, font=basic_font, command=play
    )
    stop_button = tkinter.Button(
        button_frame, text="一時停止", borderwidth=2, font=basic_font, command=stop
    )
    restart_button = tkinter.Button(
        button_frame, text="再開", borderwidth=2, font=basic_font, command=restart
    )
    play_button.grid(row=0, column=0, padx=5, pady=15, ipadx=5)
    stop_button.grid(row=0, column=1, padx=5, pady=15, ipadx=5)
    restart_button.grid(row=0, column=2, padx=5, pady=15, ipadx=5)

    # 音量バーの作成
    vol_label = tkinter.Label(vol_frame, text="音量")
    vol_scale = tkinter.Scale(
        vol_frame,
        orient="horizontal",
        length=300,
        from_=0.0,
        to=1.0,
        resolution=0.01,
        showvalue=False,  # 上の数字を非表示
        command=adjust_volume,
    )
    vol_scale.set(0.1)
    vol_label.grid(row=0, column=0, padx=10)
    vol_scale.grid(row=0, column=1, padx=10)

    # ループ処理の実行
    root.mainloop()
