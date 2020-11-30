from turtle import *

#Length of each side in units
N = 500

def solve( len ):
    #Don't recurse below 20 units
	if len <= 20:
		forward( len ) #Print a line
	else:
		solve( len / 4 )
		left( 60 )
		solve( len / 4 )
		right( 120 )
		solve( len / 4 )
		left( 60 )
		solve( len / 4 )
	
color( 'red', 'blue' ) #Red boundary and blue filling
speed( 0 )
begin_fill()
#Build 3 sides of the enclosed structure
for i in range( 1, 4 ):
	solve( N )
	right( 120 )
end_fill()
done()
