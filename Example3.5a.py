def do_twice(function):
    function()
    function()

def do_four(function):
    do_twice(function)
    do_twice(function)
    
def filled_grid_elem():
    print('+ - - - - ', end= "")
  
def empty_grid_elem():
    print('|         ', end= "")
  
def two_filled_elem():
    do_twice(filled_grid_elem)
    print('+')
    
def two_empty_elem():
    do_twice(empty_grid_elem)
    print('|')
    
def draw_cells():
    two_filled_elem()
    do_four(two_empty_elem)

def draw_grid():
    do_twice(draw_cells)
    two_filled_elem()
    
draw_grid()