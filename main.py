import json
import os
import time
import random
from datetime import datetime

import pytz
import requests

userid = os.getenv("USERID")
password = os.getenv("PASSWORD")
push_token = os.getenv("PUSH")
url_range = os.getenv("RANGE").split('-', 1)
req = requests.Session()
log = []
doc_url = [
    # Chapters 1, 2, and 3 Material (1-6)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182494-dt-content-rid-56849823_1/xid-56849823_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182494-dt-content-rid-56849824_1/xid-56849824_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182494-dt-content-rid-56849827_1/xid-56849827_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182494-dt-content-rid-56849843_1/xid-56849843_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182494-dt-content-rid-57645518_1/xid-57645518_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182494-dt-content-rid-58084472_1/xid-58084472_1",
    # Chapter 4 Material (7-10)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182495-dt-content-rid-56849340_1/xid-56849340_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182495-dt-content-rid-57645522_1/xid-57645522_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182495-dt-content-rid-57645523_1/xid-57645523_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182495-dt-content-rid-58103610_1/xid-58103610_1",
    # Chapter 5 Material (11-13)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182497-dt-content-rid-56849341_1/xid-56849341_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182497-dt-content-rid-57645548_1/xid-57645548_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182497-dt-content-rid-57645549_1/xid-57645549_1",
    # Chapter 6 Material (14-22)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182499-dt-content-rid-56849822_1/xid-56849822_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182499-dt-content-rid-57645584_1/xid-57645584_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182499-dt-content-rid-57645585_1/xid-57645585_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182499-dt-content-rid-57645586_1/xid-57645586_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182499-dt-content-rid-57645587_1/xid-57645587_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182499-dt-content-rid-58202213_1/xid-58202213_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182499-dt-content-rid-58265612_1/xid-58265612_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182499-dt-content-rid-58361777_1/xid-58361777_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182499-dt-content-rid-58475690_1/xid-58475690_1",
    # Chapter 7 Material (23-28)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182502-dt-content-rid-56849344_1/xid-56849344_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182502-dt-content-rid-56849345_1/xid-56849345_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182502-dt-content-rid-57645597_1/xid-57645597_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182502-dt-content-rid-57645598_1/xid-57645598_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182502-dt-content-rid-58663940_1/xid-58663940_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182502-dt-content-rid-58727664_1/xid-58727664_1",
    # Examination 1 Study Material (29-35)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182505-dt-content-rid-56849366_1/xid-56849366_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182505-dt-content-rid-56849367_1/xid-56849367_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182505-dt-content-rid-56849371_1/xid-56849371_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182505-dt-content-rid-56849372_1/xid-56849372_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182505-dt-content-rid-56849817_1/xid-56849817_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182505-dt-content-rid-56849840_1/xid-56849840_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182505-dt-content-rid-57645901_1/xid-57645901_1",
    # Chapter 11 Material (36-44)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182506-dt-content-rid-56849346_1/xid-56849346_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182506-dt-content-rid-56849347_1/xid-56849347_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182506-dt-content-rid-56849348_1/xid-56849348_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182506-dt-content-rid-56849349_1/xid-56849349_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182506-dt-content-rid-56849350_1/xid-56849350_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182506-dt-content-rid-56849351_1/xid-56849351_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182506-dt-content-rid-56849352_1/xid-56849352_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182506-dt-content-rid-57748354_1/xid-57748354_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182506-dt-content-rid-57748355_1/xid-57748355_1",
    # Chapter 12 Material (45-53)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182514-dt-content-rid-56849353_1/xid-56849353_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182514-dt-content-rid-56849354_1/xid-56849354_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182514-dt-content-rid-56849355_1/xid-56849355_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182514-dt-content-rid-56849790_1/xid-56849790_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182514-dt-content-rid-56849834_1/xid-56849834_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182514-dt-content-rid-56849838_1/xid-56849838_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182514-dt-content-rid-56849839_1/xid-56849839_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182514-dt-content-rid-57757767_1/xid-57757767_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182514-dt-content-rid-57757768_1/xid-57757768_1",
    # Examination 2 Study Material (54-61)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182518-dt-content-rid-56849368_1/xid-56849368_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182518-dt-content-rid-56849369_1/xid-56849369_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182518-dt-content-rid-56849373_1/xid-56849373_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182518-dt-content-rid-56849381_1/xid-56849381_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182518-dt-content-rid-56849832_1/xid-56849832_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182518-dt-content-rid-56849841_1/xid-56849841_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182518-dt-content-rid-56849842_1/xid-56849842_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182518-dt-content-rid-57759991_1/xid-57759991_1",
    # Chapter 8 Material (62-67)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182519-dt-content-rid-56849357_1/xid-56849357_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182519-dt-content-rid-56849358_1/xid-56849358_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182519-dt-content-rid-56849836_1/xid-56849836_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182519-dt-content-rid-56849837_1/xid-56849837_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182519-dt-content-rid-57759091_1/xid-57759091_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182519-dt-content-rid-57759092_1/xid-57759092_1",
    # Chapter 9 Material (68-71)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182522-dt-content-rid-56849359_1/xid-56849359_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182522-dt-content-rid-56849360_1/xid-56849360_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182522-dt-content-rid-57759986_1/xid-57759986_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182522-dt-content-rid-57759987_1/xid-57759987_1",
    # Examination 3 Study Material (72-73)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182525-dt-content-rid-56849374_1/xid-56849374_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182525-dt-content-rid-57759992_1/xid-57759992_1",
    # Chapter 10 Material (74-80)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182526-dt-content-rid-56849361_1/xid-56849361_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182526-dt-content-rid-56849362_1/xid-56849362_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182526-dt-content-rid-56849363_1/xid-56849363_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182526-dt-content-rid-56849364_1/xid-56849364_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182526-dt-content-rid-56849365_1/xid-56849365_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182526-dt-content-rid-57760555_1/xid-57760555_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182526-dt-content-rid-57760556_1/xid-57760556_1",
    # Past Final Examinations and Solutions (81-94)
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-56849370_1/xid-56849370_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-56849375_1/xid-56849375_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-56849376_1/xid-56849376_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-56849377_1/xid-56849377_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-56849378_1/xid-56849378_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-56849379_1/xid-56849379_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-56849380_1/xid-56849380_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-56849710_1/xid-56849710_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-56849818_1/xid-56849818_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-56849818_1/xid-56849818_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-56849819_1/xid-56849819_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-56849820_1/xid-56849820_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-56849821_1/xid-56849821_1",
    "https://blackboard.stonybrook.edu/bbcswebdav/pid-6182532-dt-content-rid-57759996_1/xid-57759996_1"
]


