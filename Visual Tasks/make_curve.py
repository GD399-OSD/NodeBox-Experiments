from nodebox.graphics import Path,Color
def makecurve(pt1,pt2,c1,c2):
	p = Path()
	p.moveto(pt1.x, pt1.y)
	p.curveto(c1.x, c1.y, c2.x, c2.y, pt2.x, pt2.y)
	p.fill = None
	p.stroke = Color.BLACK
	p.strokeWidth = 1.0
	return p