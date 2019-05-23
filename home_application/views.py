# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt


def home(request):
    """
    首页
    """
    return render(request, 'home_application/home.html')

def hello(request):
    return HttpResponse('Hello World!')

def params_test(request):
    q = ""
    str = request.GET.get('str','')
    if str == 'Hello Blueking':
        q = 'Congratulation'
    return HttpResponse('<input name=str>回答'+q)

def runapi(request):
    payload={
        "bk_app_code": "q2100804",
        "bk_app_secret": "e9ed3c82-3ec1-415a-a382-7a7a17c73fe5",
        "bk_token": "xxx",
        "bk_biz_id": 1,
        "bk_job_id": 100,
        "global_vars": [
            {
                "id": 436,
                "custom_query_id": [
                    "3",
                    "5",
                    "7"
                ],
                "ip_list": [
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.1"
                    },
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.2"
                    }
                ]
            },
            {
                "id": 437,
                "value": "new String value"
            }
        ],
        "steps": [{
            "script_timeout": 1000,
            "script_param": "aGVsbG8=",
            "ip_list": [
                {
                    "bk_cloud_id": 0,
                    "ip": "10.0.0.1"
                },
                {
                    "bk_cloud_id": 0,
                    "ip": "10.0.0.2"
                }
            ],
            "custom_query_id": [
                "3"
            ],
            "script_id": 1,
            "script_content": "ZWNobyAkMQ==",
            "step_id": 200,
            "account": "root",
            "script_type": 1
        },
            {
                "script_timeout": 1003,
                "ip_list": [
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.1"
                    },
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.2"
                    }
                ],
                "custom_query_id": [
                    "3"
                ],
                "script_id": 1,
                "script_content": "ZWNobyAkMQ==",
                "step_id": 1,
                "db_account_id": 31
            },
            {
                "file_target_path": "/tmp/[FILESRCIP]/",
                "file_source": [
                    {
                        "files": [
                            "/tmp/REGEX:[a-z]*.txt"
                        ],
                        "account": "root",
                        "ip_list": [
                            {
                                "bk_cloud_id": 0,
                                "ip": "10.0.0.1"
                            },
                            {
                                "bk_cloud_id": 0,
                                "ip": "10.0.0.2"
                            }
                        ],
                        "custom_query_id": [
                            "3"
                        ]
                    }
                ],
                "ip_list": [
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.1"
                    },
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.2"
                    }
                ],
                "custom_query_id": [
                    "3"
                ],
                "step_id": 2,
                "account": "root"
            }]
    }

    url = 'http://job.class.o.qcloud.com/api/c/compapi/v2/job/execute_job/'
    r = requests.post(url, data=json.dumps(payload))
    return  HttpResponse(r)

