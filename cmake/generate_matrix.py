import sys

if __name__ == '__main__':
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	matrix = None
	matrixes_out = [None, None, None]
	matrixes_out_multipliers = [0.5, 0.4, 0.3]
	
	# Read input
	with open(input_file, 'r') as file_input:
		matrix = file_input.read()
		matrix = [item.split() for item in matrix.split('\n')[:-1]]
	
	# Transform matrix
	line_length = len(matrix[0])

	for m in range(len(matrixes_out)):
		matrixes_out[m] = [[0 for i in range(line_length)] for j in range(len(matrix))]

	for i in range(len(matrix)):
		if len(matrix[i]) != line_length:
			raise ValueError("The picture provided is neither a square nor a rectangle")
		for j in range(line_length):
			matrix[i][j] = float(matrix[i][j])
			matrix[i][j] = 255.0 * matrix[i][j]
			for k in range(len(matrixes_out)):
				matrixes_out[k][i][j] = int(matrixes_out_multipliers[k] * matrix[i][j])

	# Write output
	print(matrixes_out)
	raise ValueError


sys.stdout.write(' '.join(sys.argv))
