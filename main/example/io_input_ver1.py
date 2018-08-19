"""
对英文来说检查一段文字是不是回文，需要忽略标点、空格和大小写。例如："Rise to vote, sir." 是一句回文。
"""


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")
# 除去标点、空格
forbidden = ('!', '?', '.', '...', ',', ' ')
for item in forbidden:
    if item in something:
        something = something.replace(item, '')
# 大小写转换成小写
something = something.lower()
print(something)

if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")



