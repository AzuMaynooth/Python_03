'''

In this exercise, you are tasked to create a Python program that simulates
a package loading system. Each package can carry a maximum of 20 kg of goods.
Items are added to the package with weights ranging from 1 to 10 kg.
 If adding an item to the package would exceed the 20 kg limit, the package should
 be sent, and the current item should start a new package.
 If an item with a weight of 0 is given, the program should terminate.

1. Write a program that prompts the user for the maximum number of items to be shipped.
2. The program should allow the user to enter the weight of each item, one by one.
3. If adding an item would increase the total weight of the current
package above 20 kg, mark the current package as sent and start a new
package with the current item.
4. If an item with a weight of 0 kg is given, the program should
terminate as if the maximum number of items has been reached.
5. At the end of the program, display the following information:

      Number of packages sent
      Total weight of packages sent
      Total 'unused' capacity (non-optimal packaging). This is calculated as
       the number of packages sent multiplied by 20 kg, minus the total weight
       of packages sent.
      The package number that had the most 'unused' capacity and the amount
       of 'unused' capacity in that package.


Hints:

- Use a loop to continuously prompt the user for item weights until the maximum
 number of items has been reached or an item with a weight of 0 kg is given.
- Keep track of the current package's total weight and the number of packages sent.
- Remember to handle cases where the weight of an item is outside the acceptable
range (1 to 10 kg, unless it's 0).
- Handle user inputs that are not as expected (for example, if the user enters a
string instead of a number for the item's weight). The program should not crash
in these cases, but instead, it should display an appropriate error message.



'''

n_items = None

while n_items is None:
    try:
        n_items = abs(int(input("Add number of items to be sent: ")))
    except ValueError:
        print("Wrong item weight. Please add numeric value.")


packages = [0]
item_index = 0
packages_index = 0
package_weight = 0

while item_index < n_items:

    try:

        item_weight = abs(round(float(input("Please add item weight: ")), 2))

        if item_weight == 0:
            print("Not more items to send\n")
            item_index = n_items

        elif 1 <= item_weight <= 10:

            if package_weight + item_weight <= 20:
                print("Item added to current package")
                package_weight = package_weight + item_weight
                packages[packages_index] = package_weight

            else:

                print("\n"
                      "-------------------------------------------------------------------------------------\n"
                      "Previous package has been sent\n"
                      "-------------------------------------------------------------------------------------\n"
                      "Initializing new package")
                packages.append(0)
                packages_index += 1
                package_weight = item_weight
                packages[packages_index] = package_weight
        else:
            print("Your item weight is larger than 10kg.\n"
                  "It can't be sent")

        item_index += 1

    except ValueError:
        print("Wrong item weight. Please add numeric value.")


print("\n--------------------------------------------------- Printing sent item information ---------------------------------------------------------------------------------------------\n")

total_weight = sum(packages)
max_weight = len(packages) * 20
unused_capacity = max_weight - total_weight

lighter_package_weight = min(packages)
lighter_package_index = packages.index(lighter_package_weight)


print('Number of packages sent: {0}. \n'
        'Total weight of packages sent: {1}kg \n'
        'Total unused capacity: {2}kg \n'
        'The lighter package number: {3} \n'
        'Unused capacity from lighter package: {4}kg'.format(len(packages), total_weight, unused_capacity,
                                                             lighter_package_index + 1, 20 - lighter_package_weight))