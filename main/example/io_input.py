def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")


"""
$ python3 io_input.py
Enter text: sir
No, it is not a palindrome

$ python3 io_input.py
Enter text: madam
Yes, it is a palindrome

$ python3 io_input.py
Enter text: racecar
Yes, it is a palindrome
"""

"""
我们使用切片特性来反转文本。
我们已经知道了如何通过 seq[a:b] 来得到位置 a 到位置 b 的 序列切片 。
我们也可以提供第三个参数来决定切片的 步长 。默认的步长是 1 ，因为这样会返回文本连续的部分。
给一个负值的步长，即 -1 ，会返回文本的反转。

 input() 函数将字符串作为参数，并且展示给用户。
然后它会等待用户输入并按下返回键。一旦用户输入并按下了返回键， input() 函数会将会返回用户输入的文本。

我们得到文本并反转它。如果原始文本和反转文本相等，那么这个文本就是一个 回文(http://en.wiktionary.org/wiki/palindrome) 。

"""
