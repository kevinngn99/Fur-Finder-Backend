import grequests
import json
import requests

class GoogleDrive:
    def get_access_token(self):
        client_id = '875756955135-8unjaedk1u56ppo6o0o6ccd0r69t1frm.apps.googleusercontent.com'
        client_secret = 'HYh0sZEB1j55q0w7HdyABtOr'
        refresh_token = '1//04AU-z4vG9KMrCgYIARAAGAQSNwF-L9IraNwNk_M9u3wX6lplbBGWQmem21ofxuCphUy1ruCljEHbhyyVAhxse1XmvJ54WQLtZUw'
        refresh_url = 'https://www.googleapis.com/oauth2/v4/token'

        body = {
            'grant_type': 'refresh_token',
            'client_id': client_id,
            'client_secret': client_secret,
            'refresh_token': refresh_token
        }

        result = requests.post(url=refresh_url, data=body)
        
        if result.ok:
            #print('Success.')
            #print(result.text)
            return result.json()['access_token']
        else:
            #print('Fail.')
            #print(result.text)
            return None

    def upload(self, files):
        try:
            access_token = self.get_access_token()
            drive_url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }

            reqs = []
            imgs = []
            urls = []

            if access_token != None:
                for file in files:
                    image = open(file, 'rb')
                    imgs.append(image)

                    parameters = {
                        'name': 'image',
                        'parents': ['1ibXfz1zlk6V8yjjfVp6532Og1nQZ3Jx_']
                    }

                    files = {
                        'data': ('metadata', json.dumps(parameters), 'application/json; charset=UTF-8'),
                        'file': image
                    }
                    reqs.append(grequests.post(drive_url, headers=headers, files=files))

                results = grequests.map(reqs)

                for img in imgs:
                    img.close()

                for result in results:
                    if result.ok:
                        #print('Success.')
                        #print(result.text)
                        image_url = 'https://drive.google.com/uc?export=view&id=' + result.json()['id']
                        urls.append(image_url)
                    else:
                        #print('Fail.')
                        #print(result.text)
                        pass

            return urls
        except:
            pass

#if __name__ == "__main__":
    #GoogleDrive().upload(['corgi.jpg', 'office.jpg', 'moi.jpg'])