
from listFunction import ListFunctions

def main():
    list_functions = ListFunctions()
    
    # Define some example lists
    example_lists = {
        "List1": [3, 7, 2, 8, 5],
        "List2": [10, 20, 30, 40, 50],
        "List3": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "List4": [5, 3, 8, 1, 2],
        "List5": [2.5, 3.5, 1.5, 4.5, 0.5]
    }

    # Demonstrate each function with the example lists
    for name, lst in example_lists.items():
        print(f"\n{name}: {lst}")
        print("Maximum value:", list_functions.findMax(lst))
        print("Minimum value:", list_functions.findMin(lst))
        print("Sum of elements:", list_functions.sum(lst))
        print("Average value:", list_functions.avg(lst))
        print("Median value:", list_functions.median(lst))

    # Creating additional lists using Python comprehension
    list1 = [x for x in range(10)]           
    list2 = [x**2 for x in range(10)]        
    list3 = [x for x in range(10) if x % 2 == 0]  
    list4 = [1.5 * x for x in range(10)]     

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
