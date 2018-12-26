###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time


#================================
# Part A: Transporting Space Cows
#================================




# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    
#    open file in read mode
    file = open(filename, "r")
    
#    create dictionary for cows as key with weight as vals
    cow_dict = {}
    
#    loop over lines in file
    for i in file:
#        separate cow from weight
        a, b = i.split(",")
#        convert weight to integer
        c = int(b)
#        add cow as key to weight as val to the dictionary
        cow_dict[a] = c
        
    return cow_dict
    
    

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

#    create list with cows from heaviest to least heavy
    cowsCopy = sorted(cows, key=cows.get, reverse = True)

#    create global list that will contain lists of which cows there are on each transport   
    transport_list = []
    
#    as long as there are remaining cows, iterate over this loop (keep shipping cows)
    while len(cowsCopy) > 0:
#        register the total weight and cow names of a transport
        batch_weight = 0
        batch_list = []
#        iterate over the cows that remain to be shipped, starting with heaviest
        for cow in cowsCopy:
#            only select cow if its weight + that of other cows in transport is under the max weight limit
            if cows[cow] + batch_weight < limit:
#                if cow selected, add its weight and name to weight list and name list
                batch_weight += cows[cow]
                batch_list.append(cow)
#                remove the cow name from the list that contains remaining cow names
                cowsCopy.remove(cow)
#        add transport list to the list that contain all transports
        transport_list.append(batch_list)
        
    return transport_list
                

    

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
#    make list of cows sorted by heaviest first
    cowsCopy = sorted(cows, key=cows.get, reverse = True)
    
#    create list of all partitions that will be possible
    possible_trips = []

#    iterate over all possible partitions
    for partition in get_partitions(cowsCopy):
#        as long as possibility_trip is not changed, trip is possible
        possibility_trip = True
#        iterate over lists that are generated in a partition
        for transport_list in partition:
#            set start weight per transport to zero
            transport_weight = 0
#            calculate weight of all cows that are in a transport
            for cow in transport_list:
                transport_weight += cows[cow]
#            if the weight per transport exceeds the limit, set trip_possibility to false and quit loop
            if transport_weight > limit:
                possibility_trip = False
                break
#            if weight per transport does not exceed limit, continue testing other transports in partition
            else:
                continue 
#        if the possibility_trip is true it means all transports within the partition fall within limit
        if possibility_trip is True:
#            so then add this partition to the set of possible partitions
            possible_trips.append(partition)
            
                    
#    sort list of possible partitions so the one with least amount of trips is listed as first element
    sorted_trips = sorted(possible_trips, key = len)

#    select best partition
    best_candidate = sorted_trips[0]       


    return best_candidate

        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    
#    define file name
    cow_file = 'ps1_cow_data.txt'
#    feed file to function to make it a dictionary type
    cows = load_cows(cow_file)
    
#    measure time and run the greedy algorithm
    start = time.time()
    run_greedy = greedy_cow_transport(cows)
    end = time.time()
    greedy_time = end - start

#    print the results of greedy algorithm and the run time
    print('Best transports predicted by greedy algorithm: ', run_greedy, ' in ', greedy_time, ' seconds')

#    measure time and run the brute force algorithm
    start = time.time()
    run_brute_force = brute_force_cow_transport(cows)
    end = time.time()
    brute_force_time = end - start
    
#    print the results of brute force algorithm and the run time
    print('Best transports predicted by brute force algorithm: ', run_brute_force, ' in ', brute_force_time, ' seconds')
       
    
    
#To run the code:
if __name__ == '__main__':
    compare_cow_transport_algorithms()


