__author__ = 'ags7kor'

def listPath(top,length,current,path):
    if length==0:
        return
    for i in top[current-1]:
        if current==length:
            print path+[i]
        else:
            listPath(top,length,current+1,path+[i])


def listPath1(top,length,current,path):
    if length==0:
        return
    for i in top[current-1]:
        path.append(i)
        if current==length:
            print path
        else:
            listPath1(top,length,current+1,path)
        path.remove(i)



if __name__ == '__main__':
    top=[[1,2,3],[4,5],[6,7,8,9]]

    listPath(top,len(top),1,[])

    print "\n\n"

    listPath1(top,len(top),1,[])
