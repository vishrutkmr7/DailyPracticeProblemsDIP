# This problem was recently asked by Amazon:

# You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix.
# Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

def word_search(matrix, word):
    # Fill this in.
    #   transpose = [*zip(*matrix)]
    transpose = [list(i) for i in zip(*matrix)]

    for each in matrix:
        if word in ''.join(each):
            return True

    for each in transpose:
        if word in ''.join(each):
            return True

    return False
  
matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
print (word_search(matrix, 'FOAM'))
# True
