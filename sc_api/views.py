# views.py
import json
import pymysql
from django.http import HttpResponse
from rest_framework import viewsets
from django.shortcuts import render,redirect
import logging

logger = logging.getLogger(__name__)

from .serializers import *


def RunQuery(query):
    conn = pymysql.connect(host='134.209.159.4', port=3366, user='root', passwd='MintAdz@1234', db='cric',autocommit=True)
    cur = conn.cursor()

    cur.execute(query)

    result = cur.fetchall()
    conn.close()
    print(result)
    #conn.autocommit(True)
    return (result)

def login(request):
        if request.method == "GET":
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print(body)
            phone = body["uid"]
            password = body["pwd"]
            query = '''select u2.n_usrmta_token,u.b_usr_blckd   from users u , usrmta u2 where u.c_usr_ph = "''' + phone + '''" and u.c_usr_pwd = "''' + password + '''" and u.n_usr_id = u2.n_usrmta_usr_id  ;'''
            print(query)
            token = RunQuery(query)

            if len(token) == 0:
                result = {
                "code": 1,
                "msg":
                "Invalid Credentials Provided"
            }
                #logger.log('Invalid Credentials Provided', phone)
                return HttpResponse(json.dumps(result), content_type='application/json')
            elif len(token[0][0]) > 5 and token[0][1]==0:
                result = {
                            "code": 1,
                            "msg": "Login Successful",
                            "data": {
                                "token": token[0][0]
                            }
                        }
                return HttpResponse(json.dumps(result), content_type='application/json')
            elif len(token[0][0]) > 5 and token[0][1]==1:
                result = {
                         "code" : 1,
                         "msg"  : "You have been Blocked!"
                        }

                return HttpResponse(json.dumps(result), content_type='application/json')
        elif request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print(body)
            return HttpResponse(json.dumps(body), content_type='application/json')


def forgot_password(request):
    if request.method == "GET":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        phone = body["uid"]
        query = '''select u2.n_usrmta_token,u.b_usr_blckd   from users u , usrmta u2 where u.c_usr_ph = "''' + phone + '''" and u.n_usr_id = u2.n_usrmta_usr_id  ;'''
        print(query)
        token = RunQuery(query)
        if len(token)==0:
            result = {
                    "code": 1,
                    "msg":
                        "Token Not Available"
                }
            return HttpResponse(json.dumps(result), content_type='application/json')
        elif len(token[0][0]) > 5 and token[0][1] == 0:
            result = {
 "code" : 1,
 "msg"  : "Please enter the OTP sent to your account",
 "data" : {
  "token" : token[0][0]
 }
}

            return HttpResponse(json.dumps(result), content_type='application/json')
        elif len(token[0][0]) > 5 and token[0][1] == 1:
            result = {
                "code": 1,
                "msg": "You have been Blocked!"
            }

            return HttpResponse(json.dumps(result), content_type='application/json')
    elif request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        return HttpResponse(json.dumps(body), content_type='application/json')

