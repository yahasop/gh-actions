import argparse

parser = argparse.ArgumentParser(description='Program to print two values') #Parser initialization

parser.add_argument('name', help='Write name')
parser.add_argument('email', help='Write email')

args = parser.parse_args() #Store the parsed arguments in a variable

# Print the values
print(f"The name is: {args.name}")
print(f"The email is: {args.email}")