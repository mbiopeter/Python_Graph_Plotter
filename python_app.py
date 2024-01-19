import matplotlib.pyplot as plt

x1=[0,2,4,6,8,10]
y1=[0,3,6,9,12,15]

plt.plot(x1,y1, label='Line 1')
x2=[0,2,4,7,9,12,15]
y2=[0,4,6,8,11,16,17]

plt.plot(x2,y2, label='Line 2')

plt.xlabel('X AXIS')
plt.ylabel('Y AXIS')
plt.title('Demo Graph')

plt.legend()

plt.show()
