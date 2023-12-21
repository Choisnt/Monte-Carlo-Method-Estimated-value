import matplotlib.pyplot as plt
import numpy as np

# 점의 개수를 설정합니다.
num_points = 1000

# 0과 1 사이의 무작위 점을 생성합니다.
points = np.random.rand(num_points, 2)

# 원의 중심에서의 거리를 계산합니다.
distances = np.sqrt(points[:,0]**2 + points[:,1]**2)

# 원 안에 들어간 점과 원 밖에 있는 점을 구분합니다.
inside_circle = distances <= 1.0
outside_circle = np.logical_not(inside_circle)

# 원주율을 추정합니다.
estimated_pi = 4 * np.sum(inside_circle) / num_points

# 결과를 출력합니다.
print(f"Estimated pi: {estimated_pi}")

# 그림을 그립니다.
fig, ax = plt.subplots(figsize=(6,6))
plt.scatter(points[inside_circle,0], points[inside_circle,1], color='b')
plt.scatter(points[outside_circle,0], points[outside_circle,1], color='r')

# 원의 경계를 그립니다.
circle = plt.Circle((0, 0), 1, color='black', fill=False)
ax.add_artist(circle)

plt.title(f"Estimation of Pi using Monte Carlo Method\nEstimated value: {estimated_pi}")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
