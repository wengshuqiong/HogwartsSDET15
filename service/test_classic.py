import datetime
import json

import requests


def test_tag_list():
    # access_token是企业后台去企业微信的后台获取信息时的重要票据，由corpid和secret产生。
    # 所有接口在通信时都需要携带此信息用于验证接口的访问权限
    corpid = 'wwc74c7f914eace21d'
    corpsecret = 'uzGX5dtr8g72fPmpSYpgYRZqj7ikPMmbsRbSMrWrNVE'
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': corpid, 'corpsecret': corpsecret}
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    token = r.json()['access_token']

    # 获取企业标签库，企业可通过此接口获取企业客户标签详情。
    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
        params={"access_token": token},
        json={
            'tag_id': []
        }
    )

    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    # 编辑企业客户标签
    tag_name = 'tag1_new' + str(datetime.datetime.now().strftime("%Y%m%d%H%M"))
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
        params={"access_token": token},
        json={
            'id': 'etqI2XOgAABSECf1lhb59xeKRDOqHqMw',
            'name': tag_name
        }
    )

    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    # 获取企业标签库，判断编辑企业客户标签是否成功
    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
        params={"access_token": token},
        json={
            'tag_id': []
        }
    )

    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    tags = [
        tag
        for group in r.json()['tag_group'] if group['group_name'] == 'wsq'
        for tag in group['tag'] if tag['name'] == tag_name
    ]
    assert tags != []
