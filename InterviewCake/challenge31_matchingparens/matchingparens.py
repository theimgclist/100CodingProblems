def get_closing_paren(sentence, opening_paren_index):
	open_nested_parens = 0
	position = opening_paren_index + 1
	for position in range(opening_paren_index + 1, len(sentence)):
		char = sentence[position]
		if char == '(':
			open_nested_parens += 1
		elif char == ')':
			if open_nested_parens == 0:
				return position
			else:
				open_nested_parens -= 1
	raise Exception("No closing parenthesis :(")
	
if __name__=="__main__":
	index = get_closing_paren("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.",10)
	print(index)