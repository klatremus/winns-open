"""
@brief exempfleis the use of IWMACs API
@remarks 
-- 200=repsonse:means OK [https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html ]
-- example: python3 tut-basic-postData-json-0.py | grep result 
-- security: IWMAC's backend uses "Bearer token" authentication [as seen from documetnation]; Token can be acquired upon request to IWMAC
"""

import sys, os        #! Usage: get line-number of a possible exception.
import requests       #! Usage: data-fetching through HTTPS
import hashlib        #! Usage: md5 cryptograms
import time;          #! Usage: mapping between Data Time Group (DTG) versus UNIX-time-stamp.
from datetime import datetime, timedelta #! Usage: mapping between Data Time Group (DTG) versus UNIX-time-stamp.
#import datetime;      #! Usage: mapping between Data Time Group (DTG) versus UNIX-time-stamp.
import json            #! Data-formatting
from enum import Enum  #! Why: simplify validity-checking of function-inputs, eg, when specifying which search-base-URL to use.


def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))




# ***********************************************************
#!


class BearerAuth(requests.auth.AuthBase):
  #! Src: https://stackoverflow.com/questions/29931671/making-an-api-call-in-python-with-an-api-that-requires-a-bearer-token 
  def __init__(self, token):
    self.token = token
  def __call__(self, r):
    r.headers["authorization"] = "Bearer " + self.token
    return r



def IWMAC_get_url_base(): return  'https://www.iwmac.net/api/v1/';

class IWMAC(object):
  """Interface to IWMAC API
  @author Ole Kristian (Winns), Erik (Winns), and Jostein (IWMAC).
  """

  class SearchType(Enum):
    """ Enumerates the queries which are supproted
    @remarks motivaiton is to simplify the support of future code-chanmges
    """
    #! Src: https://docs.python.org/3/library/enum.html & "docu/2019-09-13\ Data\ Domain\ API.pdf" (where an updated version of the latter can be provided by "jostein.markussen@iwmac.no".
    QUERY         = IWMAC_get_url_base()  +  'data/query'; # which maps into: url = 'https://www.iwmac.net/api/v1/data/query';
    QUERY_LATEST  = IWMAC_get_url_base()  +  'data/query/latest';      #! Eg, url = 'https://www.iwmac.net/api/v1/data/query/latest';
    QUERY_NEAREST = IWMAC_get_url_base() +  'data/query/nearest';
    # TODO: add more query-types
    #QUERY_  = IWMAC_get_url_base() + '';
    def __str__(self):
      #! Note: this funciton ensrues that the provided URL is NOT the enum; to better unstanding this (articacT), try removing this function.
      #! Src: https://stackoverflow.com/questions/24487405/enum-getting-value-of-enum-on-string-conversion
      return str(self.value)

  def __init__(self, CONFIG_NAME_COMPANY_FACILITY = None, CONFIG_KEY_AFTER_MD5 = None, CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT = None):
    self.token = None;
    if(CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT == None):
      if(CONFIG_NAME_COMPANY_FACILITY == None):
        raise Exception("Variable NOT set for: CONFIG_NAME_COMPANY_FACILITY");
      if(CONFIG_KEY_AFTER_MD5 == None):
        raise Exception("Variable NOT set for: CONFIG_KEY_AFTER_MD5");
      #!
      #! Make the request:
      self.token = IWMAC.authenticate(CONFIG_NAME_COMPANY_FACILITY, CONFIG_KEY_AFTER_MD5);
      print("auth.token=", self.token);
    else:
      self.token = CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT; #! ie, then assume that the init-process is NOT neccsary.

  @staticmethod
  def authenticate(CONFIG_NAME_COMPANY_FACILITY, CONFIG_KEY_AFTER_MD5):
    """
    @brief fetches an updated token for the given paramter-combination
    @param "CONFIG_NAME_COMPANY_FACILITY": the name/id of the facility.
    @param "CONFIG_KEY_AFTER_MD5": the md5-version of the key; if you do not have this, then contact: "jostein.markussen@iwmac.no"
    @return either the updated token, None, or a an Exception.
    """
    url = 'https://www.iwmac.net/services/auth_service.php';
    data = [
      {
      "jsonrpc": "2.0",
        "method": "token_login",
        "params": {
          "id": CONFIG_NAME_COMPANY_FACILITY, #! eg, "WINNS_2021_TRHEIM",
          #! Note: to test for case=invalidKey, set below "key" to 'abcdf' (which, hopefully, should not work).
          "key": CONFIG_KEY_AFTER_MD5,
          "token": True
        },
        "id": 0 #! a number which is internally used by IWMAC, ie, which does not need to be set.
      }
    ];
    #!
    #! Send the request:
    r = requests.post(url, json=data);    
    #! Note: the result "r" is a hash of data, ie, strategith-foward to analsye; to see the 'raw' data, type: print(r.text)
    #!
    #! Fech the importnat data from the reutrn-object:
    json = r.json(); 
    if r.status_code == 200:
      try:
        data = json["result"];
        print("auth --- data --- ", data);
        if( (type(data) == str) or (type(data) == unicode) ): #! ie, a string:
          return data; #! ie, the token.
        else:
          print("!!\t Error! Your authentication-key='{}' (of type='{}') seems to be erronous: could this key (your are using) be out-of-date? -- To investigate this, we suggest you contact the leading expert (in this turf of science), namely: jostein.markussen@iwmac.no".format(data, str(type(data))));
      except Exception as e:
        print(json);
        print(e.message, e.args);
    elif r.status_code == 500:
      print('!!\t Error! Query did not satisfy requirements; a known case relates to the sitaution where the time-stamp-values are all to close. To investgiate this issue, the returned status code is found to be of value="%s"' % r.status_code)
      print(r);
    else:
      print('!!\t Error! Returned status code %s' % r.status_code)
      print(r);


  def fetch_data(self, url, param):    
    """
    @brief fetches the data for a given url--paramter combination
    @param "self": the object to update
    @param "url": the search-url to apply; idetnifed from: IWMAC.SearchType (eg, IWMAC.SearchType.QUERY);
    @param "param": the value-filters to be applied.
    @return a json-hash of the fetched data.
    """
    #! 
    r = requests.post(url, json=param, auth=BearerAuth(self.token)); #'3pVzwec1Gs1m'))
    #!
    #! Fech the importnat data from the reutrn-object:
    json = r.json(); 
    if r.status_code == 200:
      try:
        data = json["result"]["data"];
        return data; #! ie, the result.
      except Exception as e:
        print("!!\t Error: was not able to fetch attriubte='data', given text={}".format(r.text));
        print(json);
        print(e);
        #print(e.message, e.args);
    elif r.status_code == 500:
      print('!!\t Error! Query did not satisfy requirements; a known case relates to the sitaution where the time-stamp-values are all to close. To investgiate this issue, the returned status code is found to be of value="%s"' % r.status_code)
      print(r);
    else:
      print('!!\t Error (in the value-fetching)! Returned status code %s' % r.status_code)
      print(r);

    


