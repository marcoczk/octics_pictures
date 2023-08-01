import sa
var('a b c d e f g h i')
im = sqrt(-1)
s3 = sqrt(-3)
ss3 = sqrt(3)
mm = matrix(SR,[[0   ,0   ,0,1],
                [0   ,1   ,0,a],
                [0   ,im  ,1,b],
                [0   ,-im ,1,c],
                [1+s3,ss3 ,1,d],
                [1-s3,ss3 ,1,e],
                [-2  ,ss3 ,1,f],
                [1+s3,-ss3,1,g],
                [1-s3,-ss3,1,h],
                [-2  ,-ss3,1,i]])

def minm(mat,v1,v2,v3,v4):
    return matrix(SR,[vector(mat[v1,:]),vector(mat[v2,:]),vector(mat[v3,:]),vector(mat[v4,:])])

det(minm(mm,1,2,4,6))
det(minm(mm,1,2,5,7))
det(minm(mm,1,2,8,9))
det(minm(mm,2,3,4,5))
det(minm(mm,2,3,6,9))
det(minm(mm,2,3,7,8))
det(minm(mm,1,3,4,8))
det(minm(mm,1,3,5,6))
det(minm(mm,3,4,6,7))
det(minm(mm,4,6,8,9))
det(minm(mm,3,5,8,9))
det(minm(mm,1,4,5,9))
det(minm(mm,4,5,7,8))
det(minm(mm,1,6,7,8))
det(minm(mm,2,5,6,8))
det(minm(mm,5,6,7,9))
det(minm(mm,2,4,7,9))