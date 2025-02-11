def main():
    
    num1 = 78
    num2 = 88
    num3 = 95
    num4 = 100
    
    avg = calc_avg(num1, num2, num3, num4)
    print(avg)
    
    # args or params
def calc_avg(*args):
    
    '''
    Parameters
    *args : Type Description.
    
    Returns
    avg : Type Description.
    
    '''
    
    avg = sum(args)/len(args)
    return avg
    
main()