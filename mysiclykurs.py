import tkinter # основная библиотека
from tkinter import * # доп.функции библиотеки tkinter
import tkinter.messagebox # библиотека для вывода всплывающих окон
import customtkinter # установленная ранее библиотека для визуальной составляющей программы
import os, random, time # библиотеки для работы с системой Windows
import sys
import tkinter.messagebox as mb
import webbrowser # библиотека для работы с браузером. Она понадобится далее в программе
import musiclytexts # добавляем файл с текстами

# Настройка темы программы
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Создание основного окна программы
version = "v1.0" # переменная для показа версии обновления программы

# функция для кнопки очистки поля text-box
def clear_tb():
	text_box_for_track.delete(1.0, "end")

# функция с всплывающим окном для кнопки информации
def show_info():
	msg = "Вы можете написать свой текст в поле для текстов исполнителей или отредактировать уже готовый текст"
	mb.showinfo("Информация", msg)

# функция для перехода на веб-браузер
def open_music():
	webbrowser.open('https://vk.com/uniflynx?z=audio_playlist-169584269_2', new=2)

# временная функция рестарта программы
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Функции для кнопок на показ текста
def insert_text_on_box_korol():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_korol)
def insert_text_on_box_kiskis():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_kis_kis)
def insert_text_on_box_tdd():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_tdd)
def insert_text_on_box_aikko():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_aikko)
def insert_text_on_box_ec():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_egorc)
def insert_text_on_box_rv():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_rukiv)
def insert_text_on_box_lazarev():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_lazarev)
def insert_text_on_box_glucoza():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_glucoza)
def insert_text_on_box_basta():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_basta)
def insert_text_on_box_oxxy():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_oxxy)
def insert_text_on_box_gonef():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_gonefludd)
def insert_text_on_box_pyro():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_pyroki)
def insert_text_on_box_dk():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_dk)
def insert_text_on_box_saghat():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_saghat)
def insert_text_on_box_mk():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_mk)
def insert_text_on_box_lm():
	text_box_for_track.delete("1.0","end")
	text_box_for_track.insert("0.0", text_for_box_lm)

# ТЕКСТЫ ПЕСЕН ИСПОЛНИТЕЛЕЙ
text_for_box_korol = (musiclytexts.texts_korol)
text_for_box_kis_kis = (musiclytexts.texts_kis_kis)
text_for_box_tdd = (musiclytexts.texts_tdd)
text_for_box_aikko = (musiclytexts.texts_aikko)
text_for_box_egorc = (musiclytexts.texts_egor)
text_for_box_rukiv = (musiclytexts.texts_ruki)
text_for_box_lazarev = (musiclytexts.texts_lazarev)
text_for_box_glucoza = (musiclytexts.texts_glucoza)
text_for_box_basta = (musiclytexts.texts_basta)
text_for_box_oxxy = (musiclytexts.texts_oxxxy)
text_for_box_gonefludd = (musiclytexts.texts_gonef)
text_for_box_pyroki = (musiclytexts.texts_pyroc)
text_for_box_dk = (musiclytexts.texts_danyak)
text_for_box_saghat = (musiclytexts.texts_saghat)
text_for_box_mk = (musiclytexts.texts_krug)
text_for_box_lm = (musiclytexts.texts_lasmay)

app = customtkinter.CTk() # задаем основную переменную программы
app.geometry(f"{480}x{700}") # указываем разрешение экрана программы
app.title(f"Musicly : Ознакомление с жанрами музыки [{version}]") # создаем название программы
app.resizable(width=False, height=False) # запрещаем пользователю редактировать размер программы

# Основное поле программы
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

# Label названия программы
label_name_program = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="MUSICLY", font=customtkinter.CTkFont(size=30, weight="bold"))
label_name_program.pack(pady=10, padx=10)

# Текст выбора жанра и исполнителя
label_select_ispol = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Выберите жанр и исполнителя", font=customtkinter.CTkFont(size=15, weight="bold"))
label_select_ispol.pack(pady=0, padx=10)

# Создание списка жанров
tabview_janrs = customtkinter.CTkTabview(master=frame_1, width=200, height=70)
tabview_janrs.pack(pady=5, padx=0)
tabview_janrs.add("Rock")
tabview_janrs.add("Pop")
tabview_janrs.add("Hip-Hop")
tabview_janrs.add("Dubstep")
tabview_janrs.add("Chanson")

