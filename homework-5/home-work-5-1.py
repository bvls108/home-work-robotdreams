var = input("Уведіть текст:")
var_list = list(var)
for i in var_list:
    if str.isdigit(i) == True:
        i_N=  int(i)
        if i_N%2 == 0:
            print(f"{i} є парним числом")
        else:
            print(f"{i} є непарним числом")
    if str.isalpha(i) == True:
        if str.islower(i) == True:
            print(f"{i} є маленькою буквою")
        if str.islower(i) == False:
            print(f"{i} є великою буквою")
    else:
        if str.isdigit(i) == False and str.isalpha(i) == False:
            print(f"{i} є символом")
