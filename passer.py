yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
print(red+b+'''
             ██████╗░░█████╗░░██████╗░██████╗███████╗██████╗░
             ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗
             ██████╔╝███████║╚█████╗░╚█████╗░█████╗░░██████╔╝
             ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗██╔══╝░░██╔══██╗
             ██║░░░░░██║░░██║██████╔╝██████╔╝███████╗██║░░██║
             ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
'''+b+red)

print(yellow+b+'           --[[<---------coded by V180ET------>]]--'+b+yellow)
print(' ')
print(yellow+b+'      ----[[--------<search me on github by vineet 519>-------]]---'+b+yellow)
print(' ')
import random

def generatePassword(length):
    characters = [chr(n) for n in range(33, 127)]
    return "".join(random.choices(characters, k=length))



length = int(input(cyan+b+"Enter your password length: "+b+cyan))
print(gren+'[<---------------------------password generated-------------------------]>'+gren)
print(' ')
print(yellow+ generatePassword(length)+yellow)
print(' ')
print(gren+'[----------------------------<Take your password>------------------------]'+gren)
