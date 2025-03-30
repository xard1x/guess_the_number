from PyQt5.QtCore import Qt
from random import randint
from PyQt5.QtWidgets import *
from pygame import mixer
from PyQt5.QtGui import *

number = randint(1, 1) #создание переменой с выбором бота
popitki = 1 #переменая с оставшимися попытками

glob_attempts = 0 #переменные счетчики
glob_win = 0 
glob_defeat = 0
glob_counter = 0

app = QApplication([]) # создание окна
win = QWidget()
win.setWindowTitle('Угадай число') 
win.setMinimumSize(400, 400)
win.setMaximumSize(400, 400)

main_layout = QVBoxLayout() #создание основного лайаута
 
label1 = QLabel('Угадай число:')  #надпись
label1.setFont(QFont('Arial', 20))
hor_lay1= QHBoxLayout() #горизонтальный лайаут
hor_lay1.addWidget(label1, alignment= Qt.AlignCenter)
main_layout.addLayout(hor_lay1)

but_easy =QPushButton('Легкая сложность') #кнопки сложности
but_easy.setFont(QFont('Arial', 10))
but_hard =QPushButton('Сложная сложность')
but_hard.setFont(QFont('Arial', 10))
hor_lay2 = QHBoxLayout() #горизонтальный лайаут
hor_lay2.addWidget(but_easy, alignment= Qt.AlignCenter)
hor_lay2.addWidget(but_hard, alignment= Qt.AlignCenter)
main_layout.addLayout(hor_lay2)

num_text = QLineEdit('Введи число') #ввод пользователя
num_text.setFont(QFont('Arial', 10))
but_text =QPushButton('Потвердить') #кнопка потвердит
but_text.setFont(QFont('Arial', 10))
hor_lay3 = QHBoxLayout() #горизонтальный лайаут
hor_lay3.addWidget(num_text, alignment= Qt.AlignCenter)
hor_lay3.addWidget(but_text, alignment= Qt.AlignCenter)
main_layout.addLayout(hor_lay3)

res_text = QLabel('Результат:') #надпись результат и результат
res_text.setFont(QFont('Arial', 10))
result = QLabel('-')
result.setFont(QFont('Arial', 10))
hor_lay4 = QHBoxLayout() #горизонтальный лайаут
hor_lay4.addWidget(res_text, alignment= Qt.AlignCenter)
hor_lay4.addWidget(result, alignment= Qt.AlignCenter)
main_layout.addLayout(hor_lay4)

pop_text = QLabel('Попыток осталось:') #надпись результат и результат
pop_text.setFont(QFont('Arial', 10))
pop = QLabel('-')
pop.setFont(QFont('Arial', 10))
hor_lay5 = QHBoxLayout() #горизонтальный лайаут
hor_lay5.addWidget(pop_text, alignment= Qt.AlignCenter)
hor_lay5.addWidget(pop, alignment= Qt.AlignCenter)
main_layout.addLayout(hor_lay5)

but_stat = QPushButton('Статистика') #кнопка статистики
but_stat.setFont(QFont('Arial', 13))
but_music = QPushButton('Музыка')
but_music.setFont(QFont('Arial', 13))
but_pause = QPushButton('Стоп')
but_pause.setFont(QFont('Arial', 13))
hor_lay5 = QHBoxLayout() #горизонтальный лайаут
hor_lay5.addWidget(but_stat, alignment= Qt.AlignCenter)
hor_lay5.addWidget(but_music, alignment= Qt.AlignCenter)
hor_lay5.addWidget(but_pause, alignment= Qt.AlignCenter)
main_layout.addLayout(hor_lay5)
but_pause.hide()

def okno(): #функция создания окна для статистики
    global stat_title
    global stat_text
    msg_kk = QMessageBox()
    msg_kk.setWindowTitle('Статистика')
    msg_kk.setInformativeText(stat_text)
    msg_kk.setText(stat_title)
    msg_kk.setIcon(QMessageBox.Question)
    msg_kk.exec_()
def hard(): #функция нажатия сложной сложности
    global number
    global popitki
    label1.setText('Угадай число от 1 до 100')
    number = randint(1, 100)
    popitki = 8
    but_text.show()
    pop.setText(str(popitki))
def easy():#функция нажатия легкой сложности
    global number
    global popitki
    label1.setText('Угадай число от 1 до 50')
    number = randint(1, 50)
    popitki =  5
    pop.setText(str(popitki))
    but_text.show()
def confirm(): #проверка ввода пользователя и числа выбраного на рандом
    global glob_counter
    global glob_attempts
    global glob_win 
    global glob_defeat
    global number
    global popitki
    value = num_text.text()
    if number == int(value):
        result.setText('Ты выиграл')
        glob_win += 1
        glob_counter += popitki
        glob_attempts += 1
        but_text.hide()
    if number < int(value):
        result.setText('Слишком большое число')
        popitki -= 1
        glob_attempts += 1
        pop.setText(str(popitki))
    if number > int(value):
        result.setText('Слишком маленькое число')
        popitki -= 1
        glob_attempts += 1
        pop.setText(str(popitki))
    if popitki == 0:
        pop.setText('0')
        glob_counter -= 5
        glob_defeat += 1
        glob_attempts += 1
        result.setText('Ты проиграл')
        but_text.hide()
def statistics(): #функция с выводом статистики
    global glob_counter
    global glob_attempts
    global glob_win 
    global glob_defeat
    global stat_title
    global stat_text
    stat_title = 'Общий счет:'
    stat_text = str(glob_counter)
    okno()
    stat_title = 'Кол-во побед:'
    stat_text = str(glob_win)
    okno()
    stat_title = 'Кол-во поражений:'
    stat_text = str(glob_defeat)
    okno()
    stat_title = 'Кол-во попыток:'
    stat_text = str(glob_attempts)
    okno()
def play_music(): #проигрывание музыки
    volume = 1
    mixer.init()
    mixer.music.load('music.wav')
    mixer.music.play(-1)
    mixer.music.set_volume(volume)
    but_music.hide()
    but_pause.show()
def pause(): #остановка музыки
    but_music.show()
    mixer.music.pause()
    but_pause.hide()

but_pause.clicked.connect(pause)
but_stat.clicked.connect(statistics) #заключение
but_text.clicked.connect(confirm)
but_hard.clicked.connect(hard)
but_easy.clicked.connect(easy)
but_music.clicked.connect(play_music)
win.setLayout(main_layout)
win.show()
app.exec()