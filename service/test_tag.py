import datetime

import pytest
from jsonpath import jsonpath

from service.tag import Tag

class TestTag:
    def setup_class(self):
        self.tag = Tag()

    @pytest.mark.parametrize("tag_id,tag_name",[
        ['etqI2XOgAABSECf1lhb59xeKRDOqHqMw','tag1_new'],
        ['etqI2XOgAABSECf1lhb59xeKRDOqHqMw','tag1_中文'],
        ['etqI2XOgAABSECf1lhb59xeKRDOqHqMw','tag1[中文]']
    ])
    def test_tag_list(self,tag_id,tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        tag = Tag()
        r = self.tag.list()
        r = self.tag.update(
            id=tag_id,
            tag_name=tag_name
        )
        r = self.tag.list()
        # tags = [
        #     tag
        #     for group in r.json()['tag_group'] if group['group_name'] == group_name
        #     for tag in group['tag'] if tag['name'] == tag_name
        # ]
        # assert tags != []

        assert jsonpath(r.json(), f"$..[?(@.name =='{tag_name}')]")[0]['name'] == tag_name