def validate_OTP(request):
    if request.method == "GET":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)

        resend = 0
        try:
            phone = body["uid"]
            token = body["token"]
            query = '''select u2.n_usrmta_token  from users u , usrmta u2 where u.c_usr_ph = "''' + phone + '''"  and u.n_usr_id = u2.n_usrmta_usr_id  and u2.n_usrmta_token ="''' + token + '''";'''
            print(query)
            token = RunQuery(query)
            resend = body["resend"]
            if resend == 1:
                if len(token)==0:
                    result = {
                             "code" : 2,
                             "msg"  : "You have reached the maximum number of times an OTP can be sent to this number, please try again after sometime"
                            }

                    return HttpResponse(json.dumps(result), content_type='application/json')
                elif len(token[0][0]) > 5:
                    result = {
                             "code" : 1,
                             "msg" : "Please enter your new password",
                             "data" :{
                              "token" : token[0][0]
                             }
                            }


                    return HttpResponse(json.dumps(result), content_type='application/json')
                elif len(token[0][0]) > 5 and token[0][1] == 1:
                    result = {
                        "code": 1,
                        "msg": "You have been Blocked!"
                    }

                    return HttpResponse(json.dumps(result), content_type='application/json')
        except KeyError:
            phone = body["uid"]
            otp = str(body["otp"])
            token = body["token"]
            query = '''select u2.n_usrmta_token  from users u , usrmta u2 where u.c_usr_ph = "''' + phone + '''"  and u.n_usr_id = u2.n_usrmta_usr_id  and u2.n_usrmta_otp_nd = ''' + otp + ''' and u2.n_usrmta_token ="''' + token + '''";'''
            print(query)
            token = RunQuery(query)
            if len(token)==0:
                result = {
                         "code" : 2,
                         "msg"  : "OTP Invalid, Please enter again"
                        }

                return HttpResponse(json.dumps(result), content_type='application/json')
            elif len(token[0][0]) > 5:
                result = {
                         "code" : 1,
                         "msg" : "Please enter your new password",
                         "data" :{
                          "token" : token[0][0]
                         }
                        }


                return HttpResponse(json.dumps(result), content_type='application/json')
            elif len(token[0][0]) > 5 and token[0][1] == 1:
                result = {
                    "code": 1,
                    "msg": "You have been Blocked!"
                }

                return HttpResponse(json.dumps(result), content_type='application/json')
    elif request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        return HttpResponse(json.dumps(body), content_type='application/json')

def New_Password(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        phone = body["uid"]
        pwd = body["pwd"]
        token = body["token"]
        query = '''update users set c_usr_pwd = "'''+pwd+'''" where c_usr_ph = "'''+phone+'''" and n_usr_id in (select n_usrmta_usr_id from usrmta where n_usrmta_token = "'''+token+'''");'''
        print(query)
        token = RunQuery(query)
        print(token)

        result = {
                 "code" : 1,
                 "msg"  : "Password Changed! Please login Again"
                }

        return HttpResponse(json.dumps(result), content_type='application/json')

    elif request.method == "GET":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        return HttpResponse(json.dumps(body), content_type='application/json')


def generate_access_token():
    import random, string
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=13))
    return x


def Signup(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        phone = body["phone"]
        #query = '''select u2.n_usrmta_token  from users u , usrmta u2 where u.c_usr_ph = "'''+phone+'''"  and u.n_usr_id = u2.n_usrmta_usr_id  ;'''
        #print(query)
        #token = RunQuery(query)
        #print(token)
        access_token = generate_access_token()

        result = {
                 "code" : 1,
                 "msg"  : "Please complete your profile!",
                 "data"  :{
                  "token" : generate_access_token(),
                 "filledSet": {"name": "phone_number", "value": phone}
                 }
                }


        return HttpResponse(json.dumps(result), content_type='application/json')

    elif request.method == "GET":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        return HttpResponse(json.dumps(body), content_type='application/json')

def SignupInit(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        name = body["name"]
        phone = body["phone"]
        email = body["email"]
        pwd = body["pwd"]
        dob = body["dob"]
        gender = body["gender"]
        size = body["size"]
        token = body["token"]
        #query = '''select u2.n_usrmta_token  from users u , usrmta u2 where u.c_usr_ph = "'''+phone+'''"  and u.n_usr_id = u2.n_usrmta_usr_id  ;'''
        #print(query)
        #token = RunQuery(query)
        #print(token)
        access_token = generate_access_token()
        #Insert Query is missing
        result = {
                 "code" : 1,
                 "msg"  : "Please enter the OTP sent to your account",
                 "data" : {
                  "token" : access_token
                 }
                }



        return HttpResponse(json.dumps(result), content_type='application/json')

    elif request.method == "GET":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        return HttpResponse(json.dumps(body), content_type='application/json')




def show(request):
    if request.method == "GET":
        studentsrole = Student.Get_data(Student)
        print("########################",studentsrole,'##########################')
        return HttpResponse(json.dumps(studentsrole),content_type='application/json')
        #return render(request,"show.html",{'student':studentsrole})
    elif request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        return HttpResponse(json.dumps(body), content_type='application/json')
