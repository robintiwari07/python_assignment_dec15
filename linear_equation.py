def solve_for_y(x_values):
    m = 45
    c = 0.5
    for x in x_values:
        y= m *x +c
        print("the required value of y is: {0:.2f}".format(y))

x_values=[1, 2.3, 5.6, 7, 78]
solve_for_y(x_values)