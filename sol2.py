from colorama import Fore, Back, Style, init
init(autoreset=True)


def solution(n):
    sum = 0
    terms = (n - 1) // 3
    sum += (terms * (6 + (terms - 1) * 3)) // 2  # sum of an A.P.
    terms = (n - 1) // 5
    sum += (terms * (10 + (terms - 1) * 5)) // 2
    terms = (n - 1) // 15
    sum -= (terms * (30 + (terms - 1) * 15)) // 2
    return Fore.GREEN + f'The result is {sum}'


if __name__ == "__main__":
    print(solution(int(input(Back.RED + 'Put number here: ').strip())))

# print(Fore.BLUE + 'This is Blue')
# print(Fore.RED + 'This is Blue')
# print(Fore.WHITE + 'This is Blue')
#
# print("auto reset")

