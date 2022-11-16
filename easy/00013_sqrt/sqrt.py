# https://leetcode.com/problems/sqrtx/

def mySqrt(x: int) -> int:
    '''From problem constraints:
        0 <= x <= 2^31 - 1
    so, max_sqrt_value ≃ 65_536 '''
    max_sqrt_value = 65_536
    i, j = 0, max_sqrt_value
    while i < j:
        mid = (i + j) // 2
        pow2 = mid ** 2
        if pow2 == x:
            return mid
        if pow2 > x:
            j = mid - 1
        else:
            i = mid + 1
    if i ** 2 <= x:
        return i
    else:
        return i - 1

if __name__ == '__main__':
    mySqrt(2)
