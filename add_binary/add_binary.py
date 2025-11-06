class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        c = '0'
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 and j >= 0:
            print(a[i], b[j], c)
            if (a[i] == '0' and b[j] == '1') or (a[i] == '1' and b[j] == '0'):
                # 0 + 1 + 1 => 10
                if c == '1':
                    res += '0'
                    c = '1'
                else:
                    res += '1'

            elif a[i] == '1' and b[j] == '1':
                # 1 + 1 + 1 => 1 1
                if c == '1': 
                    res += '1'
                    c = '1'
                # 1 + 1 + 0 => 1 0
                else:
                    res += '0'
                    c = '1'
            
            else:
                # 0 + 0 + 1 => 1
                if c == '1': 
                    res += '1'
                    c = '0'
                else:
                    res += '0'
            print('=', c, res)
            i -= 1
            j -= 1

        while i >= 0:
            # 0 + 1 or 1 + 0 => 1
            if (a[i] == '0' and c == '1') or (a[i] == '1' and c == '0'):
                res += '1'
                c = '0'
            # 1 + 1 => 1 0
            elif a[i] == '1' and c == '1':
                res += '0'
                c = '1'
            # 0 0
            else:
                res += '0'
            
            i -= 1
        
        while j >= 0:
            if (b[j] == '0' and c == '1') or (b[j] == '1' and c == '0'):
                res += '1'
                c = '0'
            elif b[j] == '1' and c == '1':
                res += '0'
                c = '1'
            else:
                res += '0'

            j -= 1

        if c != '0': res += c

        return res[::-1]
        