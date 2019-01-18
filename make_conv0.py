# coding:utf-8
import numpy as np
import os


param_path = "make_file/conv02to01v4"

if not os.path.isdir(param_path):
    os.makedirs(param_path)

w = np.arange(9).reshape((3, 1, 1, 3))
# w = np.arange(208).reshape((16, 1, 1, 13))
# w = np.arange(16).reshape((4, 1, 1, 4))
b = [-120.0, -120.0, -120.0]
# b = [-1.0, -1.0, -1.0, 0.0]

w = np.array(w, dtype="float32")

w[0][0][0][0] = 0.5
w[0][0][0][1] = 0.0
w[0][0][0][2] = 0.0
# w[0][0][0][3] = 0.0
w[1][0][0][0] = 0.0
w[1][0][0][1] = 0.5
w[1][0][0][2] = 0.0
# w[1][0][0][3] = 0.0
w[2][0][0][0] = 0.0
w[2][0][0][1] = 0.0
w[2][0][0][2] = 0.5
# w[2][0][0][3] = 0.0
# w[3][0][0][0] = 0.0
# w[3][0][0][1] = 0.0
# w[3][0][0][2] = 0.0
# w[3][0][0][3] = 1.0

print(w)


w2 = np.array(w, dtype="float32")
print(w2.shape)

b2 = np.array(b, dtype="float32")
print(b2.shape)

if not os.path.isdir(param_path):
    os.mkdir(param_path)
np.array(w2).tofile(os.path.join(param_path, "conv02to01_w" + ".bin"))
# np.array(b2).tofile(os.path.join(param_path, "conv00a_b" + ".bin"))
