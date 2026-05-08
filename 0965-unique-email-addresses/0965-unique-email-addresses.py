class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def process_email(email):
            res = []
            skip = False
            t = email.split('@')

            for char in t[0]:
                if char == '.': continue
                elif char == '+': break
                res.append(char)
            
            res.append('@')
            res.append(t[-1])
            return ''.join(res)

        st = set()
        for email in emails:
            print(process_email(email))
            st.add(process_email(email))
            

        return len(st)