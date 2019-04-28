import codecs
import re


fileIn = codecs.open("got.txt", "r", "utf-8")  # Opening the input file
text = fileIn.read()  # Reading the contents of the input file
fileIn.close()  # Closing the input file as it is no longer needed

# Declaring the variables the will store the results
unicorn = "\n"
title = ""
keywords = ""
html = "<!doctype html>"

# Finding the unicorn in the text
regex = r"<!--.*?-->"
matches = re.findall(regex, text, flags=re.DOTALL)
unicorn += matches[0]

# Finding the title of the article
regex = "<title>.*</title>"
matches = re.findall(regex, text)
title += re.sub(re.compile('<.*?>'), '', matches[0])

# Finding the keywords
regex = "<meta name=\"keywords\" content=\".*\">"
matches = re.findall(regex, text)
temp = matches[0]
keywords += temp[len("<meta name=\"keywords\" content=\".*\">") - 4:-2]

# Finding the paragraphs of the article
regex = "<p>.*</p>"
matches = re.findall(regex, text)
plain_text = matches

# Adding the results to the html string
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

# Adding the paragraphs to the list after removing the markup
for p in plain_text:
    regex = re.compile('<.*?>')
    txt = re.sub(regex, '', p)
    html += "\t\t\t<li>" + txt + "</li>\n"

# Adding the closing html tags
html += """\
        </ul>
    </body>
</html>
"""

fileOut = codecs.open("got_clean.html", "w", "utf-8")  # Creating the html file
fileOut.write(html)  # Writing the accumulated html to the file
fileOut.close()  # Closing the file to save it
