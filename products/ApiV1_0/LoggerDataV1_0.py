import logging
import datetime
import json
logger = logging.getLogger(__name__)
from django.conf import settings
import sys,inspect
import uuid


def LogDataV1_0(serverName,priIp,pubIp,apiName,result,request):
    '''
    :param serverName: contains server name
    :param priIp: contains private ip of the user
    :param pubIp: contains public ip of the user
    :param apiName: contains the name of Api from which logger is called
    :param result: contains the outcome, or error if any
    :param request: Contains all the parameter send by the user
    :return: None
    '''

    log_id = str(uuid.uuid4())

    dateTime=str(datetime.datetime.today())
    if "Image"  in request:
        request['Image']=str(request['Image'])
    if "File" in request:
        request['File']=str(request['File'])

    paraData=json.dumps(request)
    errorInfo = sys.exc_info()
    errorMessage = ""
    if errorInfo[2] is not None:
        errorMessage = "Error at lineNumber:"+ str(errorInfo[2].tb_lineno)+ str(errorInfo[0])+ str(errorInfo[1])
    logger = logging.getLogger(__name__)
    logger.info(
        '{"Log_Id":"%s","ServerName":"%s","Date":"%s","PrivateIP":"%s","PublicIP":"%s","ApiName":"%s","Result":"%s","ParameterData":%s}',
        log_id, serverName, dateTime, priIp, pubIp, apiName, errorMessage + str(result), str(paraData))
        
    return log_id


def Debug(*args):
    '''
    This is created to display messages in console during development.
    It will be displayed if this server is running locally,so it won't get displayed
    in server logs.
    :Author: Rakesh
    :param args: Takes multiple parameters and prints them all.
    :return: None
    '''
    if settings.SERVER_TYPE == "Curriculum-Dev":
        '''
        It will display error linenumber if called from (try-except) except.
        '''
        errorInfo = sys.exc_info()
        if errorInfo[2] is not None:
            print ("Error at lineNumber:", str(errorInfo[2].tb_lineno), str(errorInfo[0]), str(errorInfo[1]))
        for i in args:
            print (i),
        print ("")
    return
