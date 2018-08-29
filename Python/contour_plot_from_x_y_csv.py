from numpy import linspace, meshgrid
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
import csv

def grid(x, y, z, resX=100, resY=100):
    "Convert 3 column data to matplotlib grid"
    xi = linspace(min(x), max(x), resX)
    yi = linspace(min(y), max(y), resY)
    Z = griddata(x, y, z, xi, yi)
    X, Y = meshgrid(xi, yi)
    return X, Y, Z

x_array = []
y_array = []
z_array = []

f=open("don_and_acceptor_only.exposed.csv", "r")
contents = f.readlines()
for i in contents:
    x = float( i.split(',')[0] )
    y = float( i.split('\n')[0].split(',')[1] )
    x_array.append( x )
    y_array.append( y )
    z_array.append( 0 )
    #print( str(x) + " ... " + str(y) )

plt.scatter( x_array, y_array, z_array )
#X, Y, Z = grid(x, y, z)
#plt.contourf(X, Y, Z)
