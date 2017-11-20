#Erkin George
#Dr. Arias
#CSC 3310
#11/17/2017
import sys
filename = sys.argv[-1]
import re

stored_file = open(filename,"r")

print("Processing input file" + filename)
print("Result in file output.txt")

lines = stored_file.readlines()
#print (lines)
stored_file.close()

#keep track of number of tokens
token_count = 0

#Keep track of actual tokens
file_store = ""

#keep track of the type of data
what_ID = ''
#file to put output in
output_file = open("output.txt","w+")

#the tokens of the program
semicolon_token = "SEMICOLON"
print_token = "PRINT"
id_token = "ID"
plus_token = "PLUS"
minus_token = "MINUS"
times_token = "TIMES"
divide_token = "DIV"
power_token = "POWER"
assign_token = "ASSIGN"
int_token = "INT_CONST"
floating_token = "REAL_CONST"
string_token = "STRING"
left_token = "LPAREN"
right_token = "RPAREN"
quote_token = "QUOTE"

#Defining the rulers of the lexer
print_expr = re.compile('PRINT') 
ID = re.compile('[a-z0-9]+[(#|$|%)]') 
plus = re.compile('[+]') 
minus = re.compile('[-]') 
times = re.compile('[*]') 
divide = re.compile('[/]') 
power = re.compile('[\^]') 
assign = re.compile('[=]') 
int_expr = re.compile('[0-9]+') 
float_expr = re.compile('[0-9]*\.[0-9]+') 
left_par = re.compile('\\(') 
right_par = re.compile('\\)') 
semicolon = re.compile('[;]') 
string = re.compile('\"[a-zA-z ]{0,}\"')  
notwhite = re.compile('\S')

#variables to track edge cases
end_for_string = 0
lonley_semi = ''

#track types of id's
#type_ofval = ""
#find_int = ""

#For loop to read in the Prints that print in strings, as this is grammatically strict
for character in lines:
	end_for_string = 1
	found_string = string.findall(character)
	found_printing = print_expr.findall(character)
	if (found_string) and (found_printing):
		end_for_string = 0
		for chars in re.findall(string, character):
			output_file.write(print_token)
			output_file.write("\n")
			output_file.write(string_token)
			output_file.write(" ")
			output_file.write(chars)
			output_file.write("\n")

		#adds in the edge case semicolon
		lonley_semi = character.strip()[-1]
		if lonley_semi == ';':
			output_file.write(semicolon_token)
			output_file.write("\n")		

	#split up the inputted string into parsable arrays
	char = character.split()

	for item in char[:]:
		#Search objects to use regex with
		int_found = int_expr.search(item)
		float_found = float_expr.search(item)

	#checks to see what type of data is associated with the ID and sets it
	#not sure how to get this to work, out of time
	if (float_found) and (int_found):
		type_ofval = "REAL"
		find_int = floating_token
		break
	else:
		type_ofval = "INTEGER"
		find_int = int_token


	#this prevents you from going into code that is not towards the end
	if end_for_string:
		for string_object in char[:]:

				#More search objects that are defined within the array parameters
				found_plus = plus.search(string_object)
				found_minus = minus.search(string_object)
				found_times = times.search(string_object)
				found_divide = times.search(string_object)
				found_power = power.search(string_object)
				found_assign = assign.search(string_object)
				found_int_expr = int_expr.search(string_object)
				found_float = float_expr.search(string_object) 
				found_left = left_par.search(string_object)
				found_right = right_par.search(string_object)
				found_semi = semicolon.search(string_object)
				found_print = print_expr.match(string_object)
				found_ID = ID.search(string_object)

				#code to find assignment operators
				if found_plus:
					output_file.write(plus_token)
					output_file.write("\n")
				if found_minus:
					output_file.write(minus_token)
					output_file.write("\n")
				if found_times:
					output_file.write(times_token)
					output_file.write("\n")
				if found_divide:
					output_file.write(divide_token)
					output_file.write("\n")
				if found_power:
					output_file.write(power_token)
					output_file.write("\n")
				if found_assign:
					output_file.write(assign_token)
					output_file.write("\n")

				#code to print out numbers
				if found_float:
					output_file.write(floating_token)
					output_file.write(" ")
					output_file.write(string_object)
					output_file.write("\n")
				else:
					if found_int_expr:
						output_file.write(int_token)
						output_file.write(" ")
						output_file.write(string_object)
						output_file.write("\n")


				#code to print out left and right parentheses tokens
				if found_left:
					output_file.write(left_token)
					output_file.write("\n")
				if found_right:
					output_file.write(right_token)
					output_file.write("\n")

				#code to print out the semicolon token
				if found_semi:
					output_file.write(semicolon_token)
					output_file.write("\n")	

				#code to print out the print token
				if found_print:
					output_file.write(print_token)
					output_file.write("\n")

				#code to print out the ID token
				if found_ID:
					output_file.write(id_token)
					output_file.write(" ")
					shorter_item = string_object[:-1]
					output_file.write(shorter_item)
					output_file.write(" ")
					if found_float:
						output_file.write(type_ofval)
						output_file.write("\n")
					else:
						output_file.write(type_ofval)
						output_file.write("\n")
#close the file				
output_file.close()




