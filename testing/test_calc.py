import pytest
import yaml


# 解析测试数据文件
def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(add_ids)
    print(add_datas)
    return [add_datas, add_ids]


# 解析测试步骤文件
def steps(addstepsfile, calc, a, b, expect):
    with open(addstepsfile) as f:
        steps = yaml.safe_load(f)

    for step in steps:
        if 'add' == step:
            print("step: add")
            result = calc.add(a, b)
        elif 'add1' == step:
            print("step: add1")
            result = calc.add1(a, b)
        assert expect == result


class TestCalc:
    # def setup_class(self):
    #     print("计算开始")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("计算结束")

    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_calc, a, b, expect):
        # calc = Calculator()
        # result = self.calc.add(a, b)
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.1, 0.2], [0.1, 0.2, 0.3]])
    def test_add_float(self, get_calc, a, b, expect):
        # result = self.calc.add(a, b)
        result = get_calc.add(a, b)
        assert round(result, 2) == expect

    # 除数为 0 的情况
    @pytest.mark.parametrize('a,b', [[0.1, 0], [10, 0]])
    def test_div_zero(self, get_calc, a, b):
        with pytest.raises(ZeroDivisionError):
            # result = self.calc.div(a, b)
            result = get_calc.div(a, b)

    def test_add_steps(self, get_calc):
        a = 1
        b = 1
        expect = 2
        steps("./steps/add_steps.yml", get_calc, a, b, expect)
        # assert 2 == self.calc.add(1, 1)
        # assert 3 == self.calc.add(1, 2)
        # assert 0 == self.calc.add(-1, 1)

    # 同时多行注释，多行选中后 ctrl + /
    # def test_add1(self):
    #     # calc = Calculator()
    #     result = self.calc.add(100, 100)
    #     assert result == 200

    # def test_add2(self):
    #     # calc = Calculator()
    #     result = self.calc.add(0.1, 0.1)
    #     assert result == 0.2
