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
		a  = sides of the shape
		b  = base of the shape
			@args: a, b -> Int or float
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
			l = length of the rectangle
			b =  base of the rectangle
				@args: l, b -> Int or float
				@returns: Int or float
	'''
	return 2 * (l + b)


# Rhombus
## AREA
def findTheAreaOFARhombus(p,q):
	'''
		FUNCTION NAME: 	findTheAreaOFARhombus
		This function computes the perimeter of a Rhombus which is the average of p times q
			p = one side of the rhombus
			q = the second side of the rhombus
				@args: p, q -> Int or float
				@returns: Int or float
	'''
	return (p * q)/ 2

## PERIMETER
def findThePerimeterOfARhombus(a):
	'''
		FUNCTION NAME: 	findThePerimeterOfARhombus
		This function computes the perimeter of a Rhombus which 4 times a
			a = sides of the rhombus
				@args: a -> Int or float
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
			a = sides of the trapezoid
				@args: a -> Int or float
				@returns: Int or float
	'''
	return 4 * a

# Kite
## AREA
def findAreaOfKite(p, q):
	'''
		FUNCTION NAME: 	findTheAreaOFAKite
		This function computes the perimeter of a Kite which is the average of p times q
			p = one side of the rhombus
			q = the second side of the rhombus
				@args: p, q -> Int or float
				@returns: Int or float
	'''
	return (p * q)/ 2

## PERIMETER
def findThePerimeterOfAKite(a,b):
	'''
	FUNCTION NAME: 	findThePerimeterOfAKite
	This function computes the perimeter of a Kite which 2 times ( the base times plus the  height)
		a  = sides of the shape
		b  = base of the shape
			@args:a, b -> Int or float
			@returns: Int or float
	'''
	return 2 * ( a + b)

# POLYGONS
## AREA
def findTheAreaOfPolygons(a, p):
	'''
		FUNCTION NAME: 	findTheAreaOFAKite
		This function computes the area of a Kite which is half of the apotem times the perimter
			a = apotem
			p = perimeter of the polygon
				@args: a, p-> Int or float
				@returns: Int or float
	'''
	return (a + p) / 2

def findThePerimeterOfPolygons(n):
		'''
	FUNCTION NAME: 	findThePerimeterOfAPolygon
	This function computes the perimeter of a polygon which is the sum of all the sides of the polygon
		n = sides
			@args: n -> Int or float
			@returns: Int or float
	'''
		n = []
		v = int(input('Enter the value of the each sides of the polygon:'))
		n.append(v)
		print(n)
		return (fsum(n))

# 3D shapes
# CUBE
## SURFACE AREA
def findTheAreaOfACube(s):
	'''
		FUNCTION NAME: 	findTheAreaOFACube
		This function computes the area of a cube which is 6 times the sd
			a = sides of the cube
				@args: a-> Int or float
				@returns: Int or float
	'''
	return 6 * (s **2)

## CIRCUMFERENCE 
def findTheCircumferenceOfACube(r, Pi = 3.142):
	'''
		FUNCTION NAME: 	findTheCircumferenceOfACube
		This function computes the circumference of a cube which is 2 * Pi * r
			Pi = a mathematical constant
			r = radius of hte cube
				@args: pi -> Int or float
				@args: r -> Int or float
				@returns: Int or float
	'''
	return 2 * Pi * r

#RECTANGLAR PRISM
# AREA
def Area_Of_Rectangular_Prism(l, h, w):
	'''
		FUNCTION NAME: 	Area_Of_Rectangular_Prism
		This function computes the area of a rectangular prism which is A = 2(w*l + h*l + h*w)
			l = length of the rectangular prism
			h = height of the rectangular prism
			w = width of the rectangular prism
				@args: l -> Int or float
				@args: w -> Int or float
				@args: h -> Int or float
				@returns: Int or float
	'''
	return 2 * (w * l) + (h * l) +  (h * w)

## VOLUME
def Volume_Of_Rectangular_Prism(l, h, w):
	'''
		FUNCTION NAME: 	Area_Of_Rectangular_Prism
		This function computes the volume of a rectangular prism which is side1 (l) * side2 (w) * side3 (h)
			l = length of the rectangular prism
			h = height of the rectangular prism
			w = width of the rectangular prism
				@args: l -> Int or float
				@args: w -> Int or float
				@args: h -> Int or float
				@returns: Int or float
	'''
	return l * h * w

# SPHERE
##SURFACE AREA
def Area_Of_Sphere( r, Pi = 3.142):
	'''
		FUNCTION NAME: 	Area_Of_Sphere
		This function computes the area of a sphere which is A = 4 * Pi * r.sqr
			r = radius of the sphere
			Pi = a mathematical constant
				@args: Pi > Int or float
				@args: r > Int or float
				@returns: Int or float
	'''
	return 4 * Pi * (r**2)

##VOLUME 
def Volume_Of_Sphere( r, Pi = 3.142):
	'''
		FUNCTION NAME: 	Volume_Of_Sphere
		This function computes the volume of a sphere which is 4/3 * Pi * r.cube
			r = radius of the sphere
			Pi = a mathematical constant
				@args: Pi > Int or float
				@args: r > Int or float
				@returns: Int or float
	'''
	return 4/3 * Pi * (r ** 3)


# CONE
## AREA
def Area_Of_Cone(r, l, Pi = 3.142):
	'''
		FUNCTION NAME: 	Area_Of_Cone
		This function computes the area of a Cone which is A = Pi * r * side(l)
			r = radius of the sphere
			Pi = a mathematical constant
			l = sides of the cone
				@args: Pi > Int or float
				@args: r -> Int or float
				@args: l -> Int or float
				@returns: Int or float
	'''
	return Pi * r * l

## VOLUME
def Volume_Of_Cone( r, Pi = 3.142):
	'''
		FUNCTION NAME: 	Volume_Of_Cone
		This function computes the volume of a Cone which is 1/3 * Pi * r.sqr * height(h)
			r = radius of the Cone
			Pi = a mathematical constant
			h = height of the cone
				@args: Pi -> Int or float
				@args: r -> Int or float
				@args: l -> Int or float
				@returns: Int or float
	'''
	return 1/3 * Pi * (r ** 2) * h













