class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = '0'
        i, j = len(a) - 1, len(b) - 1
        q = deque()
        while i >= 0 and j >= 0:
            if (a[i] == '1' and b[j] == '0') or (a[i] == '0' and b[j] == '1'):
                if c == '0': q.appendleft('1')
                else:
                    q.appendleft('0')
                    c = '1'
            elif a[i] == '1' and b[j] == '1':
                if c == '0': 
                    q.appendleft('0')
                else:
                    q.appendleft('1')
                c = '1'
            elif a[i] == '0' and b[j] == '0':
                if c == '0': q.appendleft('0')
                else:
                    q.appendleft('1')
                    c = '0'
            i -= 1
            j -= 1

        while i >= 0:
            if a[i] == '1' and c == '1':
                q.appendleft('0')
                c = '1'
            else:
                if c == '1':
                    q.appendleft('1')
                    c = '0'
                else:
                    q.appendleft(a[i])
            i -= 1

        while j >= 0:
            if b[j] == '1' and c == '1':
                q.appendleft('0')
                c = '1'
            else:
                if c == '1':
                    q.appendleft('1')
                    c = '0'
                else:
                    q.appendleft(b[j])
            j -= 1

        if c == '1': q.appendleft('1')
        return ''.join(q)