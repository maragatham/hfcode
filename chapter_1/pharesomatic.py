import random
verbs = ['Leverge','Sync', 'Target', 'Gamify', 'offline',
         'Croed-sourced', '24/7', 'Lean-in', '30,000 foot']
adjectives = ['A/B Tested', 'Freemium', 'Hyperlocal', 'Siloed',
              'B-to-B', 'oriented', 'Cloud-based', 'API-based']
nouns = ['Early adopter', 'Low-Hanging fruit', 'Piprline', 'Splash page',
         'Productivity', 'Process', 'tipping point', 'Paradigm']

verb = random.choice(verbs)
adjective = random.choice(adjectives )
noun = random.choice(nouns)

phrase = verb + ' ' +adjective + ' ' + noun

print(phrase)