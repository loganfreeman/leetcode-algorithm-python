def check(degree, n):
    sum_deg = sum(degree)
    if(2*(n-1) == sum_deg):
        return True
    else:
        return False

n = 5
degree = [2, 3, 1, 1, 1];
if (check(degree, n)):
    print("Tree")
else:
    print("Graph")