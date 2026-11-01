def getFirstAndLAstElement(list):
    if not list:
        print("The list is empty.")
    else:
        first_element = list[0]
        last_element = list[-1]
        print(f"The first element is: {first_element}")
        print(f"The last element is: {last_element}")

getFirstAndLAstElement([1, 2, 3, 4, 5])