from iwmac import IWMAC;
import hashlib        #! Usage: md5 cryptograms

"""
@brief this file explores different API-calls to the IWMACs API-interface
@author winns.no
"""

def testCase_getautetnication_token(CONFIG_NAME_COMPANY_FACILITY, CONFIG_KEY_AFTER_MD5, CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT):
  #! Get autetnication-token to be used.
  # TODO: write unit-tests for this.
  try:
    obj = IWMAC(CONFIG_NAME_COMPANY_FACILITY, CONFIG_KEY_AFTER_MD5);
    if(obj.token != None):
      print("OK\t Authentication worked");
      print("\t(info)\t token:\t{}".format(obj.token));
      CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT = obj.token; #! ie, update the global variable; #! Note: this step is not enssary (as the object itself cna be used direclty). However, for the sake of teaching, it is usefull to exmeplify how an object can 'be itnaited from scatch' without of applying the aututciaotn-step every time.
      return CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT;
    else:
      print('!!\t Error! Unable to authenticate: token NOT set in this update-procedure');
  except Exception as e:
    print('!!\t Error! Unable to authenticate');
    print(e);
    #! Src: https://stackoverflow.com/questions/1278705/when-i-catch-an-exception-how-do-i-get-the-type-file-and-line-number
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)


def testCase_applQuery_results_latest(CONFIG_NAME_COMPANY_FACILITY, CONFIG_KEY_AFTER_MD5, CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT): #! Apply query: get latest results
  #! TODO: update below query-spec to reflect your own data-set.
  # TODO: write unit-tests for this.
  print(" --- in-func");
  try:
    print(".-------------- {}".format(CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT));
    obj = IWMAC(CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT = CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT); #! ie, use the external vairlbe to set the tken, a token used in the atuciation-part.
    if(obj.token != None):
      print("OK\t Authentication worked");
      print("\t(info)\t token:\t{}".format(obj.token));
      #!
      #! Apply Logics:
      url = IWMAC.SearchType.QUERY_LATEST; #! the type of search (ie, search-class) to apply.
      query = {
        "plant_id": 5844, #! is unqieu for every faciity
        #"num_values": 1,
        "timestamp" : [1610965897685,  	1610127420000,  	1610965897672,  	1610458877000,  	1610459207984], #! ie, the unix-time-stamp; for concrete examples, see the "datetime, time" examples (provided in relationship with this IWMAC tutorial).
        #"timestamp": [1610127420000],
        "parameters": [3,4, 5] #! IDs which reflect a givne failtiies equipmetn-setup.
      };
      #!
      #! The call:
      data = obj.fetch_data(url, query);
      # FIXEM: udapte aobf e with ar eturn-valeu ... 
      if(data != None):
        print("OK: Result:");
        #!
        if(True): #! then apply  a generic JSON->digestable text for this data-fetch-result:
          #! Example (of possible data to receive): {'3': {'data_count': 1, 'x': [1610127420], 'y': ['0.00']}, '4': {'data_count': 1, 'x': [1610459219], 'y': ['0.00']}, '5': {'data_count': 1, 'x': [1605713039], 'y': ['']}}
          for k, v in data.items():
            print("[{}] = {}".format(k, v));
      else:
        print('!!\t Error! Was not able to fetch result for this query, given:');
        print(url);
        print(data);
        print(query);        
        print(obj.token);        
    else:
      print('!!\t Error! Unable to authenticate');
  except Exception as e:
    print('!!\t Error! Unable to authenticate, given');
    print(e);


def testCase_applQuery_results_nearest(CONFIG_NAME_COMPANY_FACILITY, CONFIG_KEY_AFTER_MD5, CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT): #! Apply query: get nearest results
  #! TODO: update below query-spec to reflect your own data-set.
  # TODO: write unit-tests for this.
  try:
    print(".-------------- {}".format(CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT));
    obj = IWMAC(CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT = CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT); #! ie, use the external vairlbe to set the tken, a token used in the atuciation-part.
    if(obj.token != None):
      print("OK\t Authentication worked");
      print("\t(info)\t token:\t{}".format(obj.token));
      #!
      #! Apply Logics:
      url = IWMAC.SearchType.QUERY_NEAREST; #! the type of search (ie, search-class) to apply.
      query = {
        "plant_id": 5844,
        #"num_values": 1,
        "timestamp" : [1610965897685,  	1610127420000,  	1610965897672,  	1610458877000,  	1610459207984], #! ie, the unix-time-stamp; for concrete examples, see the "datetime, time" examples (provided in relationship with this IWMAC tutorial).
        #"timestamp": [1610127420000],
        "parameters": [3,4, 5] #! IDs which reflect a givne failtiies equipmetn-setup.
      };
      #!
      #! The call:
      data = obj.fetch_data(url, query);
      # FIXEM: udapte aobf e with ar eturn-valeu ... 
      if(data != None):
        print("OK: Result:");
        #!
        if(True): #! then apply  a generic JSON->digestable text for this data-fetch-result:
          #! Example (of possible data to receive): {'3': {'data_count': 1, 'x': [1610127420], 'y': ['0.00']}, '4': {'data_count': 1, 'x': [1610459219], 'y': ['0.00']}, '5': {'data_count': 1, 'x': [1605713039], 'y': ['']}}
          for k, v in data.items():
            print("[{}] = {}".format(k, v));
      else:
        print('!!\t Error! Was not able to fetch result for this query, given:');
        print(url);
        print(data);
        print(query);        
        print(obj.token);        
    else:
      print('!!\t Error! Unable to authenticate');
  except Exception as e:
    print('!!\t Error! Unable to authenticate, given');
    print(e);


  
      



