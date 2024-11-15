import string


def word_count(filepath):
    result_word_count = {}

    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.lower()
                line = line.translate(str.maketrans('', '', string.punctuation))

                words = line.split()
                for word in words:
                    if word in result_word_count:
                        result_word_count[word] += 1
                    else:
                        result_word_count[word] = 1
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Cannot read file")

    return result_word_count

# Example usage:
counts = word_count('sample.txt')
print(counts)
