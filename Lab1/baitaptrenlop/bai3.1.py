import numpy as np 
vec1 = np.array([1., 3., 5.]) 
print(vec1 * 2)
#[ 2.  6. 10.]
print(vec1 * vec1)
#[ 1.  9. 25.]
print(vec1 / 2)
#[0.5 1.5 2.5]
print(vec1 + vec1)
#[ 2.  6. 10.]
vec2 = np.array([2., 4.])
#print(vec1 + vec2)
#ValueError: operands could not be broadcast together with shapes (3,) (2,)
#lỗi xuất hiện do cộng 2 vececto có kích thước không tương đương
vec3 = np.array([2., 4., 6.])
print(vec1 + vec3)
#[ 3.  7. 11.]
print(vec1 / vec3)
#[0.5        0.75       0.83333333]
print(vec1 * vec3)
#[ 2. 12. 30.]
print(2* vec1 + 5* vec3)
#[12. 26. 40.]
print(vec3[2])
#6.0
vec4 = np.linspace(0, 20, 5)
print(vec4)
#vec4 = np.linspace(0, 20, 5)
vec5 = np.zeros(5)
print(vec5)
#[0. 0. 0. 0. 0.]
vec6 = np.ones(5)
print(vec6)
#[1. 1. 1. 1. 1.]
vec7 = np.empty(5)
print(vec7)
#[1. 1. 1. 1. 1.]
vec8 = np.random.random(5)
print(vec8)
#[0.46544093 0.29013607 0.23554416 0.10955278 0.89011248]
v = np.array([1., 3., 5.])
print(np.sum(v))
#9.0
print(v.shape)
#(3,)
print(v.transpose())
#[1. 3. 5.]
v1 = v[:2]
print(v1)
#[1. 3.]
v[0] = 5
print(v)
#[5. 3. 5.]
print(v1)
#[5. 3.]
#v1[:2] = [1., 2., 3.]
#ValueError: could not broadcast input array from shape (3,) into shape (2,)
#lỗi xảy ra khi bạn cố gán một mảng có 3 phần tử vào mảng có 2 phần tử
v1[:2] = [1., 2]
print(v)
#[1. 2. 5.]
v3 = 2 * v[:2] + v1 * 3
print(v3)
#[ 5. 10.]
v1 = [4, 6]
print(v3)
#[ 5. 10.]
print(v)
#[1. 2. 5.]
v + 10.0
print(np.sqrt(v))
#[1.         1.41421356 2.23606798]
print(np.cos(v))
#[ 0.54030231 -0.41614684  0.28366219]
print(np.sin(v))
#[ 0.84147098  0.90929743 -0.95892427]
print(np.dot(v1, v3))
#80
#print(v1.dot(v3))
#AttributeError: 'list' object has no attribute 'dot'
#v1 ở trên là danh sách chứ không phải mảngmảng
print(v3.dot(v1))
#8080