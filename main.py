def delna3(chislo:int):
    return True if chislo % 3==0 else False
def delna100(chislo):
    res=None
    stroka="введено не число"
    if not(isinstance(chislo,str)):
        try:
            res=100/chislo
        except ValueError:
            print("Число введено неправильно")
        except floatingPointError:
                print("ошибка")
        except ZeroDivisionError:
            print("деление ноль")
        except Exception:
                print("ошибка")
        return res
    else:
        return stroka

def magdate(date):
    if isinstance(date,str):
        try:
            date=date.split("/")
            if int(date[0])*int(date[1])==int(date[2][2:]):
                return True
            else:
                return False
        except Exception:
            print("ошибка")
    else:
        print("введена не строка")

def billetic(billc):
    try:
        if isinstance(billc,str):
            sum1=int(billc[0])+int(billc[1])+int(billc[2])
            sum2=int(billc[3])+int(billc[4])+int(billc[5])
            if sum1==sum2:
                return True
            else:
                return False
        else:
            print("ошибка")
    except Exception:
        return False








if __name__ == "__main__":
    print("проверка деления\n")
    print(delna3(15))
    print(delna3(2),"\n")

    print("проверка деления 100\n")
    print(delna100("sadas"))
    print(delna100(10.333))

    print("дата\n")
    print(magdate("22/01/2022"))
    print(magdate("22/02/2022"))

    print("Билет\n")
    print(billetic("555555"))
    print(billetic("321777"))