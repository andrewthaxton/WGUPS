# WGUPS
Delivery route optimization WGU project to demonstrate heuristic algorithms in Python

C950 Overview Document

A.	For this project I used the Greedy Algorithm modified from the example in the text to fit this scenario.

B.	1) Pseudocode explanation:

Take the parameters:

•	Delivery (nested list of packages in each delivery)

•	Num (Which delivery is being made 1, 2, or 3)

•	Current_Location (where the truck is)

Create a base case to break the loop in the algorithm

•	i.e. if there are no packages then return an empty list

Enter for loop for deliveries with packages

•	Set lowest_value to 50 (closest delivery location)

•	Set location to 0 (where the truck is headed next)

•	For I in Delivery:

o	If current location and the location of the next package is less than lowest value:

	Update lowest value and location

•	For I in Delivery:

o	If current distance is equal to lowest value:

	If delivery number 1:

•	Append package to truck 1

•	Append package address index to truck 1 index

•	Pop package form the Delivery list

•	Current location = location (update truck location)

•	Call algorithm with new list/location

	If delivery number 2:

•	Append package to truck 2

•	Append package address index to truck 2 index

•	Pop package form the Delivery list

•	Current location = location (update truck location)

•	Call algorithm with new list/location

	If delivery number 3:

•	Append package to truck 3

•	Append package address index to truck 3 index

•	Pop package form the Delivery list

•	Current location = location (update truck location)

•	Call algorithm with new list/location

2) I used Python 3.9 in PyCharm 2021.2.2 (Community Edition).

4) The major components of my project would be able to scale and adapt to fulfill the delivery of a greater number of packages. Though there would likely need to be a few minor changes to add additional trucks or new locations to accommodate the greater number of packages. The biggest constraint would be the actual loading of packages onto the trucks. I did this manually and just allowed my program to deliver the packages.

5) I believe that my software is fairly efficient with an overall time complexity of O(N^2) which scales well with the package limit for each truck being 16. The program is easy to maintain as the majority of the key components are the same just modified for different uses. This means you can refer to other instances of a function to debug should you have an error come up.

6) The primary strength of using a hash table is the speed. A hash table allows for quick lookups, insertions, and deletions. It allows me fast access to specific data elements. The primary weaknesses of a hash table are that they do not accept “null” as a key’s value and if we were to expand the program for more packages, we would likely see more collisions and we begin to lose our key advantage for using a hash table. This can be avoided by rehashing, but that would just mean more work for the programmer. (zyBooks)

C. See Program.

D. The data structure I used throughout the program is a list of lists. I chose to use this data structure for its flexibility and my familiarity with it. It is also extremely easy to implement with a hash table. Using the list, I was able to create a chaining hash table allowing me to quickly lookup, insert, delete, and quickly access specific data elements.

E. See Program

F. See program 

I.	1)  The primary advantages of using the greedy algorithm is its ability to find an optimized route for the delivery trucks quickly, as well as the ability to scale with various sizes of data sets.

2) Verified.

3) Another algorithm I could have used would be heuristic algorithms. This algorithm would start at the hub then search for the closest delivery route. Then the truck would be loaded, and those packages delivered. Then the algorithm would determine the next shortest route and so on until the packages were all delivered. This would determine sufficient route but not necessarily optimal. Another algorithm I could have used would be dynamic programming. This algorithm would have broken the problem down into smaller functions. It would have stored various paths along a route and searched for the shortest path. It would have cost the program in its space complexity but would have provided the optimal routes overall. (zyBooks)

J. If I had this project to do over again the main difference in my approach would have been to make package and truck objects as opposed to lists. This would have likely made the packages much more manageable. If I were to improve upon my code, I would likely add in some heuristics to do the loading of the trucks as opposed to me having to do it manually.

K. 1) a) The time needed to complete the lookup function for this program should scale linearly with the number of packages since it has a Big-O time complexity of O(N).

b) Due to my use of lists of lists the relation between the data structure space usage and the number of packages would be more quadratic.

c)Neither the number of trucks or cities would have a major impact on this program as far a space and time complexities are concerned.

2) A couple different options I had to use for data structures would have been a binary search tree or graphs. For a binary search tree, I could have sorted the packages and used the tree to quickly access them. As for the graphs I could have connected similar packages with vertices then traversed the graph until I filled a truck with its 16-package limit. (zyBooks)

Sources

Learn.zybooks.com. (n.d.). zyBooks. [online] Available at: learn.zybooks.com/zybook/WGUC950AY20182019 [Accessed Sept. 2021].
