import requests

def OnSite():
    '''Check if website is connected to internet'''
    try:
        requests.get("http://www.emiralp.site")
        return True
    
    except requests.ConnectionError:
        return False

if OnSite():
    print("Internet Access")

else:
    print('No Internet')