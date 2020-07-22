import asyncio
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

    async def upload(self, files):
        try:
            access_token = self.get_access_token()
            drive_url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            urls = []

            if access_token != None:
                images = []
                responses = []

                for file in files:
                    parameters = {
                        'name': 'image',
                        'parents': ['1ibXfz1zlk6V8yjjfVp6532Og1nQZ3Jx_']
                    }

                    files = {
                        'data': ('metadata', json.dumps(parameters), 'application/json; charset=UTF-8'),
                        'file': file
                    }

                    images.append(dict(url=drive_url, headers=headers, files=files))
                
                loop = asyncio.get_event_loop()
                responses = [loop.run_in_executor(None, lambda: requests.post(**image)) for image in images]
                results = await asyncio.gather(*responses)

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

                #print(urls)

            return urls
        except:
            pass

    def run(self, data):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(self.upload(data))

#if __name__ == "__main__":
    #images = ['corgi.jpg', 'office.jpg', 'moi.jpg']
    #data = []

    #for image in images:
        #with open(image, 'rb') as img:
            #data.append(img.read())

    #google_drive = GoogleDrive()

    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(google_drive.upload(data))