import codecs


fileIn = codecs.open("shake.txt", "r", "utf-8")  # Opening the input file
text = fileIn.read()  # Retrieving the contents of the input file
fileIn.close()  # Closing the input file as it is no longer needed

# Creating the outline of the xml file
xml = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>

<!DOCTYPE poem [
<!ELEMENT poem (stanza+)>
<!ELEMENT stanza (token+)>
<!ATTLIST stanza s-id CDATA #REQUIRED>
<!ELEMENT token (wordform,rhyme)>
<!ATTLIST token t-id CDATA #REQUIRED>
<!ELEMENT wordform (#PCDATA)>
<!ELEMENT rhyme (#PCDATA)>
]>

<poem>
"""

stanzalist = text.split("\n\n")  # Splits the text into a list of the stanzas

# Iterating through the stanzas
for i, stanza in enumerate(stanzalist):
    i += 1  # Adding 1 so that the first stanza has the s-id 1 instead of 0
    xml += "\t<stanza s-id=\"" + str(i) + "\">\n"  # Adding the tag representing the current stanza to the xml result
    rhyme = ""  # Creating a variable to store the rhyme of a line
    k = 1  # Creating a variable to store what the number of the current word/token is

    lines = stanza.split("\n")  # Splitting the current stanza into lines
    for j, line in enumerate(lines):
        if j in [0, 2]:
            rhyme = "A"  # Assigning A to the rhyme if the current line is either 1st or 3rd
        elif j in [1, 3, 4]:
            rhyme = "B"  # Assigning A to the rhyme if the current line is either 2nd or 4th or 5th
        elif j in [5, 6]:
            rhyme = "C"  # Assigning A to the rhyme if the current line is either 6th or 7th

        tokens = line.split(" ")  # Splitting the line into tokens
        for token in tokens:  # Adding tags representing the current token which contains wordform and rhyme
            if token == '&':  # If the token is & then it is replaced with &amp; in order to avoid errors
                xml += "\t\t<token t-id=\"" + str(i) + "-" + str(k) + "\">\n\t\t\t<wordform>&amp;</wordform>\n\t\t\t<rhyme>" + rhyme + "</rhyme>\n\t\t</token>\n"
            else:
                xml += "\t\t<token t-id=\"" + str(i) + "-" + str(k) + "\">\n\t\t\t<wordform>" + token + "</wordform>\n\t\t\t<rhyme>" + rhyme + "</rhyme>\n\t\t</token>\n"
            k += 1

    xml += "\t</stanza>\n"  # Adding the closing tag to the stanza

xml += "</poem>"  # Adding the closing tag to the poem

print(xml)  # Printing out the xml code directly to the console

fileOut = codecs.open("shake.xml", "w", "utf-8")  # Creating the xml file
fileOut.write(xml)  # Writing the accumulated xml code to the file
fileOut.close()  # Closing the file to save it
