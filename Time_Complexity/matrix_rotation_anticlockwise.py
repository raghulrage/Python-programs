def reverse(arr, i, j):
    for idx in range((j - i + 1) // 2):
        arr[i + idx], arr[j - idx] = arr[j - idx], arr[i + idx]
 
 
def rotateList(A, K):

    l = len(A)
    K %= len(A)
 
    reverse(A, l - K, l - 1)
    reverse(A, 0, l - K - 1)
    reverse(A, 0, l - 1)
 
    return A
 
 
def rotateLayers(N, M, R, layers):
    for layer in layers:
        rotateList(layer, len(layer) - R)
 
 
def rotateMatrix(M, N, R, mat):

    l = int(min(N, M) // 2)
    layers = [[] for _ in range(l)]
    for level in range(l):
        top = (N - 1) - 2 * level
        side = (M - 1) - 2 * level
        for i in range(top):  # right
            layers[level].append(mat[level][level + i])
        for j in range(side):  # down
            layers[level].append(mat[level + j][level + top])
        for i in range(top):  # left
            layers[level].append(mat[level + side][level + top - i])
        for j in range(side):  # up
            layers[level].append(mat[level + side - j][level])
 
    # rotate each layer
    rotateLayers(N, M, R, layers)
 
    # fill the layers back in
    for level in range(l):
        top = (N - 1) - 2 * level
        side = (M - 1) - 2 * level
        for i in range(top):
            mat[level][level + i] = layers[level].pop(0)  # right
        for j in range(side):
            mat[level + j][level + top] = layers[level].pop(0)  # down
        for i in range(top):
            mat[level + side][level + top - i] = layers[level].pop(0)  # left
        for j in range(side):
            mat[level + side - j][level] = layers[level].pop(0)  # up
 
 
def main():
    # M, N, R = map(int, raw_input().split())
    mat = []
    M, N, R = 4,4,1
    # for i in range(M):
    #     mat.append(list(map(int, raw_input().split())))
    mat = [ [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
          ]
    rotateMatrix(M, N, R, mat)

    for i in mat:
        print(*i)
 
 
if __name__ == '__main__':
    main()
