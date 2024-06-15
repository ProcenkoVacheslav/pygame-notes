import pygame as pg
from settings import *
from colors import *
from bottoms import Bottomn
from massivs import *
from enterboxes import *
import datetime

pg.init()

# fonts
else_informa_font = pg.font.SysFont('arial', 20)

root = pg.display.set_mode((width, height))
clock = pg.time.Clock()

get_file_font = pg.font.SysFont('arial', 70)
get_file_text = get_file_font.render('Создать новый файл', True, green)

time_label = Bottomn(x=300, y=0, width=300, height=50, color=white, field=root, border_color=blask)
date_label = Bottomn(x=600, y=0, width=300, height=50, color=white, field=root, border_color=blask)
file_label = Bottomn(x=900, y=0, width=300, height=50, color=white, field=root, border_color=blask)
file_label.set_text('Файлы', 40, blask)

get_bottumn = Bottomn(x=0, y=0, width=300, height=50, color=white, field=root, border_color=blask)
get_bottumn.set_text('Новый файл.', 40, blask)
all_bottumns.append(get_bottumn)
firs_level_buttons.append(get_bottumn)

finish_file_button = Bottomn(x=width // 2 - 280, y=height // 2 + 30, width=275, height=50, color=white, field=root, border_color=blask)
finish_file_button.set_text('Готово', 60, blask)
all_bottumns.append(finish_file_button)
second_level_buttons.append(finish_file_button)

censel_file_button = Bottomn(x=width // 2 + 5, y=height // 2 + 30, width=275, height=50, color=white, field=root, border_color=blask)
censel_file_button.set_text('Отмена', 60, blask)
all_bottumns.append(censel_file_button)
second_level_buttons.append(censel_file_button)

name_file = Bottomn(x=width // 2 - 280, y=height // 2 - 50, width=90, height=50, color=white, field=root)
name_file.set_text('Имя:', 50, blask)
all_bottumns.append(name_file)
second_level_buttons.append(name_file)

save_to_file = Bottomn(x=900, y=830, width=300, height=50, color=white, border_color=blask, field=root)
save_to_file.set_text('Сохранить', 50, blask)
save_to_file.run(True)
all_bottumns.append(save_to_file)

enter_name_file = EnterField(word_size=50, x=width // 2 - 190, y=height // 2 - 50, width=470, height=50, color=white, field=root, text='Новый файл', len=11)
input_boxes_reg.append(enter_name_file)
second_level_buttons.append(enter_name_file)

work_font = pg.font.SysFont('arial', 40)