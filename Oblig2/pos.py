import codecs

file = codecs.open('pos_input.txt', 'r', 'utf-8')
pos_input = file.read()            # Retrieving the contents of the input file
file.close()

words = pos_input.split()
results = []
previous_word = ''
for word in words:
    if 'PUNCT' in previous_word and ('NOUN' in word or 'PRON' in word or 'PROPN' in word):
        results.append(previous_word + ' ' + word)
    previous_word = word

results.sort()
for r in results:
    print(r)

most_common_sequence = results[0]
most_common_sequence_count = results.count(results[0])
for word in results:
    w_count = results.count(word)
    if w_count > most_common_sequence_count:
        most_common_sequence = word
        most_common_sequence_count = w_count

print('\n', most_common_sequence, most_common_sequence_count)
