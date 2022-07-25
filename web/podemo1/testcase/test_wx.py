from web.podemo1.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        # 添加联系人
        username = "aaaaaaa1"
        account = "aaaaaa1_hogwarts"
        phonenum = "13750009111"

        addmember = self.main.goto_addmember()
        addmember.add_member(username,account,phonenum)
        assert username in addmember.get_member()