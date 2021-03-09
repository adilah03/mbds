### Question 6 ###

# needed for point.in.polygon function
library(sp)

# load points of polygon and split into x and y coordinates
poly_points <- read.table('input_question_6_polygon')
poly_x <- poly_points[,1]
poly_y <- poly_points[,2]

# load query points and split into x and y coordinates
query_points <- read.table('input_question_6_points')
query_x <- query_points[,1]
query_y <- query_points[,2]

# run point.in.polygon function
# algorithm works by 
# 1) create edges that connects polygon points
# 2) extend each query point along the x axis both to the left and right as a ray 
# 3) count the number of intersections between the left/right ray and the edges
# 4) if the numbers are 0 and an even number, the point lies outside of the polygon, function returns 0
# 5) if the numbers are both odd, the point lies inside the polygon, function returns 1
# 6) if the numbers are an odd and an even number, the point lies on an edge of the polygon, function returns 2
# 7) if the point is a point of the polygon, i.e., it is a vertex, function returns 3
position <- point.in.polygon(query_x, query_y, poly_x, poly_y)
output <- cbind(query_points,position)
# change integer labels to string labels
output$position[output$position==0] <- 'outside'
output$position[output$position==1] <- 'inside'
output$position[output$position==2] <- 'inside'
output$position[output$position==3] <- 'inside'

write.table(output, 'output_question_6', quote=F, row.names=F, col.names=F)