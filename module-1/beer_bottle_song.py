def beer_bottle_song(initial_number_of_beer_bottles):
    
    # Validate input
    if initial_number_of_beer_bottles < 1:
        print("You need at least one beer bottle to start the song!")
        return
    
    # countdown loop for the song
    for bottles in range(initial_number_of_beer_bottles, 0, -1):
        
        # use correct plural when referring to bottles that are more than one. 
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            
            # if only one bottle left after taking one down use the singular for bottle.
            if bottles == 2:
                print("Take one down and pass it around, 1 bottle of beer on the wall.")
            # otherwise use the plural form bottles.
            else:
                print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.")
                
        elif bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.")
            print("No more bottles of beer on the wall, no more bottles of beer.")
            # add decoration to show end of verse
            print("_________________________________________________________________________")
            
# Add main function to allow user to input bottles
def main():
    
    # welcome user and get input
    print("This is 100 Bottles of Beer on the Wall")
    print("Welcome, enjoy the song!")
    
    # ask user for number of bottles
    try:
        user_input = input(" How many beer bottles do you want to buy on the wall? (Enter a positive number): ")
        # Validate user input
        num_bottles = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a positive number.")
        return
    except KeyboardInterrupt:
        print("\nProcess interrupted. Do not forget to restock your beer.")
        return
    
    if num_bottles <= 0:
        print("Number of beer has to be a positive number. Please enter number greater than zero.")
        return

    print("Here we go! We have", num_bottles, "bottles of beer on the wall!")
    print("_________________________________________________________________________")
    
    # call the beer bottle song function
    beer_bottle_song(num_bottles)
    
    # remind user to buy more beer
    print("Ohh no! We are out of beer. Time to buy more beer!!")

if __name__ == "__main__":
    main()
