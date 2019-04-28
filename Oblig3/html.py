import codecs
import re


fileIn = codecs.open("got.txt", "r", "utf-8")
text = fileIn.read()
fileIn.close()

unicorn = "\n"
title = ""
keywords = ""
plain_text = []
html = "<!doctype html>"

firstIndex = 0
for i in range(len(text)):
    if text[i] + text[i + 1] + text[i + 2] + text[i + 3] == "<!--":
        firstIndex = i
        break

for i in range(firstIndex, len(text)):
    unicorn += text[i]
    if text[i] + text[i + 1] + text[i + 2] == "-->":
        unicorn += text[i + 1] + text[i + 2]
        break

firstIndex = 0
for i in range(len(text)):
    if text[i] + text[i + 1] + text[i + 2] + text[i + 3] + text[i + 4] + text[i + 5] + text[i + 6] == "<title>":
        firstIndex = i + 7
        break

for i in range(firstIndex, len(text)):
    title += text[i]
    if text[i + 1] + text[i + 2] + text[i + 3] + text[i + 4] + text[i + 5] + text[i + 6] + text[i + 7] + text[i + 8] == "</title>":
        break


firstIndex = 0
for i in range(len(text)):
    if text[i] + text[i + 1] + text[i + 2] + text[i + 3] + text[i + 4] + text[i + 5] + text[i + 6] + text[i + 7] == 'name="ke':
        firstIndex = i + 25
        break

for i in range(firstIndex, len(text)):
    keywords += text[i]
    if text[i + 1] + text[i + 2] == "\">":
        break

i = 0
while i < len(text):
    paragraph = ""

    firstIndex = 0
    if i + 2 < len(text) and text[i] + text[i + 1] + text[i + 2] == '<p>':
        firstIndex = i + 3
        for j in range(firstIndex, len(text)):
            paragraph += text[j]
            if text[j + 1] + text[j + 2] + text[j + 3] + text[j + 4] == "</p>":
                plain_text.append(paragraph)
                i = j + 5
                break

    i += 1

html += unicorn + "\n"
html += """\
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>""" + title + """</title>
        <style>
            h1 {
                text-decoration: underline;
            }
            
            span {
                color: red;
                font-style: italic;
            }
            
            ul {
                list-style-type: square;
            }
        </style>
    </head>
    <body>
        <h1>""" + title + """</h1>
        <p>Keywords: <span>""" + keywords + """</span></p>
        <ul>
"""

for p in plain_text:
    regex = re.compile('<.*?>')
    txt = re.sub(regex, '', p)
    html += "\t\t\t<li>" + txt + "</li>\n"

html += """\
        </ul>
    </body>
</html>
"""

fileOut = codecs.open("got_clean.html", "w", "utf-8")  # Creating the html file
fileOut.write(html)  # Writing the accumulated html to the file
fileOut.close()  # Closing the file to save it
