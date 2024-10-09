def count_vowels(s):
    vowels = "aeiouAEIOU"  # Include both lowercase and uppercase vowels
    count = sum(1 for char in s if char in vowels)
    return count

# Example usage
input_string = "Hello, World!"
vowel_count = count_vowels(input_string)
print(f"The number of vowels in '{input_string}' is: {vowel_count}")
