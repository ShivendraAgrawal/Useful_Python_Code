__author__ = 'ags7kor'

def perm1(mylist, sol, length):
    if len(sol)==length:
        print sol
    else:
        for i in mylist:
            temp_list=mylist[:]
            temp_list.remove(i)
            sol.append(i)
            perm1(temp_list, sol, length)
            sol.remove(i)

def perm2(l):
        # Compute the list of all permutations of l
    if len(l) <= 1:
            return [l]
    r = []  # here is new list with all permutations!
    for i in range(len(l)):
            s = l[:i] + l[i+1:]
            p = perm2(s)
            for x in p:
              r.append(l[i:i+1] + x)
    return r


if __name__ == '__main__':
    a=[1,2,3,4]
    perm1(a,[], len(a))
    print "\n\n2nd Solution\n\n"
    r=perm2(a)
    for i in r:
        print i
