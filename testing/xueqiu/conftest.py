import pytest


@pytest.fixture()
def conn_db():
    print("完成 数据库连接aaa")
    yield "database"
    print("关闭 数据库连接aaa")


# fixture 类似 setUp，tearDown 功能，但比 setUp，tearDown 更灵活
@pytest.fixture(scope="function")
def login():
    # setup 操作
    print("登录操作")
    # yield 相当于 return 操作
    yield ['tom', '123456']
    # teardown 操作
    print("登出操作")



