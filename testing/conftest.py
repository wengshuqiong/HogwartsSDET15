import pytest

from pythoncode.calculator import Calculator

# scope='session' 作用于当前目录的所有文件，执行一次
@pytest.fixture(scope='session',autouse=True)
def conn_db():
    print("完成 数据库连接")
    yield "database"
    print("关闭 数据库连接")


# fixture 类似 setUp，tearDown 功能，但比 setUp，tearDown 更灵活
# params=['tom','jerry'] 参数化
@pytest.fixture(scope="function",params=['tom','jerry'])
def login(request):
    # setup 操作
    print("登录操作")
    username = request.param
    # yield 相当于 return 操作
    yield username
    # teardown 操作
    print("登出操作")


@pytest.fixture(scope="class")
def get_calc():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")



