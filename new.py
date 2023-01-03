arr = [3,4,6,3,29,10,55,34,6,4,5]

def linearSearch(myList, search_element):
  print(len(arr))
  for i in range(len(myList)): 
    print(i)       #Looping through an item 
    if myList[i] == search_element:    #Comparison for value 
      print(myList[i], "is present in array at index", i)
linearSearch(arr,10)

arr2 = [2, 3, 4, 4, 5, 6, 6, 10, 29, 34, 55]

def binarySearch(myList, element):
  first = 0
  last = len(myList) - 1
  index = -1

  while (first <= last) and (index == -1):
    mid = (first + last)//2
    print(mid,"mid")
    print(last,"last")
    print(first,"first")
    if myList[mid] == element:
      index = mid
      print(element," is present at index", index)

    else:
      if element < myList[mid]:
        last = mid - 1

      else:
        first = mid + 1 

binarySearch(arr2,3)