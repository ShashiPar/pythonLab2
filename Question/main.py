
from listFunction import ListFunctions

def main():
    list_functions = ListFunctions()
    
    my_list = [3, 7, 2, 8, 5]
    
    max_value = list_functions.findMax(my_list)
    min_value = list_functions.findMin(my_list)
    total_sum = list_functions.sum(my_list)
    average = list_functions.avg(my_list)
    median_value = list_functions.median(my_list)
    
    print("Maximum:", max_value)
    print("Minimum:", min_value)
    print("Sum:", total_sum)
    print("Average:", average)
    print("Median:", median_value)

    # Creating lists using Python comprehension
    list1 = [x for x in range(10)]           # List of numbers from 0 to 9
    list2 = [x**2 for x in range(10)]        # List of squares of numbers from 0 to 9
    list3 = [x for x in range(10) if x % 2 == 0]  # List of even numbers from 0 to 9
    list4 = [1.5 * x for x in range(10)]     # List of multiples of 1.5 from 0 to 13.5
    
    print("\nList1:", list1)
    print("Maximum value in List1:", list_functions.findMax(list1))
    print("Minimum value in List1:", list_functions.findMin(list1))
    print("Sum of elements in List1:", list_functions.sum(list1))
    print("Average of List1:", list_functions.avg(list1))
    print("Median of List1:", list_functions.median(list1))
    
    print("\nList2:", list2)
    print("Maximum value in List2:", list_functions.findMax(list2))
    print("Minimum value in List2:", list_functions.findMin(list2))
    print("Sum of elements in List2:", list_functions.sum(list2))
    print("Average of List2:", list_functions.avg(list2))
    print("Median of List2:", list_functions.median(list2))
    
    print("\nList3:", list3)
    print("Maximum value in List3:", list_functions.findMax(list3))
    print("Minimum value in List3:", list_functions.findMin(list3))
    print("Sum of elements in List3:", list_functions.sum(list3))
    print("Average of List3:", list_functions.avg(list3))
    print("Median of List3:", list_functions.median(list3))
    
    print("\nList4:", list4)
    print("Maximum value in List4:", list_functions.findMax(list4))
    print("Minimum value in List4:", list_functions.findMin(list4))
    print("Sum of elements in List4:", list_functions.sum(list4))
    print("Average of List4:", list_functions.avg(list4))
    print("Median of List4:", list_functions.median(list4))

if __name__ == "__main__":
    main()
