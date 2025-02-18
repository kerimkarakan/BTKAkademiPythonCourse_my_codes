def sayiYazdir(baskan, by="ali" , *args): # args herhangi bir değişken # böyle herhangi bir değişken tanımlayarak istediğimiz kadar veri girebiliriz.
    print(args)
    print(type(args)) # bizim args değişkenimiz tuple bir tipe sahip
    print([*args])
    for arg in args:
        print(arg)

sayiYazdir(5,6,98,54,21)