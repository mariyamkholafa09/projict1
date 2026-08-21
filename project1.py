print ('welcome')
name= input('Enter your name : ',)
print("Hello", name)

print ('Would you solve this equation')
print ('5**2')
answer = int(input())
if answer == 25 :
    print('You are advanced to stage2 ')
    print("I have hands but I can't clap, I have a face but I can't smile, What am I ?")
    answer2 = input()
    if answer2 == "clock":
        print("correct")
    else:
        print("wrong")
else:
    print('Wrong answer')
