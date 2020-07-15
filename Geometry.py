''' for 2D shapes, we have to work on the following
[] Triangle
[] Parallelogram
[] Square
[] Rectangle
[] Rhombus
[] Trapezoid
[] Kite
[] Polygons

'''

# Triangle
## AREA OF A TRIANGLE
def findAreaOfTriangle(b,h):
	'''
	FUNCTION NAME: 	findAreaOfTriangle
	This function computes the area of a triangle which is half of the base times the  height
		b = distance along the base of the triangle
		h = vertical height of the triangle measured at right angles to the base
			@args: b, h -> Int or float
			@returns: Int or float
	'''
	return 0.5 * b * h

## PYTHAGOREAN THEOREM
def calculateThePythagoreanTheorem():
	from math import sqrt

	print('Pythagorean theorem calculator! Calculate your triangle sides.')
	print('Assume the sides are a, b, c and c is the hypotenuse (the side opposite the right angle')
	formula = input('Which side (a, b, c) do you wish to calculate? side> ')

	if formula == 'c':
		side_a = int(input('Input the length of side a: '))
		side_b = int(input('Input the length of side b: '))

		side_c = sqrt(side_a * side_a + side_b * side_b)
		
		print('The length of side c is: ' )
		print(side_c)

	elif formula == 'a':
	    side_b = int(input('Input the length of side b: '))
	    side_c = int(input('Input the length of side c: '))
	    
	    side_a = sqrt((side_c * side_c) - (side_b * side_b))
	    
	    print('The length of side a is' )
	    print(side_a)

	elif formula == 'b':
	    side_a = int(input('Input the length of side a: '))
	    side_b = int(input('Input the length of side c: '))
	        
	    side_c = sqrt(side_c * side_c - side_a * side_a)
	    
	    print('The length of side b is')
	    print(side_c)

	else:
		print('Please select a side between a, b, c')

#Parallelogram
## AREA
def findAreaOfParallelogram(b,h):
	'''
	FUNCTION NAME: 	findAreaOfParallelogram
	This function computes the area of a parallelogram which is the base times the  height
		b = distance along the base of the parallelogram
		h = vertical height of the parallelogram 
			@args: b, h -> Int or float
			@returns: Int or float
	'''
	return 0.5 * b * h	
## PERIMETER
def findThePerimeterOfAParallelogram(a,b):
	'''
	FUNCTION NAME: 	findThePerimeterOfAParallelogram
	This function computes the perimeter of a parallelogram which 2 times ( the base times plus the  height)
		b = distance along the base of the parallelogram
		h = vertical height of the parallelogram 
			@args: b, h -> Int or float
			@returns: Int or float
	'''
	return 2 * ( a + b)


# Square
## AREA
def findAreaOfSquare(s):
	'''
	FUNCTION NAME:	findAreaOfSquare
		This function computes the area of a square which is the square of the sides since all sides are equal
		s = sides of the square
		@args: s -> Int or float
		@returns: Int or float
	'''
	return s ** 2


# Rectangle
## AREA
def findAreaOfRectangle(b, h):
	'''
	FUNCTION NAME:	findAreaOfRectangle
		This function computes the area of a rectangle which is the base times the  height
		b = distance along the base of the rectangle
		h = vertical height of the rectangle
			@args: b, h -> Int or float
			@returns: Int or float
	'''
	return b * h

## PERIMETER
def  findThePerimeterOfARectangle(l,b):
	'''
		FUNCTION NAME: 	findThePerimeterOfARectangle
		This function computes the perimeter of a rectangle which 2 times ( the length times plus the  breadth)
			b = distance along the base of the rectangle
			h = vertical height of the rectangle 
				@args: b, h -> Int or float
				@returns: Int or float
	'''
	return 2 * (l + b)


# Rhombus
## AREA
def findTheAreaOFARhombus(p,q):
	'''
		FUNCTION NAME: 	findTheAreaOFARhombus
		This function computes the perimeter of a Rhombus which is the average of p times q
			b = distance along the base of the Rhombus
			h = vertical height of the Rhombus 
				@args: b, h -> Int or float
				@returns: Int or float
	'''
	return (p * q)/ 2

## PERIMETER
def findThePerimeterOfARhombus(a):
	'''
		FUNCTION NAME: 	findThePerimeterOfARhombus
		This function computes the perimeter of a Rhombus which 4 times a
			b = distance along the base of the Rhombus
			h = vertical height of the Rhombus 
				@args: b, h -> Int or float
				@returns: Int or float
	'''
	return 4 * a

# Trapezoid
## AREA
def findAreaOfTrapezoid(a, b, h):
	'''
	FUNCTION NAME: 	findAreaOfTrapezoid
	This function computes the area of a trapezoid which is the average of the two base lenght times the altitude
	a = upper base
	b = lower base
	h = height of the trapezoid
		@args: a,b, h -> Int or float
		@returns: Int or float
	'''
	return ((a + b)* h) / 2

## PERIMETER
def findThePerimeterOfATrapezoid(a):
	'''
		FUNCTION NAME: 	findThePerimeterOfATrapezoid
		This function computes the perimeter of a Trapezoid which 4 times a
			b = distance along the base of the Trapezoid
			h = vertical height of the Trapezoid 
				@args: b, h -> Int or float
				@returns: Int or float
	'''
	return 4 * a

# Kite
## AREA
def findAreaOfKite(p, q):
	'''
		FUNCTION NAME: 	findTheAreaOFAKite
		This function computes the perimeter of a Kite which is the average of p times q
			b = distance along the base of the Kite
			h = vertical height of the Kite 
				@args: b, h -> Int or float
				@returns: Int or float
	'''
	return (p * q)/ 2

## PERIMETER
def findThePerimeterOfAKite(a,b):
	'''
	FUNCTION NAME: 	findThePerimeterOfAKite
	This function computes the perimeter of a Kite which 2 times ( the base times plus the  height)
		b = distance along the base of the Kite
		h = vertical height of the Kite 
			@args: b, h -> Int or float
			@returns: Int or float
	'''
	return 2 * ( a + b)

# POLYGONS
## AREA
def findTheAreaOfPolygons(a, p):
	'''
		FUNCTION NAME: 	findTheAreaOFAKite
		This function computes the perimeter of a Kite which is half of the apotem times the perimter
			b = distance along the base of the Kite
			h = vertical height of the Kite 
				@args: b, h -> Int or float
				@returns: Int or float
	'''
	return (a + p) / 2

def findThePerimeterOfPolygons(n):
		'''
	FUNCTION NAME: 	findThePerimeterOfAPolygon
	This function computes the perimeter of a polygon which is the sum of all the sides of the polygon
		b = distance along the base of the polygon
		h = vertical height of the polygon 
			@args: b, h -> Int or float
			@returns: Int or float
	'''
	n = [int(input('Enter the value of the side of the polygon:'))]
	return fsum(n)












