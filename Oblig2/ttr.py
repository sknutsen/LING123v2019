import codecs

file = codecs.open('ttr_input.txt', 'r', 'utf-8')
ttr_input = file.read()            # Retrieving the contents of the input file
file.close()


words = ttr_input.split()          # Creating a list with all the words from the text
unique_words = []                  # Creating a list that only contains unique words (no duplicates)
for word in words:
    if word not in unique_words:
        unique_words.append(word)  # Adding word to list if it has not been added prior


ttr = (len(unique_words) / len(words)) * 100  # Calculating the Type-Token Ratio


print(ttr)  # Printing out the results
