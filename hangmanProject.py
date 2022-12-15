#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string
words_list = [
    'wares',
    'soup',
    'mount',
    'extend',
    'brown',
    'expert',
    'tired',
    'humidity',
    'backpack',
    'crust',
    'dent',
    'market',
    'knock',
    'smite',
    'windy',
    'coin',
    'throw',
    'silence',
    'bluff',
    'downfall',
    'climb',
    'lying',
    'weaver',
    'snob',
    'kickoff',
    'match',
    'quaker',
    'foreman',
    'excite',
    'thinking',
    'mend',
    'allergen',
    'pruning',
    'coat',
    'emerald',
    'coherent',
    'manic',
    'multiple',
    'square',
    'funded',
    'funnel',
    'sailing',
    'dream',
    'mutation',
    'strict',
    'mystic',
    'film',
    'guide',
    'strain',
    'bishop',
    'settle',
    'plateau',
    'emigrate',
    'marching',
    'optimal',
    'medley',
    'endanger',
    'wick',
    'condone',
    'schema',
    'rage',
    'figure',
    'plague',
    'aloof',
    'there',
    'reusable',
    'refinery',
    'suffer',
    'affirm',
    'captive',
    'flipping',
    'prolong',
    'main',
    'coral',
    'dinner',
    'rabbit',
    'chill',
    'seed',
    'born',
    'shampoo',
    'italian',
    'giggle',
    'roost',
    'palm',
    'globe',
    'wise',
    'grandson',
    'running',
    'sunlight',
    'spending',
    'crunch',
    'tangle',
    'forego',
    'tailor',
    'divinity',
    'probe',
    'bearded',
    'premium',
    'featured',
    'serve',
    'borrower',
    'examine',
    'legal',
    'outlive',
    'unnamed',
    'unending',
    'snow',
    'whisper',
    'bundle',
    'bracket',
    'deny',
    'blurred',
    'pentagon',
    'reformed',
    'polarity',
    'jumping',
    'gain',
    'laundry',
    'hobble',
    'culture',
    'whittle',
    'docket',
    'mayhem',
    'build',
    'peel',
    'board',
    'keen',
    'glorious',
    'singular',
    'cavalry',
    'present',
    'cold',
    'hook',
    'salted',
    'just',
    'dumpling',
    'glimmer',
    'drowning',
    'admiral',
    'sketch',
    'subject',
    'upright',
    'sunshine',
    'slide',
    'calamity',
    'gurney',
    'adult',
    'adore',
    'weld',
    'masking',
    'print',
    'wishful',
    'foyer',
    'tofu',
    'machete',
    'diced',
    'behemoth',
    'rout',
    'midwife',
    'neglect',
    'mass',
    'game',
    'stocking',
    'folly',
    'action',
    'bubbling',
    'scented',
    'sprinter',
    'bingo',
    'egyptian',
    'comedy',
    'rung',
    'outdated',
    'radical',
    'escalate',
    'mutter',
    'desert',
    'memento',
    'kayak',
    'talon',
    'portion',
    'affirm',
    'dashing',
    'fare',
    'battle',
    'pupil',
    'rite',
    'smash',
    'true',
    'entrance',
    'counting',
    'peruse',
    'dioxide',
    'hermit',
    'carving',
    'backyard',
    'homeless',
    'medley',
    'packet',
    'tickle',
    'coming',
    'leave',
    'swing',
    'thicket',
    'reserve',
    'murder',
    'costly',
    'corduroy',
    'bump',
    'oncology',
    'swatch',
    'rundown',
    'steal',
    'teller',
    'cable',
    'oily',
    'official',
    'abyss',
    'schism',
    'failing',
    'guru',
    'trim',
    'alfalfa',
    'doubt',
    'booming',
    'bruised',
    'playful',
    'kicker',
    'jockey',
    'handmade',
    'landfall',
    'rhythm',
    'keep',
    'reassure',
    'garland',
    'sauna',
    'idiom',
    'fluent',
    'lope',
    'gland',
    'amend',
    'fashion',
    'treaty',
    'standing',
    'current',
    'sharpen',
    'cinder',
    'idealist',
    'festive',
    'frame',
    'molten',
    'sill',
    'glisten',
    'fearful',
    'basement',
    'minutia',
    'coin',
    'stick',
    'featured',
    'soot',
    'static',
    'crazed',
    'upset',
    'robotics',
    'dwarf',
    'shield',
    'butler',
    'stitch',
    'stub',
    'sabotage',
    'parlor',
    'prompt',
    'heady',
    'horn',
    'bygone',
    'rework',
    'painful',
    'composer',
    'glance',
    'acquit',
    'eagle',
    'solvent',
    'backbone',
    'smart',
    'atlas',
    'leap',
    'danger',
    'bruise',
    'seminar',
    'tinge',
    'trip',
    'narrow',
    'while',
    'jaguar',
    'seminary',
    'command',
    'cassette',
    'draw',
    'anchovy',
    'scream',
    'blush',
    'organic',
    'applause',
    'parallel',
    'trolley',
    'pathos',
    'origin',
    'hang',
    'pungent',
    'angular',
    'stubble',
    'painted',
    'forward',
    'saddle',
    'muddy',
    'orchid',
    'prudence',
    'disprove',
    'yiddish',
    'lobbying',
    'neuron',
    'tumor',
    'haitian',
    'swift',
    'mantel',
    'wardrobe',
    'consist',
    'storied',
    'extreme',
    'payback',
    'control',
    'dummy',
    'influx',
    'realtor',
    'detach',
    'flake',
    'consign',
    'adjunct',
    'stylized',
    'weep',
    'prepare',
    'pioneer',
    'tail',
    'platoon',
    'exercise',
    'dummy',
    'clap',
    'actor',
    'spark',
    'dope',
    'phrase',
    'welsh',
    'wall',
    'whine',
    'fickle',
    'wrong',
    'stamina',
    'dazed',
    'cramp',
    'filet',
    'foresee',
    'seller',
    'award',
    'mare',
    'uncover',
    'drowning',
    'ease',
    'buttery',
    'luxury',
    'bigotry',
    'muddy',
    'photon',
    'snow',
    'oppress',
    'blessed',
    'call',
    'stain',
    'amber',
    'rental',
    'nominee',
    'township',
    'adhesive',
    'lengthy',
    'swarm',
    'court',
    'baguette',
    'leper',
    'vital',
    'push',
    'digger',
    'setback',
    'accused',
    'taker',
    'genie',
    'reverse',
    'fake',
    'widowed',
    'renewed',
    'goodness',
    'featured',
    'curse',
    'shocked',
    'shove',
    'marked',
    'interact',
    'mane',
    'hawk',
    'kidnap',
    'noble',
    'proton',
    'effort',
    'patriot',
    'showcase',
    'parish',
    'mosaic',
    'coil',
    'aide',
    'breeder',
    'concoct',
    'pathway',
    'hearing',
    'bayou',
    'regimen',
    'drain',
    'bereft',
    'matte',
    'bill',
    'medal',
    'prickly',
    'sarcasm',
    'stuffy',
    'allege',
    'monopoly',
    'lighter',
    'repair',
    'worship',
    'vent',
    'hybrid',
    'buffet',
    'lively']
