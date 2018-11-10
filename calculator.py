'''
import math

def main():
	
	def calc(k):

		functions = ['sin', 'cos', 'tan', 'sqrt', 'pi']

		for i in functions:
			if i in k.lower():
				withmath = 'math.' + i 
				k = k.replace(i, withmath)


		try:
			k = eval(k)
		except ZeroDivisionError:
			print("Can't divide by 0")
			exit()
		except NameError:
			print("Invalid Input")
			exit()

		return k


	print("\nScientific Calculator\nEg: pi * sin(90) - sqrt(81)")

	k = input("\nWhat is")

	k = k.replace(' ', '')

	k = k.replace('^', '**')	

	k = k.replace('=', '')

	k = k.replace('?', '')

	k = k.replace('%', '/100')

	print("\n" + str(calc(k)))


if __name__ == '__main__':
	main()				
				
'''









import math

def main():
    
    def calc(k):

        functions = ['sin', 'cos', 'tan', 'sqrt', 'pi']    
        
        for i in functions:
            if i in k.lower():
                withmath = 'math.' + i
                k = k.replace(i, withmath)
        
        try:
            k = eval(k)
        except ZeroDivisionError:
            print ("Can't divide by 0")
            exit()
        except NameError:
            print ("Invalid input")
            exit()
        
        return k


    print ("\nScientific Calculator\nEg: pi * sin(90) - sqrt(81)")

    k = input("\nWhat is ")

    k = k.replace(' ', '')
    k = k.replace('^', '**')
    k = k.replace('=', '')
    k = k.replace('?', '')
    k = k.replace('%', '/100')

    print ("\n" + str(calc(k)))
    
if __name__ == "__main__":
    main()
