dict1={}
def main():
    pi=3.14
    '''This program asks for the shape and its dimensions
       and returns back its area and also stores it in a dictionary as a workspace history'''
    yes=1
    while(yes==1):
        shape=input('Enter the shape, whose area you want to calculate: ')
        if shape=='circle':
            print('Enter the dimensions')
            r=float(input('Enter the radius: '))
            area=pi*(r**2)
            print(f'The area of the {shape} with radius {r} is {area}' )
            store(shape,area)
            ask=int(input('Enter any number except 1 if you want to stop calculating '))
            yes=ask
        elif shape=='rectangle':
            print('Enter the dimensions')
            l=float(input('Enter the length: '))
            b=float(input('Enter the breadth: '))
            area=l*b
            print(f'The area of the {shape} with length {l} and Breadth {b} is {area}' )
            store(shape,area)
            ask=int(input('Enter any number except 1 if you want to stop calculating '))
            yes=ask
        elif shape=='square':
            print('Enter the dimensions')
            a=float(input('Enter the side length: '))
            area=a**2
            print(f'The area of the {shape} with side {a} is {area}' )
            store(shape,area)
            ask=int(input('Enter any number except 1 if you want to stop calculating '))
            yes=ask
        elif shape=='triangle':
            typ=input('Is it equilateral ')
            if typ=='yes':
                a=float(input('enter the side : '))
                area=((3**(1/2))/(4))*(a**2)
                print(f'The area of the triangle with side {a} is {round(area,3)}')
                store(shape,area)
                ask=int(input('Enter any number except 1 if you want to stop calculating '))
                yes=ask
            else:
                print('Enter the dimensions')
                b=float(input('Enter the breadth: '))
                h=float(input('Enter the height: '))
                area=0.5*b*h
                print(f'The area of the {shape} with breadth {b} and height {h} is {area}' )
                store(shape,area)
                ask=int(input('Enter any number except 1 if you want to stop calculating '))
                yes=ask
        else:
            print(f'Sorry, I currently don\'t have information on {shape}' )
            continue
        
        req=input('Would you like to see your workspace , Press "yes" if you want to :  ')
        if req=='yes':
            print(f"{dict1}")
            continue
        else:
            continue

'''The code below stores the area of the shape after each iteration in the dictionary'''
        
def store(shape,area):
    Area=round(area,2)
    dict1.update([(shape,Area)]) 
    
    
    

if __name__ == "__main__":
    main()