from operator import add, mul

max_num = max(3, 1)
min_num = min(-1, 5)
add_num = add(2,3)
mul_num = mul(3,5)


shakes = open("shakespeare.txt")
text = shakes.read().split()

words = set(text)

# List comprehension
# [Expression for item in list]
palindromes = {w for w in words if w[::-1] == w and len(w) > 2}
palindromes_in_words = {w for w in words if w[::-1] == w and w in words and len(w) > 2}
print(palindromes)
print(palindromes_in_words)

words = open("/usr/share/dict/words").read().split()
palindrome_two = {w for w in words if w[::-1] == w and len(w) > 2}
palindrome_two_in_var_words = {w for w in words if w[::-1] == w and len(w) > 2 and w in words}
print(f"Palindrome: {palindrome_two}")
print(f"Palindrome: {palindrome_two_in_var_words}")
