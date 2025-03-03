import point
# p=point.Point3(1,1,1)
def copy2d(p):
	q=point.Point3(p.x,p.y,0)
	return q
q=point.Point3(1,2,3)
r=copy2d(q)
# if __name__=='__main__':

print(r)
print(r.x,r.y,r.z)

