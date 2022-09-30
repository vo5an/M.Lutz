'''Файл certificate.py:сценарий на Python.
Генерирует простой сертификат об окончании чтения: Выводит
и сохраняет в текстовом и HTML-файле, отображаемом в веб-браузере.
'''

from __future__ import print_function
import time, sys, webbrowser

if sys.version_info[0] ==2:
    input = raw_input
    import cgi
    htmlescape = cgi.escape
else:
    import html
    htmlescape = html.escape

maxline = 60
browser = True
saveto = 'Certificate.txt'
template = '''
%s
===> Official Certificate <===

Date: %s

This certificates that:

\t%s

has survived the massive tome:

\t%s

and is now entitled to all privileges thereof, including
the right to procces on to learning how to develop Web
sites, desctop GUIs, scientific models, and assorted Apps,
with the possible assistance of follow-up applications
books such as Programming Python (shameless plug intended).

-- Mark Lutz, Instructor

(Note: certificate void where obtained by skipping ahead.)

%s
'''

#Взаимодействие, настройка
for c in 'Conglatulations!'.upper():
    print(c, end=' ')
    sys.stdout.flush()
    time.sleep(0.25)

print()

date = time.asctime()
name = input('Enter your name: ').strip() or 'An unknown reader'
sept = '*' * maxline
book = 'Learning Python 5th Edition'

# Создание версии в текстовом файле
file = open(saveto, 'w')
text = template % (sept, date, name, book, sept)
print(text, file = file)
file.close()

#Создание версии в файле html
htmlto = saveto.replace('.txt', '.html')
file = open(htmlto, 'w')

tags = text.replace(sept, '<hr>')   # Вставка нескольких html  - дескрипторов
tags = tags.replace('===>', '<h1 align=center>')
tags = tags.replace('<===', '</h1>')

tags = tags.split('\n')       #Построчный режим
tags = ['<p>' if line ==''
              else line for line in tags]
tags = ['<i>%s</i>' % htmlescape(line) if line[:1] == '\t'
                     else line for line in tags]
tags = '\n'.join(tags)

link = '<i><a href="http://www.rmi.net/~lutz">Book support site</a></i>\n'
foot = '<table>\n<td><img scr="ora-lp.jpg" hspace=5>\n<td>%s</table>\n' % link
tags = '<html><body bgcolor=beige>' + tags + foot + '</body></html>'

print(tags, file=file)
file.close()

#Отображение результатов
print('[File: %s]' % saveto, end ='')
print('\n' * 2, open(saveto).read())

if browser:
    webbrowser.open(saveto, new = True)
    webbrowser.open(htmlto, new = False)

if sys.platform.startswith('win'):
    input('[Press Enter]') # Оставить окно открытым при щелчке в Windows
