

import numpy as np

a = np.array([1, 2, 3])

print(a.shape)


import numpy as np

b = np.array([[1, 2, 3],

              [4, 5, 6]])

print(b.shape)




import numpy as np

c = np.array([[[1, 2],

               [3, 4]]])

print(c.shape)


import numpy as np

c = np.array([[[1, 2], [3, 4]],

              [[5, 6], [7, 8]]])

print(c.shape)



import numpy as np

sales = np.array([

    [100, 120, 90],

    [110, 130, 95],

    [105, 125, 100]

])

print("每天銷售:", sales.sum(axis=1))

print("每商品銷售:", sales.sum(axis=0))

print("總銷售:", sales.sum())


import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[0])



import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[0:4:2])


a = np.array([

    [10, 20, 30],

    [40, 50, 60],

    [70, 80, 90]

])

print(a[1])

print(a[:, 2])

print(a[0, :])



a = np.array([

    [10, 20, 30],

    [40, 50, 60],

    [70, 80, 90]

])

print(a[1])

print(a[:, 2])

print(a[0, :])



a = np.array([

    [10, 20, 30],

    [40, 50, 60],

    [70, 80, 90]

])

print(a[0:2, :])

print(a[:, 1:3])

print(a[0:2, 1:3])



import numpy as np

a = np.array([

    [[10, 20, 30],

     [40, 50, 60],

     [70, 80, 90]],

    [[100, 110, 120],

     [130, 140, 150],

     [160, 170, 180]]

])

print(a[0:2, :, :])

print(a[:, 1:3, :])

print(a[0:2, :, 1:3])


import numpy as np

a = np.array([1, 2, 3])

b = 10

c = a + b

print(c)


import numpy as np

a = np.array([

    [100, 120, 90],

    [110, 130, 95],

    [105, 125, 100]

])

b = np.array([10, 20, 30])

c = a + b

print("原始銷售：", a)

print("調整金額：", b)

print("調整後銷售：", c)





import numpy as np

a = np.array([10, 50, 30])

print(np.argmax(a))

print(np.argmin(a))


import numpy as np

a = np.array(["A", "B", "C"])

b = np.array([10, 20, 30])

c = np.argmax(b)

d = np.argmin(b)

print("最大的品項:", a[c])

print("最小的品項:", a[d])



