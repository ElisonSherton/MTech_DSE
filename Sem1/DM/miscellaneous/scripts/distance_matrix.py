from scipy import spatial
import numpy as np

points = np.array([[.4, .53],
                   [.2, .38],
                   [.35, .32],
                   [.26, .19],
                   [.08, .41],
                   [.45, .3],
                   ])

print(np.round(spatial.distance_matrix(points, points),3))