class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            image[row] = image[row][::-1]
            for column in range(len(image[row])):
                image[row][column] = 1 - image[row][column]
        return image
