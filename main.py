class Solution:
    def getRange(self, arr, target):
    first = self.binarySearch(arr, 0, len(arr) -1, target, True)
    last = self.binarySearch(arr, 0, len(arr) -1, target, False)
    return [first, last]
  def binarySearch(self, arr, low, high, target, findFirst):
      if high < low:
          return -1
        mid = low + (high - low) / 2
        if findFirst:
            if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                return mid
            if target > arr[mid]:
                return self.binarySearch(arr, mid + 1, high, target, findFirst)

                else:
                return self.binarySearch(arr, low, mid - 1, target, findFirst)
                

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 15,]
    x = 0
    print Solution().getRange(arr, 9)