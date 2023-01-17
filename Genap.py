def contains_even_number(l):
    for ele in l:
        if ele % 2 == 0:
            print("List berisi bilangan genap")
            break
    else:
        print("List tidak berisi bilangan genap")

print("For list 1:")
contains_even_number([1,9,8])
print("\nFor list 2:")
contains_even_number([1,3,5])