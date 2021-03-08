### Question 5 ###

# create L by L square grid
create_grid <- function(L) {
  g <- matrix(rep('X',L^2), nrow = L)
  return(g)
}

# The algorithm works by placing beads of the same color in alternate spaces
# In the first fill, we place the beads in odd columns of odd rows and even columns of even rows
# In the second fill, we place the beads in even columns of odd rows and odd columns of even rows

# find total number of spaces for first fill
mid_spaces <- function(L) {
  i = L^2/2
  return(ceiling(i))
}

# find the last filled row in our first fill
last_filled_row_1 <- function(grid) {
  filled <- which(grid != 'X', arr.ind=T)
  if (nrow(filled) == 0) {return(1)}
  else {return(max(filled[,'row']))}
}

# find the last filled row in our second fill
last_filled_row_2 <- function(grid) {
  filled <- which(grid != 'X', arr.ind=T)
  if (nrow(filled) == 0) {return(1)}
  else {return(min(filled[,'row']))}
}

# first fill
fill_grid_1 <- function(grid, n, bead) {
  i = 1 # number of beads that we have filled
  L = nrow(grid)
  # find the last filled row among first fill
  start_row = last_filled_row_1(grid)
  # iterate from this row onward to the last row
  for (r in start_row:L) {
    c = 1
    # iterate within the columns of each row
    while (c <= L) {
      # check if it is unfilled
      if (grid[r,c] == 'X') {
        # check that we have not filled all the beads
        if (i > n) {break}
        # check that it is either odd column, odd row
        else if (r%%2==1 & c%%2==1) {
          grid[r,c] <- bead
          i = i + 1
        }
        # or even column, even row
        if (r%%2==0 & c%%2==0) {
          grid[r,c] <- bead
          i = i + 1
        }
        # if it fulfills all our conditions, we can put the bead in the space
        # and update our count, i
      }
      c = c + 1 # update the column index
    }
  }
  return(grid)
}

# second fill
# same as the first fill, but this time we
fill_grid_2 <- function(grid, n, bead) {
  i = 1
  L = nrow(grid)
  start_row = last_filled_row_2(grid)
  for (r in start_row:L) {
    c = 1
    while (c <= L) {
      if (grid[r,c] == 'X') {
        if (i > n) {break}
        # check that it is either odd row, even column
        else if (r%%2==1 & c%%2==0) {
          grid[r,c] <- bead
          i = i + 1
        }
        # or even row, odd column
        if (r%%2==0 & c%%2==1) {grid[r,c] <- bead
        i = i + 1
        }
      }
      c = c + 1
    }
  }
  return(grid)
}

# For this algorithm, we fill the beads in the order of their sizes,
# i.e, the color with the most beads gets filled first and so on
# As long as the biggest size is less than half of the grid (mid_spaces),
# there is no penalty

# 5.1)
a <- create_grid(5)
a <- fill_grid_1(a, 13, 'B')
a <- fill_grid_2(a, 12, 'R')
write.table(a, 'output_question_5_1', quote=F, row.names=F, col.names=F)

# 5.2)
b <- create_grid(64)
mid = mid_spaces(64) # find number of spaces for first fill
b <- fill_grid_1(b, 1451, 'B')
b <- fill_grid_1(b, 597, 'W') # split white beads over the 2 fills
b <- fill_grid_2(b, 475, 'W')
b <- fill_grid_2(b, 977, 'G')
b <- fill_grid_2(b, 457, 'Y')
b <- fill_grid_2(b, 139, 'R')
write.table(b, 'output_question_5_2', quote=F, row.names=F, col.names=F)

