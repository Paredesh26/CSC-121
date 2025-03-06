def display(dictionary):
    '''
    Parameters
    ----------
    scores : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
print(f'{"Name":<12}{"Score"}')
for k, v in scores.items():
    # print(x, '\t', scores[x]')
    # print(k, '\t', v')
    scores[k] = v + 5
    print(f'{k:<12}{v}')