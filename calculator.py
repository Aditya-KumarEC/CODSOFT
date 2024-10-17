def main():#define  list to store tasks
    calculator =[]
    #Display menu for user actions
    while True:
        print("\n=====YOUR ASSISTANT=====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multipication")
        print("4. Division")

        option=input("enter the no between 1-4 ")
        if option =='1':
            print()
            n=int(input("enter how many no. have to count : "))
            s=0
            for i in range(n):
                a=int(input("enter no."))
                s=s+int(a)
            print()
            print("-----Answer is :",s)

        elif option =='2' :
            n=int(input("enter how many no. have to count : "))
            s=0
            print()
            print("first no without negative sign and other with negative sign")
            print("if the number is negative then not need to add sign")
            for i in range(n):
                a=int(input("enter no."))
                s=a+s
            print()
            print("-----Answer is :",s)

        elif option =='3':
            n=int(input("enter how many no. have to count : "))
            s=1
            print()
            for i in range(n):
                a=input("enter no.")
                s=int(a)*int(s)
            print()
            print("-----Answer is :",s)

        elif option =='4':
            a=int(input("enter the Dividend"))
            b=int(input("enetr the Divisor"))
            print()
            print("-----Answer is :" ,a/b)


if __name__=="__main__":
    main()
            