num_items = 0
total_price_float = 0.0
current_item = 1
lowest_item = 0.0


#check if the user has inputted 0
while current_item != 0:

    current_item = float(input())

    #again making sure the user hasnt inputting 0 before adding it to our total

    if current_item != 0:

        num_items += 1
        total_price_float += current_item

        #calculate the lowest item
        if current_item < lowest_item or lowest_item == 0.0:
            
            lowest_item = current_item
    

#print the results

print("Number of items:", num_items)
print("Total price:", round(total_price_float, 1))
if num_items != 0:
    print("Lowest price:", round(lowest_item, 1))