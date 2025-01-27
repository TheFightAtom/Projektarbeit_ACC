from radariq import find_com_port, RadarIQ, MODE_POINT_CLOUD

import matplotlib.pyplot as plt

import numpy as np

fig = plt.figure()

ax = fig.add_subplot(projection='3d')

riq = RadarIQ()

riq.set_mode(MODE_POINT_CLOUD)

riq.set_units('m', 'm/s')

riq.set_frame_rate(10)

riq.set_distance_filter(0, 10)

riq.set_angle_filter(-45, 45)

riq.start(20)

for row in riq.get_data():

for x, y, z, q, v in row :

ax.scatter(x, y, z, '*')

ax.set_xlabel('X')

ax.set_ylabel('Y')

ax.set_zlabel('Z')

plt.show()
