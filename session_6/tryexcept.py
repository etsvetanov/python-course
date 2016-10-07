class MyError(ZeroDivisionError):
    pass


def divise_10(divisor):
    try:
        if divisor == 0:
            raise MyError
        else:
            return 10/divisor
    except:
        print('Make sure to catch the exception')
        raise


def try_to_divise():
    while True:
        divisor = input('Enter number: ')
        try:
            result = divise_10(int(divisor))
            print('Result is {}'.format(result))
        except ZeroDivisionError:
            print('Ne moje da se deli na 0')
        except ValueError:
            print('Tova ne e chislo')


try_to_divise()