import pprint

people = {}
people['Ford'] = { 'Nazwisko' : 'Ford Perfect',
                   'Płeć' : 'Mężczyzna',
                   'Zawód' :'Badacz',
                   'Planeta' : 'Betelgeza 7'}
people['Sarah'] = { 'Nazwisko' : 'Sarah Jessica Parker',
                   'Płeć' : 'Kobieta?',
                   'Zawód' :'...dla rodziny',
                   'Planeta' : 'Wenus'}
people['Kot'] = { 'Nazwisko' : 'Jarek',
                   'Płeć' : '????',
                   'Zawód' :'Złodziej',
                   'Planeta' : 'Ziemia'}

pprint.pprint(people)
