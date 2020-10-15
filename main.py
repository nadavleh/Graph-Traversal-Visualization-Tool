import pygame 
import math
from queue import PriorityQueue

WIDTH = HEIGHT = 800 #400 is another option
win = pygame.display.set_mode((WIDTH,HEIGHT))
  

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (128, 0, 128)
ORANGE = (250, 165, 0)
TURQUOISE = (88, 237, 247)



class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width ########### TODO: is it actually row * width and not col * width ??
        self.y = col *width ## width is the width of each cube i.e. WIDTH/number_of_cols that way we know where each cube starts
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows        
    def get_pos(self):
        return self.row, self.col    
    def is_closed(self):
        return self.color == RED
    def is_open(self):
        return self.color == GREEN
    def is_barrier(self):
        return self.color == BLACK
    def is_end(self):
        return self.color == PURPLE    
    def reset(self):
        self.color = WHITE
    def make_closed(self):
        self.color = RED
    def make_open(self):
        self.color = GREEN
    def make_barrier(self):
        self.color = BLACK
    def make_end(self):
        self.color = TURQUOISE
    def make_path(self):
        self.color = PURPLE
    def make_start(self):
        self.color = ORANGE
    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))   
    def update_neighbors(self,grid):
        self.neighbors = []
        # append to the adjacancy list of the node\spot the square below it, unless its a barrier
        if self.row < self.total_rows -1 and not grid[self.row + 1][self.col].is_barrier():           # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
            
        # append to the adjacancy list of the node\spot the square above it, unless its a barrier
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():                            # UP
            self.neighbors.append(grid[self.row - 1][self.col])
            
        # append to the adjacancy list of the node\spot the square on the right of it, unless its a barrier
        if self.col < self.total_rows -1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])                                       # RIGHT
            
        # append to the adjacancy list of the node\spot the square on the left of it, unless its a barrier
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():                            # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])             
    def __lt__(self, other): # overwrite the "less than <" opperator
        return False   
def graphify(grid):  # update adjacancy list of each node in the grid, using the update_neighbors() method
    for row in grid:
        for spot in row:
            spot.update_neighbors(grid)
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2)+abs(y1-y2)

def A_star(draw, grid, start, end):
# =============================================================================
# the following function is the exact implementation of the pseudo code appearing in wikipedia    
# =============================================================================
    
    
    # reminder: the "draw" var we input is actually a function (or a lambda expression which is a 1 line unction), so draw(var1,var2,..,varn) is the way to use it.
    # we actually assign the local var draw thats here to be the draw() function (not the spot.draw() method) seen below, which gets the following vars: win (the pygame window which is a global var so 
    # its in he scope of all functions and doesnt need to be sent), grid (which consists of all nodes and their colors), start and end nodes. 
    # It is entirely unclear why we need to send this algorith the draw() function as an input, when we have all the parameters needed to invoke it ourselfs (as we get grid,start,end as inputs and win is known to all functions)
    # the only posibility is that we can now invoke draw(win, grid,start,end) by just using draw(), but this could have been done all the same using a lambda expression inside the A_star scope.
    count = 0
    open_set = PriorityQueue() # The priority Queue (PQ) consists of unvisited nodes which we have encountered during our search. It consists of tuples each with a pointer to 
                               # to the node in question + some other usful info such as its G value (its distance from the start node which == count etc.)
    open_set.put( (0, count, start) ) # the PQ consist initially with the start node
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row} # this is a neet python way to initialize the g_score dictionary with each spot\node as key and inf as value
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    open_set_hash = {start} # we initialize a set\hash function to store all the items that are inside the PQ, as checking if an element is in the PQ can takes at least O(N), depending on how the PQ is implemented.
                            # now we can see if an element was enqued already by looking at the hash in constant time (at the expance of the hash\set memory ofcourse)
    while not open_set.empty():
        # allow for user interruption
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]
        open_set_hash.remove(current)
        
        if current == end:
            reconstruct_path(came_from, start, end)
            draw()
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current]+1
            
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = g_score[neighbor] + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put( (f_score[neighbor], count, neighbor) )
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        
        draw()
        
        if current != start:
            current.make_closed()
    
    return False
def reconstruct_path(came_from, start, end):
    node = end
    while node != start:
        node.make_path()
        node = came_from[node]
        
        
        
        
        


def make_grid(rows, width):
    grid = []
    gap = width // rows # the width of each cube 
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))
def draw(win, grid, rows, width):
    win.fill(WHITE) # fill the entire screen with white
    for row in grid:
        for spot in row:
            spot.draw(win)
            
    draw_grid(win, rows, width)
    pygame.display.update()    
def get_click_pos(pos, rows, width):
    gap = width // rows
    y,x = pos
    row = y // gap
    col = x // gap
    return row, col

def main(win, width):
    ROWS = 50
    # COLS = ROWS
    grid = make_grid(ROWS, width)
    
    start = None
    end = None
    
    run = True
    started = False
    
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if started:
                continue
            if pygame.mouse.get_pressed()[0]: # left mouse button pressed
                pos = pygame.mouse.get_pos()
                row, col = get_click_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()
                    
                    
            elif pygame.mouse.get_pressed()[2]: # right mouse button pressed
                pos = pygame.mouse.get_pos()
                row, col = get_click_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    graphify(grid) # once the user pressed down on the spaceBar then he is done drawing the graph. now 
                                   # we use graphify() to run over all nodes and connect them to each other (i.e. update each node's\spots' adjacancy list to include its neighboring nodes)
                A_star(lambda: draw(win, grid, ROWS, width), grid, start, end )
            
            if event.type == pygame.K_c:
                start = None
                end = None
                grid = make_grid(ROWS, width)
            
    pygame.quit()
    

if __name__ == "__main__":
    main(win, WIDTH)
