items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
i = 0

for each in items:
   items[i] = '<li>' + items[i] + '</li>\n'
   html_str = html_str + str(items[i])
   i += 1

html_str = html_str + '</ul>'
print(html_str)

#teacher solution:

#for item in items:
#    html_str += "<li>{}</li>\n".format(item)
#html_str += "</ul>"

#print(html_str)

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key in basket_items:
#if the key is in the list of fruits, add to fruit_count.
    if key in fruits:
        fruit_count += basket_items.get(key)
    else:
        not_fruit_count += basket_items.get(key)
#if the key is not in the list, then add to the not_fruit_count


print("The number of fruits in your basket is {}"
      " the rest of the items sum a total of {}".format(fruit_count, not_fruit_count))