# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

def make_squares(arr):

  right, left = len(arr) - 1, 0
  largestSquare = len(arr) - 1
  squares = [0] * len(arr)

  while right >= left:
    rSquare = arr[right] * arr[right]
    lSquare = arr[left] * arr[left]

    if rSquare > lSquare:
      squares[largestSquare] = rSquare
      right -= 1
    else:
      squares[largestSquare] = lSquare
      left += 1
    largestSquare -= 1
  return squares