def get_mid_str(s, start_str, stop_str):
    start_pos = s.find(start_str)
    if start_pos == -1:
        return None
    start_pos += len(start_str)
    stop_pos = s.find(stop_str, start_pos)
    if stop_pos == -1:
        return None
    return s[start_pos:stop_pos]


def get_time():
    now = datetime.now(tz=pytz.timezone('US/Eastern'))
    fmt = '%Y-%m-%d %H:%M:%S %Z: '
    return now.strftime(fmt)


def get_nonce():
    url = "https://blackboard.stonybrook.edu/webapps/login/"

    headers = {
        'Host': 'blackboard.stonybrook.edu',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Referer': 'https://blackboard.stonybrook.edu/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': "zh-CN,zh;q=0.9"
    }
    result = req.get(url, headers=headers)
    return get_mid_str(result.text,
                       "<input type=\'hidden\' name=\'blackboard.platform.security.NonceUtil.nonce\' value=\'",
                       "\'>")


def login(nonce):
    url = "https://blackboard.stonybrook.edu/webapps/login/"

    headers = {
        'Host': 'blackboard.stonybrook.edu',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '\"Microsoft Edge\";v=\"93\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"93\"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Origin': 'https://blackboard.stonybrook.edu',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Referer': 'https://blackboard.stonybrook.edu/webapps/login/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }

    body = "user_id=" + userid + \
           "&password=" + password + \
           "&login=Login" \
           "&action=login" \
           "&new_loc=" \
           "&blackboard.platform.security.NonceUtil.nonce=" + nonce

    result = req.post(url=url, headers=headers, data=body)
    welcome = get_mid_str(result.text, "<title>", "&ndash; Blackboard Learn</title>")
    if welcome is None:
        return False
    log.append(get_time() + "Login successful, " + welcome)
    print(get_time() + "Login successful, " + welcome)
    return True


def request_doc(url):
    headers = {
        'Host': 'blackboard.stonybrook.edu',
        'Connection': 'keep-alive',
        'sec-ch-ua': '\"Microsoft Edge\";v=\"93\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"93\"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '\"Windows\"',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Referer': 'https://blackboard.stonybrook.edu/webapps/blackboard/content/listContent.jsp?course_id=_1233729_1'
                   '&content_id=_6129737_1&mode=reset',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }

    result = req.get(url, headers=headers)
    if result.status_code != 200:
        log.append(get_time() + "ERROR CODE: " + str(result.status_code))
        print(get_time() + "ERROR CODE: " + str(result.status_code))
        return False
    return True


def push_message(log_list):
    content = ""
    for i in log_list:
        content += i + "  \n"

    title = 'Click 315'

    # ServerChan
    if push_token[0:3] == "SCT":
        url = 'https://sctapi.ftqq.com/' + push_token + '.send'
        body = {
            "title": title,
            "desp": content
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    # Push Plus Plus
    else:
        url = 'http://www.pushplus.plus/send'
        data = {
            "token": push_token,
            "title": title,
            "content": content,
            "template": "markdown"
        }
        headers = {'Content-Type': 'application/json'}
        body = json.dumps(data).encode(encoding='utf-8')

    result = requests.post(url, data=body, headers=headers)

    if result.status_code == 200:
        text = json.loads(result.text)
        if text["code"] == 200:
            print(get_time() + "Push message successful")
        elif text["code"] == 0:
            print(get_time() + "Push message successful")
        else:
            print(get_time() + "Push message failed." + " Message: " + result.text)

    else:
        print(get_time() + "Push message failed." + " Message: " + result.text)


def start_request():
    success = 0
    fail = 0
    log.append(get_time() + "Click url " + url_range[0] + " to " + url_range[1])
    print(get_time() + "Click url " + url_range[0] + " to " + url_range[1])

    for i in range(int(url_range[0]) - 1, int(url_range[1])):
        sleep = random.randint(30, 180)
        log.append(get_time() + "sleep " + str(sleep) + " second")
        print(get_time() + "sleep " + str(sleep) + " second")
        time.sleep(sleep)

        log.append(get_time() + "Processing URL " + str(i + 1) + "...")
        print(get_time() + "Processing URL " + str(i + 1) + "...")
        try:
            if request_doc(doc_url[i]):
                success += 1
            else:
                log.append(get_time() + "ERROR URL: " + doc_url[i])
                print(get_time() + "ERROR URL: " + doc_url[i])
                fail += 1
        except requests.exceptions.ConnectionError as e:
            fail += 1
            log.append(get_time() + str(e))
            log.append(get_time() + "ERROR URL: " + doc_url[i])
            print(get_time() + str(e))
            print(get_time() + "ERROR URL: " + doc_url[i])
    log.append(get_time() + "Total success: " + str(success) + ", failed: " + str(fail))
    print(get_time() + "Total success: " + str(success) + ", failed: " + str(fail))


if __name__ == '__main__':
    if login(get_nonce()):
        start_request()
    else:
        log.append(get_time() + "Login Failed")
        print(get_time() + "Login Failed")

    if push_token is not None:
        push_message(log)
