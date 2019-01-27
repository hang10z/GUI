import pygame.mixer

#This is a gameshow "buzzer"
#
# Create a mixer object and initialize the pygame sound system
sounds = pygame.mixer
sounds.init()

# create a function that waits/checks for the sound to finish playing
def wait_finish(channel):
    while channel.get_busy():
        pass


# create the two sounds that will play, correct and wrong. Wav files should be in dir
correct_s = sounds.Sound('correct.wav')
wrong_s = sounds.Sound('wrong.wav')

# create the answers to the questions the host will press
number_asked = 0
number_correct = 0
number_wrong = 0

prompt = 'Press 1 for Correct, 2 for Wrong , or 0 to Quit'

choice = input(prompt)
while choice != '0':
    if choice == '1':
        number_asked = number_asked + 1
        number_correct = number_correct + 1
        wait_finish(correct_s.play())
    if choice == '2':
        number_asked = number_asked + 1
        number_wrong = number_wrong + 1
        wait_finish(wrong_s.play())
    choice = input(prompt)

print('You asked ' + str(number_asked) + ' Questions')
print(str(number_correct) + ' were correctly answered ')
print(str(number_wrong) + ' were answered incorrectly')