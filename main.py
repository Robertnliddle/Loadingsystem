"""
#input
#output (print)
#If statement
#Loop (while or for)

1. ask the user for a number of items to be shipped
2. set starting variables
   - package_weight (0kg)
   - number of packages sent (0)
   - number of the most empty package (0)
   - total weight sent (0)
3. in a loop:
   - ask user for the weight of the next item
   - if the weight of the item is 0, exit the loop
   - if the weight of the item is between 1 and 10:
     - add the item to the package (add to package_weight)
     - check if the package_weight exceeds 20kg
     - if yes :
       - remove the last item
       - send package
       - take new, empty package and add the last item to it
   - else: inform about the error, close the loop
4. print the summary of the packing system
"""

item_weight_min = 1
item_weight_max = 10
max_package_weight = 20

packages_sent = 0
weight_sent = 0
package_weight = 0
lightest_package = 20
index_most_empty_package = 0
item_weight = 0

correct_items = 0

items_to_be_shipped = int(input("What is the maximum of items to be shipped? "))

while correct_items < items_to_be_shipped:
    item_weight = int(input("Enter the weight of the next item: "))
    if item_weight == 0:
        print("Ending the packaging.")
        break
    elif item_weight < 1 or item_weight > 10:
        print("You must enter a weight between 1 and 10")
        continue
    else:
        correct_items += 1
        package_weight += item_weight
        if package_weight > 20:
            package_weight -= item_weight
            packages_sent += 1
            weight_sent += package_weight
            if package_weight < lightest_package:
                lightest_package = package_weight
                index_most_empty_package = packages_sent
                package_weight = item_weight

if package_weight > 0:
    packages_sent += 1
    weight_sent += package_weight
    if package_weight < lightest_package:
        lightest_package = package_weight
        index_most_empty_package = packages_sent

unused_capacity = packages_sent * 20 - weight_sent

print('-' * 50)

print("Summary of the packing system")
print(f"Packages sent: {packages_sent} packages")
print(f"Total weight of packages: {weight_sent}kg")
print(f"Total unused capacity: {unused_capacity}kg")
print(f"Package number that had the most unused kilograms: {index_most_empty_package}")
