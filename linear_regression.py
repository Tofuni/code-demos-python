# params: (ls) a list of 2-item tuples
def lin_reg(ls):
	n, xy, x2, y2, x, y = len(ls), 0, 0, 0, 0, 0
	for i in range(0,len(ls)):
		x += ls[i][0]
		y += ls[i][1]
		x2 += ls[i][0]**2
		y2 += ls[i][1]**2
		xy += ls[i][0]*ls[i][1]
	a = ((y*x2)-(x*xy))/((n*x2)-x**2)
	b = ((n*xy)-(x*y))/((n*x2)-x**2)
	return {'a':a, 'b':b, 'formula':'y = '+str(a)+' + '+str(b)+'*x'}
	
# ------------------- test -------------------

a = [
	[(0,1),(2,11)],
	[(0,0),(1,1),(2,2),(3,3)],
	[(0,0),(1,2),(2,4),(3,6)],
	[(-1,5),(1,1),(2,-1),(3,-3)],
	[(0,2),(1,2.5),(2,3),(3,3.5)],
	[(0,-1),(1.1,-1.7),(1.85,-2.9),(3.1,-3.85)],
	[(0,1),(23,27),(40,42),(50,55),(31,37),(40,50),(12,15),(63,59),(46,39),(20,26)],
	[(0,11.2),(1.8,0.3),(3.7,-12.5),(6.2,-19.2),(7.9,-31.5)],
	[(3,1),(5,3),(2,1),(7,4)]
	]
for i in a:
	print('\n' + str(i) + '\n\n' + str(lin_reg(i)) + '\n\n--------------------')
input()