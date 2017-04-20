import math
from time import sleep


def calculate_rubenstein_ne(pie_decay__multiple_inverted=2, number_of_rounds=4):
    print('')
    print('N.E. for pie decay of (1/%d) ' % pie_decay__multiple_inverted + 'and (%d) rounds' % number_of_rounds)
    sleep(2)
    print('')
    print('PAYOFFS TO PLAYERS:')
    print('')
    play1 = []
    play2 = []
    for i in range(number_of_rounds):
        totalrejects = i
        p1a = 0
        p2a = 0
        for r in reversed(range(totalrejects+1)):
            try:
                pie = 1/math.pow(pie_decay__multiple_inverted,r)
            except OverflowError:
                raise ValueError('number of rounds too big.')
            p1r = p1a
            p2r = p2a
            if not r % 2 == 0:   # if returns a remainder it is odd
                x_accept = pie - p1r
                p1a = pie - x_accept
                p2a = x_accept
            else:   # EVEN NUMBER OF rejections
                x_accept = pie - p2r
                p1a = x_accept
                p2a = pie - x_accept

        play2.append(str(p2a))
        play1.append(str(p1a))
        print("round: " + str(totalrejects) + " P1: " + str(p1a) + " P2: " + str((p2a)))
        sleep(0.01)
    print('')
    print('    (' + str(play1[-1]) + ',' + str(play2[-1]) + ")")

def main():
    print('')
    print('Rubenstein Bargaining Game!')
    print('')
    print('In the Rubenstein model, you have a decaying pie. The pie decays each round. The pie may decay, for example, by 50% (1/2).')
    print('')
    print('The denominator of a rate of decay of 1/2 is 2.')
    print('')
    try:
        inverted_rate_of_decay = int(raw_input('Enter the denominator of your rate of decay: '))
        print('')
        number_of_rounds = int(raw_input('Enter the number of rounds: '))
        print('')
    except:
        raise ValueError('both must be integers')
    calculate_rubenstein_ne(inverted_rate_of_decay,number_of_rounds)
	
if __name__ == '__main__':
    main()