from matplotlib.mlab import griddata
from numpy import linspace, meshgrid
from numpy.random import uniform, seed
from scipy.interpolate import griddata
import csv
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import numpy.ma as ma

def grid(x, y, z, resX=100, resY=100):
    "Convert 3 column data to matplotlib grid"
    xi = linspace(min(x), max(x), resX)
    yi = linspace(min(y), max(y), resY)
    Z = griddata(x, y, z, xi, yi)
    X, Y = meshgrid(xi, yi)
    return X, Y, Z

x_array = []
y_array = []
#z_array = []

f=open("don_and_acceptor_only.exposed.csv", "r")
contents = f.readlines()
for i in contents:
    x = float( i.split(',')[0] )
    y = float( i.split('\n')[0].split(',')[1] )
    x_array.append( x )
    y_array.append( y )
    #z_array.append( 0 )
    #print( str(x) + " ... " + str(y) )

print( len( x_array ) )

#plt.scatter( x_array, y_array )
#X, Y = grid(x_array, y_array)
#plt.contourf(X, Y)
#plt.show()
#plt.savefig('plot.png')

'''
delta = 0.1
x = np.arange(0, 100, delta)
y = np.arange(0, 100, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
Z = 10.0 * (Z2 - Z1)

norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())
cmap = cm.PRGn

levels = np.arange(-2.0, 1.601, 0.4)

fig, axes = plt.subplots(1,1, sharey=True)

ax = axes

ax.contourf(X, Y, Z, levels,
            cmap=cm.get_cmap(cmap, len(levels)-1),
            norm=norm)
ax.autoscale(False) # To avoid that the scatter changes limits
ax.scatter( x_array,
            y_array,
            zorder=1)
ax.set_title('Scatter with zorder={0}'.format(1))

plt.show()
'''

npts = len(x_array)
#x = uniform(-2,2,len(x_array))
#y = uniform(-2,2,len(y_array))
x = np.asarray( x_array )
y = np.asarray( y_array )
assert len( x ) == len( x_array )
assert len( y ) == len( y_array )
z = x * np.exp( -x**2 - y**2 )
# define grid
xi = np.linspace(0,40,400)
yi = np.linspace(0,60,600)
# grid the data.
zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')
# contour the gridded data, plotting dots at the randomly spaced data points.
CS = plt.contour(xi,yi,zi,5,linewidths=0.5,colors='k')
CS = plt.contourf(xi,yi,zi,5,cmap=plt.cm.jet)
plt.colorbar() # draw colorbar
# plot data points.
#plt.scatter(x,y,marker='o',c='b',s=5)
plt.xlim(0,100)
plt.ylim(0,200)
plt.title('griddata test (%d points)' % npts)
plt.show()
