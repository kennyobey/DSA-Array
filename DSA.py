
# sampleArray = [4,5,6,7,8,8,9,7,4,3,2,2,4,5,6,7]

# def findBiggestNumber(sampleArray):
#     biggestNumber = sampleArray[0,5,5,6,6,3,5,6,]
#     for index in range(len(biggestNumber)):
#         if sampleArray[index] > biggestNumber:
#             biggestNumber = sampleArray[index]
#     print("Biggest number")
    
#     findBiggestNumber(sampleArray)
    
    
    
    
    #Initialize array     
arr = [95, 11, 7, 75, 56];     
     
#Initialize max with first element of array.    
max = arr[0];    
     
#Loop through the array    
for i in range(0, len(arr)):    
    #Compare elements of array with max    
   if(arr[i] > max):    
       max = arr[i];    
           
print("Largest element present in given array: " + str(max));   