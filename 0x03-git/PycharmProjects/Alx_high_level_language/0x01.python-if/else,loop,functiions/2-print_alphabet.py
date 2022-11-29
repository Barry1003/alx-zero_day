for alpha_letters in range(ord('A'), ord('Z')+1):
    if alpha_letters == 'e' or alpha_letters == 'q':
       continue
    print("{:c} ".format(alpha_letters), end="\n")
# alternatively using the sting module

import string
for alpha_letters in string.ascii_lowercase:
    if alpha_letters not in 'qe':
        print(alpha_letters, end="")