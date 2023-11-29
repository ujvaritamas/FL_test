def test0(a:int, b:int)-> int:
    return a+b

def test1(n: int)->None:
    if n%2:
        print("Weird")
    elif 2<= n and n<=5:
        print("Not Weird")
    elif 6<= n and n<=20:
        print("Weird")
    else :
        print("Not Weird")