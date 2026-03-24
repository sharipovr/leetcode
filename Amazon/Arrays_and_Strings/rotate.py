class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) # get the size of the matrix
        # Loop through each layer, from outermost to innermost
        for layer in range(n // 2):
            first = layer   # first index of the layer
            last = n - 1 - layer    # last index of the layer
            # Loop through each element if the current layer
            for i in range(first, last):
                offset = i - first  # calculate offset within the layer
                # Sae the top element
                top = matrix[first][i]
                # Move left element to top
                matrix[first][i] = matrix[last - offset][first]
                # Move bottom element to left
                matrix[last - offset][first] = matrix[last][last - offset]
                # Move right element to bottom
                matrix[last][last-offset] = matrix[i][last]
                # Move top element to right
                matrix[i][last] = top

        