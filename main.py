from pygame_settings import *
from massivs import *
import datetime

pg.init()


def get_new_bottumn(content):
    global main_field
    main_field = 1


def censel_new_file(content):
    global main_field
    main_field = 0


def complite_file(text):
    global file_pos, main_field
    counter = 0
    if len(file_list) >= 1:
        file_list.append(Bottomn(x=width - 280, y=file_list[len(file_list) - 1].pos_y + 55, width=260, height=50, color=orange, field=root))
    else:
        file_list.append(Bottomn(x=width - 280, y=file_pos, width=260, height=50, color=orange, field=root))

    counter_file = open('settings_files/file_counter.txt', 'a')
    counter_file.write(f'{text}\n')
    counter_file.close()
    file_counter = open('settings_files/file_counter.txt', 'r')
    names = file_counter.readlines()
    file_counter.close()
    for i in range(len(names)):
        names[i] = names[i][:-1]

    for i in range(len(names)):
        if names[i] == text:
            counter += 1

    settings_file = open('settings_files/file_names.txt', 'a')

    if counter > 1:
        file = open(f'files/{text + str(counter)}.txt', 'w')
        file_list[len(file_list) - 1].set_text(text + str(counter), 50, blue)
        settings_file.write(f'{text + str(counter)}\n')
        file_names.append(f'{text + str(counter)}')
    else:
        file = open(f'files/{text}.txt', 'w')
        file_list[len(file_list) - 1].set_text(text, 50, blue)
        settings_file.write(f'{text}\n',)
        file_names.append(f'{text}')

    file.write('')

    file.close()
    settings_file.close()
    file_names.append(text)

    enter_name_file.change_text('Новый файл')

    main_field = 0

    for i in range(len(file_list)):
        file_list[i].run(True)


def open_file(file_name):
    global work_file, lets_work, current_file_name, work_file_text, max_word
    max_word = 0
    word_counter = 0

    work_file = open(f'files/{file_name}.txt', 'a')
    work_file_read = open(f'files/{file_name}.txt', 'r')
    lets_work = True

    for i in range(len(file_list)):
        file_list[i].run(False)

    work_file_text = work_file_read.readlines()
    current_file_name = file_name

    for i in range(len(work_file_text)):
        work_file_text[i] = work_file_text[i][:-1]
        word_counter += 1
        for j in range(len(work_file_text[i][:-1])):
            word_counter += 1

    if len(work_file_text) == 1 and len(work_file_text[0]) == 0:
        word_counter = 0

    if len(work_file_text) == 0:
        work_file_text.append('')

    max_word = word_counter
    work_file_read.close()
    work_file.close()


def blit_text(text, x, y):
    global work_file_text
    image = work_font.render(text, True, blask)
    root.blit(image, (x, y))


def save_file(file_name):
    global work_file_text, enter_color, lets_work_field
    text_list = []
    for i in range(len(work_file_text)):
        text_list.append(work_file_text[i])
        text_list[i] += '\n'
    with open(f'files/{file_name}.txt', 'w') as file:
        file.writelines(text_list)
        file.close()

    enter_color = white
    lets_work_field = False
    for i in range(len(file_list)):
        file_list[i].run(True)


with open('settings_files/file_names.txt', 'r') as file:
    file_settings = file.readlines()
    if len(file_settings) > 0:
        for i in range(len(file_settings)):
            file_names[i] = file_settings[i]
    file.close()

for i in range(len(file_settings)):
    file_list.append(Bottomn(x=width - 280, y=file_pos, width=260, height=50, color=orange, field=root))
    file_pos += 55

for i in range(len(file_settings)):
    file_list[i].set_text(file_names[i][:-1], 50, blue)

for i in range(len(file_list)):
    file_list[i].run(True)

