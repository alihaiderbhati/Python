import random

while True:
    print("--------------- **************** -----------------\n")
    print('Enter "g" to generate Password and "q" to close the script')
    generate = input('Enter your query :- ')
    print("--------------- **************** -----------------\n")
    if generate == 'g':
        numbers = [0,1,2,3,4,5,6,7,8,9]
        largealphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        smallalphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        specialcharacters = ['!','@','#','$','%','^','&','*','(',')','<','>','?',':',',','.']


        print('Strong Password Generator ')

        password = f'{largealphabets[random.randint(0,len(largealphabets)-1)]}{numbers[random.randint(0,len(numbers)-1)]}{specialcharacters[random.randint(0,len(specialcharacters)-1)]}{smallalphabets[random.randint(0,len(smallalphabets)-1)]}{largealphabets[random.randint(0,len(largealphabets)-1)]}{specialcharacters[random.randint(0,len(specialcharacters)-1)]}{smallalphabets[random.randint(0,len(smallalphabets)-1)]}{numbers[random.randint(0,len(numbers)-1)]}'

        print(f"Your Password is \n {password}")
        print("--------------- **************** -----------------\n")
    elif generate == 'q':
        quit()
    else:
        pass
