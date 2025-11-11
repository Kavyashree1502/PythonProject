PB_Glo_variable = 20  # Global variable outside the function


def my_function():
    private_variable = 10  # Local variable
    print(private_variable)
    print(PB_Glo_variable)

my_function()


print(PB_Glo_variable)
