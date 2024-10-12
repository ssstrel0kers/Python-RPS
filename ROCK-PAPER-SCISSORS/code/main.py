import random
import time

print('                                                                                                         ')
print('                                                                                                         ')
print('   Rock, Paper, Scissors!')
print('   ---------------------------------------------------------------------------------------------------------')
text = input('   What will you use: rock, scissors or paper? (write in the nominative case with a small letter) ')

random1 = random.sample((1, 2, 3), 1)

if text == 'rock' and random1 == [1]:
    print('   We have a draw. I have a rock too.')
    print('   ---------------------------------------------------------------------------------------------------------')
    print('   Happy end!')
    time.sleep(3)
    quit()
elif text == 'scissors' and random1 == [3]:
    print('   We have a draw. I have a scissors too.')
    print('   ---------------------------------------------------------------------------------------------------------')
    print('   Happy end!')
    time.sleep(3)
    quit()
elif text == 'paper' and random1 == [2]:
    print('   We have a draw. I have a paper too.')
    print('   ---------------------------------------------------------------------------------------------------------')
    print('   Happy end!')
    time.sleep(3)
    quit()
elif text == 'rock' and random1 == [2]:
    print('   I won! I have paper.')
    print('   ---------------------------------------------------------------------------------------------------------')
    print('   You lose!')
    time.sleep(3)
    quit()
elif text == 'rock' and random1 == [3]:
    print('   You have won! I have scissors.')
    print('   ---------------------------------------------------------------------------------------------------------')
    print('   Happy end!')
    time.sleep(3)
    quit()
elif text == 'scissors' and random1 == [2]:
    print('   You have won! I have paper.')
    print('   ---------------------------------------------------------------------------------------------------------')
    print('   Happy end!')
    time.sleep(3)
    quit()
elif text == 'scissors' and random1 == [1]:
    print('   I won! I have rock.')
    print('   ---------------------------------------------------------------------------------------------------------')
    print('   You lose!')
    time.sleep(3)
    quit()
elif text == 'paper' and random1 == [3]:
    print('   I won! I have scissors.')
    print('   ---------------------------------------------------------------------------------------------------------')
    print('   You lose!')
    time.sleep(3)
    quit()
elif text == 'paper' and random1 == [1]:
    print('   You have won! I have rock.')
    print('   ---------------------------------------------------------------------------------------------------------')
    print('   Happy end!')
    time.sleep(3)
    quit()
