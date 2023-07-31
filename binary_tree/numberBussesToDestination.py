"""_summary_

    The problem asks us to find the minimum number of buses that we need to change in order to get from the source to the target.
    We are given the input list routes, with routes[i] representing all of the stops that route i stops at.

    The most straightforward way to think about getting from the source stop to the target stop is to think about intermediate stops 
    along the way that connect them together, which makes graphs a natural choice since they represent relationships between objects. 
    In this case, we could perform a preprocessing step to create a graph of the (interconnected) stops in order to represent our data. 
    That would look a little something like the following:

    graph = {
        stop_1 : [stop_2, stop_14, stop_20],
        stop_2 : [stop_1],
        ...
    }
    This would have us going through all of the stops along each route i and connecting them to each other. Looking at the problem constraints,
    this step would be computationally expensive, as there can be as many as 10^5 total stops. Performing this quadratic operation
    (as it's a nested for-loop for each route within routes in order to connect the stops) doesn't seem very feasible. Furthermore, this representation
    of the data is very stop-centric instead of route-centric. After all, we are looking for 
    the minimum number of buses (i.e., routes) that we need to change and not the number of stops between the source and the target. With this representation,
    it's not clear how we make use of the route information. Therefore, we need to change our representation of the data.

    Instead of creating stop-stop connections, we can think about which routes are present at which stops. That would look like the following:

    graph = {
        stop_1: [route_1, route_4],
        stop_2: [route_3, route_9],
        ...
    }
    A stop may be part of multiple different routes, so we can start at our source and explore all the nodes along our starting route.
    If we find the target node, great! If not, we can check which other routes those stops are on and explore those routes as well, incrementing
    our count (num_changes) with each change of route. This gradual exploration from the source makes breadth-first search a natural choice.

    Code

    From a coding perspective, we can use a queue to which we add all connected nodes along with how many route changes we've made to get to that node.
    We also want to make sure we keep track of which routes we've already visited and which nodes we've seen so far, so we're not going through the
    effort of exploring those multiple times.


"""

from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        pass
        
        
        
if __name__ ==- "__main__":
    routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
    source = 15
    target = 12
    print(Solution().numBusesToDestination(routes, source, target))
    