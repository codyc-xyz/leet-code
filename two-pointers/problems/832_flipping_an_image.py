# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1,1,0] horizontally results in [0,1,1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0,1,1] results in [1,0,0].

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        c = len(image) 
        for row in image:
            for i in range((len(image) + 1) // 2):
                tmp = row[i]
                row[i] = 1 - row[c - 1 - i]
                row[c - 1 - i] = 1 - tmp
        return image