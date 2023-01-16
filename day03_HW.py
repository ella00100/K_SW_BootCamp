#prob 5.4 & 5.5
salutation = 'Mr.'
name = 'jake'
product = 'chocolate'
verbed = 'delayed'
room  = 'house'
animals = 'animals'
amount = '10'
percent = '30'
spokesman = 'Ella'
job_title = 'Marketing Manager'

letter = print('  Dear {} {},\n\n'.format(salutation,name),
               ' Thank you for your letter. We are sorry that our {} {} in your {}.'.format(product,verbed,room),
               'Please note that it should never be used in a {}, especially near any {}.\n\n'.format(room,animals),
               ' Send us your receipt and {} for shipping and handling'.format(amount),
               'We will send you another {} that, in out tests, is {}% less likely to have {}\n\n'.format(product,percent,verbed),
               ' Thank you for your support.\n  Sincerely,\n  {}\n  {}'.format(spokesman,job_title)
)