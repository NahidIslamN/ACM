def quick_sort(sequence):
    length=len(sequence)
    if length<=1:
        return sequence
    else:
        privot=sequence.pop()
        Left=[]
        Right=[]
        for item in sequence:
            if item<=privot:
                Left.append(item)
            else:
                Right.append(item)
    return quick_sort(Left) + [privot] + quick_sort(Right)
print(quick_sort([20,30,5,47,85,3]))
                
