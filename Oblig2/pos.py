import codecs

file = codecs.open('pos_input.txt', 'r', 'utf-8')  # Opening the input file
pos_input = file.read()  # Retrieving the contents of the input file
file.close()  # Closing the input file as it is no longer needed

words = pos_input.split()  # Splitting the contents of the text into a list
results = []  # Creating the list that will contain all the words that fit the specified requirements
previous_word = ''  # A string to store the previous element of the list in order to find the fitting pairs
for word in words:
    if 'PUNCT' in previous_word and ('NOUN' in word or 'PRON' in word or 'PROPN' in word):
        results.append(previous_word + ' ' + word)  # Adding all nouns (NOUN, PRON and PROPN) preceded by PUNCT
    previous_word = word  # Setting the current element as the previous for the next iteration

results.sort()  # Sorting the list to make it easier to read when the results are printed
for result in results:
    print(result)  # Printing the list of sequences

print('\n')


# Task 7

# The list of alternatives to look for
alternatives_list = ['./PUNCT MPs/PROPN', ':/PUNCT Fallout/PROPN', ',/PUNCT Wednesday/PROPN', '?/PUNCT Brexit/NOUN',
                     '-/PUNCT deal/NOUN', './PUNCT Government/NOUN', '?/PUNCT Theresa/PROPN', ':/PUNCT What/NOUN',
                     '?/PUNCT What/NOUN', '?/PUNCT MPs/NOUN', './PUNCT What/NOUN', ':/PUNCT Something/NOUN',
                     './PUNCT Brexit/PROPN', './PUNCT She/PRON']
for alternative in alternatives_list:
    contained_in_list = False
    if alternative in results:
        contained_in_list = True  # Assigning True if the alternative is present
    print(alternative, contained_in_list)  # Printing the alternative and True if present, False if not


# Task 8

most_common_sequence = results[0]
most_common_sequence_count = results.count(results[0])
for sequence in results:
    sequence_count = results.count(sequence)  # Counting how many times a given sequence appears in the results list
    if sequence_count > most_common_sequence_count:
        most_common_sequence = sequence  # Declaring the current sequence the most common if more common than old value
        most_common_sequence_count = sequence_count  # Replacing the count

# Printing the most common sequence and how many times it appears
print('\nMost common Sequence: ', most_common_sequence, 'appears', most_common_sequence_count, 'times.')
