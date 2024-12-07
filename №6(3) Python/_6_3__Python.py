
from collections import Counter

def search():
    a = input('Enter your number: ')
    b = Counter(a)
    c = max(b.values())

    result = [digit for digit, count in b.items() if count == c]

    print(f"Most frequent digits: {' '.join(result)}") 
    print(f"Frequency: {b}")

search()