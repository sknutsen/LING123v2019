TEXT1 = ["The politician who holds the authority of all EU countries has just completely condemned a chunk of the British cabinet wondering aloud",
"What that special place in hell looks like for those who promoted Brexit without even a sketch of a plan how to carry it out safely",
"Sure for a long time the EU has been frustrated with how the UK has approached all of this",
"And sure plenty of voters in the UK are annoyed too at how politicians have been handling these negotiations",
"But it is quite something for Donald Tusk to have gone in like this studs up even though he sometimes reminisces about his time as a football hooligan in his youth"]

TEXT2 = ["An outbreak of the flu in Alabama has closed an elementary and middle school with school officials struggling to find enough healthy teachers to teach",
"The schools will be closed for the rest of the week because of the number of cases of flu among students and employees",
"Lawrence County Schools Superintendent Jon Bret Smith told news outlets that Moulton Elementary School and Moulton Middle School are closed Wednesday through Friday"]

# Counts the words in the specified text
def count_words(text):
    word_count = 0
    for sentence in text:
        words = sentence.split(" ")
        word_count += len(words)
    return word_count


# Counts the estimated number of syllables in the specified text based on number of vowels
def count_syllables(text):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    syllable_count = 0
    for sentence in text:
        for char in sentence:
            if char in vowels:
                syllable_count += 1
    return syllable_count


# Calculations for TEXT1
TEXT1_words = count_words(TEXT1)  # count the number of words in TEXT1

TEXT1_sentences = len(TEXT1)  # count the number of words in TEXT1

TEXT1_syllables = count_syllables(TEXT1)  # count the number of words in TEXT1

# FRES for TEXT1
TEXT1_FRES = 206.835 - 1.015 * (TEXT1_words / TEXT1_sentences) - 84.6 * (TEXT1_syllables / TEXT1_words)  


# Calculations for TEXT2
TEXT2_words = count_words(TEXT2)  # count the number of words in TEXT2

TEXT2_sentences = len(TEXT2)  # count the number of words in TEXT2

TEXT2_syllables = count_syllables(TEXT2)  # count the number of words in TEXT2

# FRES for TEXT2
TEXT2_FRES = 206.835 - 1.015 * (TEXT2_words / TEXT2_sentences) - 84.6 * (TEXT2_syllables / TEXT2_words)  
