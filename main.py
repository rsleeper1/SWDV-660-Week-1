import simple_math
from colorama import init, Fore, Back, Style

init(convert=True)

print(Fore.RED + "Welcome to math class!")
getInt = int(input("Please type a positive integer: "))
getFactors = simple_math.factors(getInt)
print("The factors of ", getInt, " are ", getFactors)
endProgram = input("Thanks for doing some math with me! Press enter to close application.")