p1=input()
p2=input()
def game(p1,p2):
    if (p1 == p2):
        return('no result')
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'scissors') and (p1 == 'paper' and p2 == 'rock'):
        return('p1 wins')
    else:
        retrn('p2 wins')
x=game('rock','scissors')
print(x)