while game_run:
    # constants
    root.fill(grey)
    main_mous_x, main_mous_y = pg.mouse.get_pos()
    keys = pg.key.get_pressed()
    date = datetime.date.today()
    current_time = datetime.datetime.now()

    time1 = '0' if current_time.hour < 10 else ''
    time2 = '0' if current_time.minute < 10 else ''
    time3 = '0' if current_time.second < 10 else ''
    date1 = '0' if date.day < 10 else ''
    date2 = '0' if date.month < 10 else ''

    time_label.set_text(f'Ч: {time1}{current_time.hour} М: {time2}{current_time.minute} С: {time3}{current_time.second}', 40, blask)
    date_label.set_text(f'Д: {date1}{date.day} M: {date2}{date.month} Г: {date.year}', 40, blask)

    FPS_text = else_informa_font.render(f'FPS: {FPS}', True, blask)
    word_text = else_informa_font.render(f'Слов: {max_word}/500', True, blask)
    current_file_text = else_informa_font.render(f'Файл: {current_file_name}', True, blask)

    root.blit(FPS_text, (20, 875))
    root.blit(word_text, (100, 875))
    root.blit(current_file_text, (250, 875))

    # main work

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_run = False

        if event.type == pg.MOUSEWHEEL and len(file_list) >= 13 and event.y == 1 and file_list[0].pos_y <= 80:
            for i in range(len(file_list)):
                file_list[i].pos_y += 20

        if event.type == pg.MOUSEWHEEL and len(file_list) >= 1 and event.y == -1 and file_list[len(file_list) - 1].pos_y >= height - 155:
            for i in range(len(file_list)):
                file_list[i].pos_y -= 20

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            get_bottumn.click(click=event, function=get_new_bottumn, pos_x=main_mous_x, pos_y=main_mous_y)
            finish_file_button.click(click=event, function=complite_file, pos_x=main_mous_x, pos_y=main_mous_y, content=enter_name_file.return_text())
            censel_file_button.click(click=event, function=censel_new_file, pos_x=main_mous_x, pos_y=main_mous_y)
            for i in range(len(file_list)):
                file_list[i].click(click=event, function=open_file, pos_x=main_mous_x, pos_y=main_mous_y, content=file_list[i].return_text())

            if main_field != 1 and not file_list[0].run_opportunity:
                save_to_file.click(click=event, function=save_file, pos_x=main_mous_x, pos_y=main_mous_y, content=current_file_name)

            if enter_rect.collidepoint(main_mous_x, main_mous_y) and lets_work:
                if enter_color == white:
                    enter_color = light_grey
                    lets_work_field = True
                    for i in range(len(file_list)):
                        file_list[i].run(False)
                else:
                    enter_color = white
                    lets_work_field = False
                    for i in range(len(file_list)):
                        file_list[i].run(True)

        for box in input_boxes_reg:
            box.handle_event(event, function=complite_file, content=enter_name_file.return_text())

        # enter block
        if event.type == pg.TEXTINPUT and lets_work_field and max_word < 500 and word_oport == True:
            work_file_text[-1] += event.text
            test_image = work_font.render(work_file_text[-1], True, blask)
            test_width = test_image.get_width()
            if test_width > 800 and len(work_file_text) < 20:
                work_file_text.append('')
            elif test_width > 800 and len(work_file_text) == 20:
                word_oport = False
            max_word += 1
        if event.type == pg.KEYDOWN and lets_work_field:
            if event.key == pg.K_BACKSPACE:
                if len(work_file_text[-1]) > 0:
                    work_file_text[len(work_file_text) - 1] = work_file_text[len(work_file_text) - 1][:-1]
                    max_word -= 1
                else:
                    if len(work_file_text) - 1 > 0:
                        work_file_text.pop(len(work_file_text) - 1)
                if word_oport == False:
                    word_oport = True
            if event.key == pg.K_RETURN:
                if len(work_file_text) < 20:
                    work_file_text.append('')

    pg.draw.rect(root, white, (width - 290, file_rect_y, 280, file_plays_y))

    for i in range(len(file_list)):
        file_list[i].draw(shift_y=8, shift_x=2)

    for i in range(len(firs_level_buttons)):
        firs_level_buttons[i].run(True)
    for i in range(len(second_level_buttons)):
        second_level_buttons[i].run(False)

    pg.draw.line(root, blask, (width - 300, 0), (width - 300, height), 2)
    pg.draw.rect(root, grey, (width - 290, 0, 280, 70))
    file_label.draw(border=5, shift_x=105, shift_y=12)
    pg.draw.rect(root, grey, (width - 290, height - 90, 280, 90))
    get_bottumn.draw(border=5, shift_x=57, shift_y=12)
    get_bottumn.guidens(x=main_mous_x, y=main_mous_y, guid_color=grey, border_color=blue)
    time_label.draw(border=5, shift_x=35, shift_y=12)
    date_label.draw(border=5, shift_x=20, shift_y=12)

    for i in range(len(file_list)):
        file_list[i].guidens(x=main_mous_x, y=main_mous_y, guid_color=yellow)

    # работа с файлом
    enter_rect = pg.Rect(20, 70, 860, 810)
    pg.draw.rect(root, enter_color, enter_rect)

    for row, line in enumerate(work_file_text):
        blit_text(line, 29, 65 + (row * 40))

    save_to_file.draw(border=5, shift_x=55, shift_y=9)
    save_to_file.guidens(main_mous_x, main_mous_y, grey)

    # поле создания файла
    if main_field == 1:
        for i in range(len(firs_level_buttons)):
            firs_level_buttons[i].run(False)
        for i in range(len(file_list)):
            file_list[i].run(False)
        for i in range(len(second_level_buttons)):
            second_level_buttons[i].run(True)

        pg.draw.rect(root, gluboi, (width // 2 - 300, height // 2 - 150, 600, 300))
        root.blit(get_file_text, (width // 2 - 280, height // 2 - 150))
        enter_name_file.draw(shift_y=9, border=2, border_color=blask, active_color=grey)
        finish_file_button.draw(border=2, shift_x=65, shift_y=7)
        censel_file_button.draw(border=2, shift_x=50, shift_y=7)
        name_file.draw(shift_y=9, border=2, shift_x=5)
        finish_file_button.guidens(main_mous_x, main_mous_y, grey)
        censel_file_button.guidens(main_mous_x, main_mous_y, grey)

    clock.tick(FPS)
    pg.display.flip()
    pg.display.set_caption('Заметки')
    pg.display.set_icon(pg.image.load('img/img.png'))