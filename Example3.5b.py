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
  
def four_filled_elem():
    do_four(filled_grid_elem)
    print('+')
    
def four_empty_elem():
    do_four(empty_grid_elem)
    print('|')
    
def draw_cells():
    four_filled_elem()
    do_four(four_empty_elem)

def draw_grid():
    do_four(draw_cells)
    four_filled_elem()
    
draw_grid()