from _mysql import IntegrityError

import datetime
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from logger import logger
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout

from pmproject.exceptions import UnAuthorizedException
from pmproject.utils import get_log_string, get_friendly_name, get_user_model


class loginUser(APIView):
    def post(self, request):
        USERMODEL = get_user_model()
        try:
            user = USERMODEL.objects.get(email=request.DATA["email"])
            if 'google' in user.sources or 'facebook' in user.sources:
                return Response({"error": "Please log in with " + ' or '.join(user.sources)}, 500)
            user = authenticate(email=request.DATA["email"], password=request.DATA["password"], type='user')
            if user is None:
                raise UnAuthorizedException("Invalid User Name or Password")
            login(request, user)
            return Response({
                "result": user.name,
                "email": user.email,
                "name": user.name,
                "mobile": user.phoneNumber,
                "success": True
            })
        except USERMODEL.DoesNotExist:
            return Response({"error": "Invalid username or password"}, 500)
        except MultiValueDictKeyError as e:
            logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
            #This exception is raised when empty username or password is sent
            return Response({"error": "Invalid username or password"}, 500)
        except UnAuthorizedException as e:
            logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
            return Response({"error": e.message}, 401)
        except Exception as e:
            logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
            return Response({"error": str(e)}, 500)

@api_view(['GET','POST'])
def logoutUser(request):
    try:
        logout(request)
        return redirect('/')
    except Exception as e:
        logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
        return Response({}, 500)

class signUpUser(APIView):
    def post(self, request, source):
        try:
            if source == 'direct':
                return sign_up_directly(request)
            else:
                return Response({"error": 'Source not recognized'}, 500)
        except MultiValueDictKeyError as ke:
            logger.error(get_log_string('error: '+str(ke),request=request),exc_info=True)
            return Response({"error": str(ke)+' is missing in the request data'}, 500)
        except Exception as e:
            logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
            return Response({"error": str(e)}, 500)

class checkUserLogin(APIView):
    def get(self, request):
        try:
            email = request.user.email
            return Response({"success":email}, 200)
        except:
            return Response({"error": "user is not logged in"}, 500)


def create_user(name, email, phone, password, source='direct', additional_info={}, is_email_subscribed=False):
    USERMODEL = get_user_model()
    try:
        print "getting "+str(email)+" user.." +str(datetime.datetime.now())
        user = USERMODEL.objects.get(email=email)
        print "got "+str(email)+"  user.." +str(datetime.datetime.now())
    except USERMODEL.DoesNotExist:
        user = None
    try:
        if user:
            if source != 'direct':
                user.sources.add(source)
                user.name = name
                user.additionalInfo[source] = additional_info
                user.set_password(password)
                print "saving  "+str(email)+" user.. " +str(datetime.datetime.now())
                user.save()
                print "saved  "+str(email)+" user.. " +str(datetime.datetime.now())
                return True, {"name": user.name, "email": user.email}
            else:
                return False, {'message': "This email id is already registered"}
        else:
            addInfo = {}
            addInfo[source] = additional_info
            user = USERMODEL.objects.create_user(email, phone, password, name, sources={source}, additionalInfo=addInfo,
                                                 user_type='user',is_email_subscribed=is_email_subscribed)
            return True, {"name": user.name, "email": user.email, "password":password}
    except IntegrityError as e:
        return False, {"message": 'User already exists'}
    except Exception as e:
        logger.error(get_log_string('error: '+str(e)),exc_info=True)
        return False, {"message": str(e)}
    pass


def sign_up_directly(request):
    try:
        success, data = create_user(request.DATA['name'], request.DATA['email'], request.DATA['phoneNumber'], request.DATA['password'], source='direct', is_email_subscribed=request.DATA.get("isSubscribed", False))
        if success:
            user = authenticate(email=data.get("email"), password=data.get("password"), type='user')
            login(request, user)
            return Response({"name":data.get("name"), "email":data.get("email")}, 200)
        else:
            return Response({"error": data['message']}, 500)
    except MultiValueDictKeyError as e:
        logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
        return Response({"error": get_friendly_name(str(e))+' is missing from the input data'}, 500)
    except Exception as e:
        logger.error(get_log_string('error: '+str(e),request=request),exc_info=True)
        return Response({"error": str(e)}, 500)