def cloth(words_list):
    word = random.choice(words_list)
    return word.upper()


# In[2]:


def display_hangman(chances):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]


# In[3]:


def hangman():
    word = cloth(words_list)
    print(word)
    guess_word = set(word)  #word selected from  list randomly
    guessed_letters= set()  #created empty set to store guessed letters and display to user
    chances =6
    while len(guess_word)>0 and chances>0:
        word_list=[]
        print('you have used these letters already:',' '.join(guessed_letters)) #print shows which letters are already used by user
        for letter in word:
            if letter in guessed_letters:
                word_list.append(letter)
            else:
                word_list.append('_')
        print('current word:', ' '.join(word_list))   #print shows route to the user like how many letters are left and what he guessed
        

        user_guess=input("guess a letter or word:").upper() #takes input from the user
        if user_guess==word:
            print('your guess was right: {}'.format(word))  #prints if user can guess correct word without letters
            break
            
        if len(user_guess)==1 and user_guess in set(string.ascii_letters)-guessed_letters: #checks whether user entered letter or not

            guessed_letters.add(user_guess) 
            if user_guess in guess_word:       #if letter guessed is in word which is selected from list then it removes that letter from word
                guess_word.remove(user_guess)
            else:
                chances= chances-1              #if letter guessed is not in word then chance will decrease by one
                print('remainning chances are: {}'.format(chances))
                print(display_hangman(chances   #display the stage of hangman
        elif user_guess in guessed_letters:
            print("you have already guessed this letter")
            chances=chances-1
            print(display_hangman(chances))
        else:
            print('inavlid entry')
    if chances==0:
         print('you are dead')
    else:
         print('you won')
            
       
        
    
    
    


# In[ ]:




