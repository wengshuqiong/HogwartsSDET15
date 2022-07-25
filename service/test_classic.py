import json

import requests


def test_tag_list():
    # access_token是企业后台去企业微信的后台获取信息时的重要票据，由corpid和secret产生。
    # 所有接口在通信时都需要携带此信息用于验证接口的访问权限
    corpid = 'wwc74c7f914eace21d'
    corpsecret = 'uzGX5dtr8g72fPmpSYpgYRZqj7ikPMmbsRbSMrWrNVE'
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid':corpid,'corpsecret':corpsecret}
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    token=r.json()['access_token']

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
