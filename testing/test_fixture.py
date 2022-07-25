# @pytest.mark.usefixtures("login")
def test_case1(login):
    print(login)
    print("用例1")


def test_case2():
    print("用例2")


# 如果测试用例里，需要用到 fixture 的返回值的话，fixture 的名字需要以参数的形式传入到方法里，不能使用装饰器的方式。
def test_case3(conn_db):
    print(conn_db)
    print("用例3")
