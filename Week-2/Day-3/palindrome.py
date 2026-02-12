def is_palindrome(word):
    left = 0
    right = len(word) - 1

    while(left <= right):
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    
    return True

words = ["dad", "bat", "Axilex", "pap"]
for w in words:
    if is_palindrome(w):
        print(w, " -> Palindrome")
    else:
        print(w, " -> Not palindrome")

    