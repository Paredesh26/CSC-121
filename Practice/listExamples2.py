'''
scores = [45, 89.5, 65, 100, 98.5]
names = ['Tom', 'Jessica', 'Sammy', 'Nancy', 'Josh']

print(f'{"Name":<10}{"Score"}')
print('-'*20)


for i in range(len(scores)):
    
    print(f'{names[i]:<10}{scores[i]}')
'''

import functions as fn

scores = {'Tom': 45, 'Jessica': 89.5, 'Sammy': 65, 'Nancy': 100, 'Josh': 98.5}

# scores. + tab = this will show up what methods you can use
# .get another method

# iterate over dictionary
print('Before adding 5 bonus points')


fn.display(scores)


'''
def display(dictionary):
    '''
'''
    Parameters
    ----------
    scores : TYPE
        DESCRIPTION.

    Returns
    -------
    None.'''

'''
print(f'{"Name":<12}{"Score"}')
for k, v in scores.items():
    # print(x, '\t', scores[x]')
    # print(k, '\t', v')
    scores[k] = v + 5
    print(f'{k:<12}{v}')
'''    
    

print('After adding 5 bonus points')

for k in scores:
    scores[k] = scores[k] + 5
 
    '''
# print
for k, v in scores.items():
    
    print(f'{k:<12}{v}')
    '''
    
print()
fn.display(scores)