import hashlib
import termcolor2
import termcolor
from colorama import Fore


# efcoriti

#Demonstrates the difference between two types of hashing, SHA1 and Bcrypt
print(Fore.BLUE)
print("""    
                        ###############
                      ##################
                   ######################
                  #########################
                ###########################
               #############################
               ##############################
              ##############################
              #############################
                              ##########
                 ## ### #### ##
                                      ### ###
                                    #### ###
               #### ##############
               ##########################
                 #######################
                  #####################
                    ##############
                       ###########
                      ##############
                    ##################
                   #################
                     ##### #######
                       ### #########
                      ##################
                     ######################
                     #########
                     #######################
                      ## ## ## ##""")
print(termcolor2.colored('id tel and rubika >> @efcoriti ',color = "cyan"))
print(termcolor2.colored('channel telegram : @efcoriti_programmer' , color = "cyan"))
print("\n\n\n")
password = input(termcolor2.colored('Input the password to hash\n> ',color = "red"))
print(Fore.YELLOW)
print("\nSHA1===>>\n")
for i in range(3):
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.sha1(setpass)
    guess_pw = hash_object.hexdigest()
    print(guess_pw)
print(Fore.GREEN)
print("\n")
print("\nMD5===>>\n")

for i in range(3):
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.md5(setpass)
    guess_pw = hash_object.hexdigest()
    print(guess_pw)


print("\n\n\n\n\n\n\n\n\n\n\n\n")
print(Fore.BLUE)
print("""coded by efcoriti
       goodbye""")
