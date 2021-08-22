'''
Reverse First k Elements of Queue
'''


def reverseKelements(data:list,k:int)->list:
    rev_q = list()
    stack = list()
    for i,e in enumerate(data):
        if i<k:
            stack.append(e)
            if i==k-1:
                for j in range(len(stack)):
                    rev_q.append(stack[len(stack)-1-j])
        else:
            rev_q.append(e)

    if k>len(data):
        for j in range(len(stack)):
            rev_q.append(stack[len(stack)-1-j])


    return rev_q


if __name__ == "__main__":
    print(reverseKelements([1,2,3,4,5,6,7,8,9],0))
    print(reverseKelements([1,2,3,4,5,6,7,8,9],1))
    print(reverseKelements([1,2,3,4,5,6,7,8,9],5))
    print(reverseKelements([1,2,3,4,5,6,7,8,9],9))

    print(reverseKelements([1,2,3,4,5,6,7,8,9],10))
    print(reverseKelements([],10))