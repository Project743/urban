def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
# inner_function() данная функция определена внутри функции test_function и не может быть вызвана из вне
