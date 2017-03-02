def f(lst):
    tmp=[0,0,0]
    for i in lst:
        if i==0:
            tmp[0]+=1
        elif i==1:
            tmp[1]+=1
        elif i==2:
            tmp[2]+=1

    for i in range(len(lst)):
        if tmp[0]!=0:
            lst[i]=0
            tmp[0]-=1
        elif tmp[1]!=0:
            lst[i]=1
            tmp[1]-=1
        elif tmp[2]!=0:
            lst[i]=2
            tmp[2]-=1

    return lst


def main():
    print(f([1, 2, 2, 0]))


if __name__ == '__main__':
    main()
