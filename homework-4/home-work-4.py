var = input("Уведіть текст:")
if str.isdigit(var) == True:
    var_int = int(var)
    if var_int%2 == 0:
       print("Уведене число. Число є парним")
    else:
        print("Уведене число. Число є непарним")
if str.isdigit(var) == False:
    c=len(var)
    print(f"Уведено слово. Слова має {c} букв")