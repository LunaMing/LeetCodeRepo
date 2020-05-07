def editDis(s, t):
    def recurse(m, n):
        """ 
        求最小编辑距离
        - m是s的长度
        - n是t的长度
        """
        if m == 0:
            result = n
        elif n == 0:
            result = m
        elif s[m-1] == t[n-1]:
            result = recurse(m-1, n-1)
        else:
            replaceDis = 1+recurse(m-1, n-1)
            insertDis = 1+recurse(m, n-1)
            deleteDis = 1+recurse(m-1, n)
            result = min(replaceDis, insertDis, deleteDis)
        return result
    return recurse(len(s), len(t))

print(editDis("a cat", "the cats"))
