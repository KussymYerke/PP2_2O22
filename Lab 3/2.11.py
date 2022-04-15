def func(n):
    rev = n
    if(rev[::-1] == n):
        print("Palindrome")
    else:
        print("Not Palindrome")


n = input()
func(n)