# Добавляем кнопки исполнителей по жанрам tabview
optionmenu_rock_korol = customtkinter.CTkButton(tabview_janrs.tab("Rock"), text="Король и Шут", command=insert_text_on_box_korol)
optionmenu_rock_korol.grid(row=0, column=0, padx=30, pady=(10, 10))
optionmenu_rock_kis_kis = customtkinter.CTkButton(tabview_janrs.tab("Rock"), text="Кис-Кис", command=insert_text_on_box_kiskis)
optionmenu_rock_kis_kis.grid(row=0, column=1, padx=30, pady=(10, 10))
optionmenu_rock_tdd = customtkinter.CTkButton(tabview_janrs.tab("Rock"), text="Три Дня Дождя", command=insert_text_on_box_tdd)
optionmenu_rock_tdd.grid(row=1, column=0, padx=30, pady=(10, 10))
optionmenu_rock_aikko = customtkinter.CTkButton(tabview_janrs.tab("Rock"), text="Aikko", command=insert_text_on_box_aikko)
optionmenu_rock_aikko.grid(row=1, column=1, padx=30, pady=(10, 10))
optionmenu_pop_egor = customtkinter.CTkButton(tabview_janrs.tab("Pop"), text="Егор Крид", command=insert_text_on_box_ec)
optionmenu_pop_egor.grid(row=0, column=0, padx=30, pady=(10, 10))
optionmenu_pop_ruki = customtkinter.CTkButton(tabview_janrs.tab("Pop"), text="Руки Вверх!", command=insert_text_on_box_rv)
optionmenu_pop_ruki.grid(row=0, column=1, padx=30, pady=(10, 10))
optionmenu_pop_lazarev = customtkinter.CTkButton(tabview_janrs.tab("Pop"), text="Лазарев", command=insert_text_on_box_lazarev)
optionmenu_pop_lazarev.grid(row=1, column=0, padx=30, pady=(10, 10))
optionmenu_pop_glucoza = customtkinter.CTkButton(tabview_janrs.tab("Pop"), text="Глюкоза", command=insert_text_on_box_glucoza)
optionmenu_pop_glucoza.grid(row=1, column=1, padx=30, pady=(10, 10))
optionmenu_hip_hop_basta = customtkinter.CTkButton(tabview_janrs.tab("Hip-Hop"), text="Баста", command=insert_text_on_box_basta)
optionmenu_hip_hop_basta.grid(row=0, column=0, padx=30, pady=(10, 10))
optionmenu_hip_hop_oxxy = customtkinter.CTkButton(tabview_janrs.tab("Hip-Hop"), text="Оксимирон", command=insert_text_on_box_oxxy)
optionmenu_hip_hop_oxxy.grid(row=0, column=1, padx=30, pady=(10, 10))
optionmenu_hip_hop_gonef = customtkinter.CTkButton(tabview_janrs.tab("Hip-Hop"), text="GONE.Fludd", command=insert_text_on_box_gonef)
optionmenu_hip_hop_gonef.grid(row=1, column=0, padx=30, pady=(10, 10))
optionmenu_hip_hop_pyroc = customtkinter.CTkButton(tabview_janrs.tab("Hip-Hop"), text="PYROKINESIS", command=insert_text_on_box_pyro)
optionmenu_hip_hop_pyroc.grid(row=1, column=1, padx=30, pady=(10, 10))
optionmenu_dubstep_danyak = customtkinter.CTkButton(tabview_janrs.tab("Dubstep"), text="Даня Кашин", command=insert_text_on_box_dk)
optionmenu_dubstep_danyak.grid(row=0, column=0, padx=30, pady=(10, 58))
optionmenu_dubstep_saghat = customtkinter.CTkButton(tabview_janrs.tab("Dubstep"), text="Сагат", command=insert_text_on_box_saghat)
optionmenu_dubstep_saghat.grid(row=0, column=1, padx=30, pady=(10, 58))
optionmenu_chansom_krug = customtkinter.CTkButton(tabview_janrs.tab("Chanson"), text="Михаил Круг", command=insert_text_on_box_mk)
optionmenu_chansom_krug.grid(row=0, column=0, padx=30, pady=(10, 58))
optionmenu_chansom_lasmay = customtkinter.CTkButton(tabview_janrs.tab("Chanson"), text="Ласковый Май", command=insert_text_on_box_lm)
optionmenu_chansom_lasmay.grid(row=0, column=1, padx=30, pady=(10, 58))

# Основной текст бокс программы
text_box_for_track = customtkinter.CTkTextbox(master=frame_1, width=400, height=250)
text_box_for_track.pack(pady=10, padx=10)
text_box_for_track.insert("0.0", "Текст песни исполнителя")

# Кнопка очистри поля text-box
button_clear = customtkinter.CTkButton(master=frame_1, text="Очистить поле", command=clear_tb)
button_clear.pack(pady=10, padx=10)

# Кнопка с всплывающим окном информации о использовании text-box
button_your_text = customtkinter.CTkButton(master=frame_1, text="Свой текст", command=show_info)
button_your_text.pack(pady=10, padx=10)

# Кнопка для перехода на браузер с мелодиями
button_beats = customtkinter.CTkButton(master=frame_1, text="Музыка", command=open_music)
button_beats.pack(pady=10, padx=10)

# Временная кнопка рестарта программы, для удобста
button_restart = customtkinter.CTkButton(master=frame_1, text="Restart", command=restart_program)
button_restart.pack(pady=10, padx=10)

app.mainloop() # параметр запуска программы. Без него программа не запустится