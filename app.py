# A simple program that uses loops, list objects, function , and conditional statements

# Pass in key word arguments into the function definition my_name
def my_name(first_name='Albert', last_name='Einstein', age=46):
    return 'Hello World, my name is: {} {}, and I am {} years old'.format(first_name,last_name, age)

print(my_name('Henry', 'Ford', 96))

my_list = [1,2,3,4,5, "python", 43.98, "fish", True]

my_list2 = ['grapes', 'oranges','Aegis', 100]

new_list = my_list + my_list2

for letter in new_list:
    print(new_list)
#check if the correct interger and string text is in the list
if 20 in new_list and "python" in new_list:
    print("That is correct, this is the best programming langauge in the world!")
else:
      print("Please chose the correct string or interger value!")




