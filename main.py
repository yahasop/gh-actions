import argparse

parser = argparse.ArgumentParser(description='Program to print two values') #Parser initialization

parser.add_argument('name', help='Write name')
parser.add_argument('email', help='Write email')

args = parser.parse_args() #Store the argument in a variable

#Using a try and except bloc this tries to check if the file provided has an extension
print(f"The name is: {args.name}")
print(f"The email is: {args.email}")