def highest_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] = char_count[char]+1
        else:
            char_count[char] = 1
    highest_char = None
    highest_count = 0
    for char, count in char_count.items():
        if count > highest_count:
            highest_count = count
            highest_char = char
    return highest_char, highest_count
input_string = "hippopatamus"
char, count = highest_characters(input_string)
print(f"The highest occurring character is '{char}' with {count} occurrences.")
