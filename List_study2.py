# -*- coding: utf-8 -*-
# @Author  : Mlx
a=[1,2,3]
b=a
a.append(5)
print a,b
#result   [1, 2, 3, 5] [1, 2, 3, 5]
a=[1,2,3]
b=a
a=[4,5,6]
print a,b
#result    [4, 5, 6] [1, 2, 3]