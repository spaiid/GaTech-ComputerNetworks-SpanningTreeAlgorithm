# submitted by , OMSCS Fall 2018

#          6---------49----------42      56-------45------1
#          |                     |        |
# 23------10-------14   16------27-------67
# |\      /|\      /|   |\      /|\      /|
# | \    / | \    / |   | \    / | \    / |
# |  \  /  |  \  /  |   |  \  /  |  \  /  |
# |   \/   |   \/   |   |   \/   |   \/   |
# |   /\   |   /\   |   |   /\   |   /\   |
# |  /  \  |  /  \  |   |  /  \  |  /  \  |
# | /    \ | /    \ |   | /    \ | /    \ |
# |/      \|/      \|   |/      \|/      \|
# 8--------7--------4   11-------12------13
# |\      /|\      /|   |\      /|\      /|
# | \    / | \    / |   | \    / | \    / |
# |  \  /  |  \  /  |   |  \  /  |  \  /  |
# |   \/   |   \/   |   |   \/   |   \/   |
# |   /\   |   /\   |   |   /\   |   /\   |
# |  /  \  |  /  \  |   |  /  \  |  /  \  |
# | /    \ | /    \ |   | /    \ | /    \ |
# |/      \|/      \|   |/      \|/      \|
# 2--------33------18   32-------5-------88

topo = {
	1: [45],
	2: [7,8,33],
	4: [14,7,10,33,18],
	5: [32,11,12,13,88],
	6: [49,10],
	7: [2,8,23,10,14,4,18,33],
	8: [23,10,7,33,2],
	10: [6,23,8,7,4,14],
	11: [16,27,12,5,32],
	12: [16,27,67,13,88,5,32,11],
	13: [67,27,12,5,88],
	14: [10,7,4],
	16: [27,12,11],
	18: [33,7,4],
	23: [10,7,8],
	27: [42,16,11,12,13,67],
	32: [5,12,11],
	33: [2,8,7,4,18],
	42: [49,27],
	45: [1,56],
	49: [6,42],
	56: [45,67],
	67: [56,27,12,13],
	88: [13,12,5]
}

# 1 - 45
# 2 - 7
# 4 - 10, 4 - 18, 4 - 33
# 5 - 12
# 6 - 10, 6 - 49
# 7 - 2, 7 - 10
# 8 - 10
# 10 - 4, 10 - 6, 10 - 7, 10 - 8, 10 - 14, 10 - 23
# 11 - 12
# 12 - 5, 12 - 11, 12 - 16, 12 - 32, 12 - 67, 12 - 88
# 13 - 67
# 14 - 10
# 16 - 12
# 18 - 4
# 23 - 10
# 27 - 42, 27 - 67
# 32 - 12
# 33 - 4
# 42 - 27, 42 - 49
# 45 - 1, 45 - 56
# 49 - 6, 49 - 42
# 56 - 45, 56 - 67
# 67 - 12, 67 - 13, 67 - 27, 67 - 56
# 88 - 12