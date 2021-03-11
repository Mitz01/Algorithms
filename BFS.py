def main():  
    #fff
        #     0  1  2  3
        #  0  0  1  1  0
        #  1  0  0  1  0
        #  2  1  0  0  1
        #  3  0  0  0  1

        # The graph's adjacency matrix
        
    R = int(input())
    matrix = [] 
    for i in range(R):          #row entries 
        a =[] 
        for j in range(R):      #column entries 
            a.append(int(input())) 
        matrix.append(a) 
  

    visited = []            # The visited array 
    for x in range(R):      #initializing all values of visited to 0 
        visited.append(0) 
    


    queue = [0]             # Add the start node to the queue i.e. node 0


    visited[0] = 1          # Set the visited value of node 0 to visited


    node = queue.pop(0);    # Dequeue node 0
    print (node)
    while True:
        for x in range (0, len(visited)): # Check is route exists and that node isn't visited
            if matrix[node][x] == 1 and visited[x] == 0:
                visited[x] = 1; # Visiting node
                queue.append(x) # Enqueue element

        if len(queue) == 0:
            break;
        else:
            node = queue.pop(0)
            print (node)
            
if __name__ == "__main__":
    main()
