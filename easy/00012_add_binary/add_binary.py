# https://leetcode.com/problems/add-binary/

def addBinary(a: str, b: str) -> str:
    a2 = int(a, 2)
    b2 = int(b, 2)
    c2 = f'{a2 + b2:b}'
    return c2

if __name__ == '__main__':
    a = '11'
    b = '1'
    addBinary(a, b)
        
