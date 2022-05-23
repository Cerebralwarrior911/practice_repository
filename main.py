def abc():

    try:
        if int(val) > 2:
            print("value is greater than two")
        else:
            print("value is less than two")
    except:
        print("something is wrong!")


if __name__ == '__main__':
    print("Enter a value:")
    val = input()
    abc()