def testCase_applQuery_results_all(CONFIG_NAME_COMPANY_FACILITY, CONFIG_KEY_AFTER_MD5, CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT): #! Apply query: get all results
  #! TODO: update below query-spec to reflect your own data-set.
  # TODO: write unit-tests for this.
  try:
    #! Note: heads-up: this query-set is NOT test --- due to limtied data avaibalbe --- Expert=Josien is now validaiting this issue.
    print(".-------------- {}".format(CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT));
    obj = IWMAC(CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT = CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT); #! ie, use the external vairlbe to set the tken, a token used in the atuciation-part.
    if(obj.token != None):
      print("OK\t Authentication worked");
      print("\t(info)\t token:\t{}".format(obj.token));
      #!
      #! Apply Logics:
      url = IWMAC.SearchType.QUERY; #! the type of search (ie, search-class) to apply.
      #!
      #! Task: construct the query:
      t_to = 1611051093; #! where 'to' could be set from: " print time.time()"
      #t_from = 
      t_from = t_to - 1000; #! Note: the results does sometimes NOT work, which could be due to lack of data that none of these valeue-ranges work? <-- tried for [10, 100, 1000]
      q1 = { "plant_id": "5844", "parameters": ["3", "4"], "from": t_from, "to": t_to};
      q2 = {
        "plant_id": 5844,
        #"num_values": 1,
        "timestamp" : [1610965897685,  	1610127420000,  	1610965897672,  	1610458877000,  	1610459207984], #! ie, the unix-time-stamp; for concrete examples, see the "datetime, time" examples (provided in relationship with this IWMAC tutorial).
        #"timestamp": [1610127420000],
        "parameters": [3,4, 5] #! IDs which reflect a givne failtiies equipmetn-setup.
      };
      #!
      #! Note: below exemplfiy a batchification of the query, ie,  to apply for muliple queries using the same setupf for printing:
      for query in [q1, q2]:
        #!
        #! The call:
        data = obj.fetch_data(url, query);
        # FIXEM: udapte aobf e with ar eturn-valeu ... 
        if(data != None):
          print("OK: Result:");
          #!
          if(True): #! then apply  a generic JSON->digestable text for this data-fetch-result:
            #! Example (of possible data to receive): {'3': {'data_count': 1, 'x': [1610127420], 'y': ['0.00']}, '4': {'data_count': 1, 'x': [1610459219], 'y': ['0.00']}, '5': {'data_count': 1, 'x': [1605713039], 'y': ['']}}
            for k, v in data.items():
              print("[{}] = {}".format(k, v));
        else:
          print('!!\t Error! Was not able to fetch result for this query, given:');
          print(url);
          print(query);
          print(data);
          print(obj.token);        
    else:
      print('!!\t Error! Unable to authenticate');
  except Exception as e:
    print('!!\t Error! Unable to authenticate, given');
    print(e);




# ***********************************************************
#!
if __name__ == '__main__':
  #!
  #! PART: Local configurations:
  CONFIG_NAME_COMPANY_FACILITY         = # FIXME: set this to a value provided by IWMAC
  CONFIG_KEY_BEFORE_MD5                = # FIXME: set this to a value provided by IWMAC
  #! Note: if below proerpties are set, then the IWMAC data-fetching can be used directly, ie, without a pre-step of token identification
  CONFIG_KEY_AFTER_MD5                 = None;
  CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT = None;
  if(CONFIG_KEY_AFTER_MD5 == None):
    #! Note: mandatory in the IWMAC authetnication process. 
    #! Src: https://www.geeksforgeeks.org/md5-hash-python/
    key = hashlib.md5(CONFIG_KEY_BEFORE_MD5.encode('utf-8'));
    print("---");
    print(key);
    # printing the equivalent byte value. 
    #print("The byte equivalent of hash is : "); #, end ="") 
    print(key.hexdigest()) #! this givesn the <hash-number>, which correpsoidns to the correct IWMAC-key attribute.
    #!
    CONFIG_KEY_AFTER_MD5 = key.hexdigest();
    print("(info)\t Update(After-md5)\t CONFIG_KEY_AFTER_MD5:{}".format(CONFIG_KEY_AFTER_MD5));

  


  # --------------------------------
  if( (CONFIG_NAME_COMPANY_FACILITY == None) or  (CONFIG_KEY_AFTER_MD5 == None) or (CONFIG_KEY_AFTER_MD5 == None)  ):
    sys.exit('Minimum Configuraitons NOT propertly set: please update your script.')

    
  #!
  #!
  #! Get autetnication-token to be used.
  CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT = testCase_getautetnication_token(CONFIG_NAME_COMPANY_FACILITY, CONFIG_KEY_AFTER_MD5, CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT);
  print("CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT=", CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT);
  #!
  #!
  testCase_applQuery_results_latest(CONFIG_NAME_COMPANY_FACILITY, CONFIG_KEY_AFTER_MD5, CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT); #! Apply query: get latest results
  #!
  #!
  if(False): # FIXME: remove this false-statement when the 'lack of test-data' issue is resolved.
    testCase_applQuery_results_nearest(CONFIG_NAME_COMPANY_FACILITY, CONFIG_KEY_AFTER_MD5, CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT); #! Apply query: get nearest results
    #!
    #!
    testCase_applQuery_results_all(CONFIG_NAME_COMPANY_FACILITY, CONFIG_KEY_AFTER_MD5, CONFIG_TOKEN_GENERATED_AFTER_Md5_AUT); #! Apply query: get all results    
    
    
