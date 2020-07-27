import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
import sqlite3
import requests


from .models import Thread, ChatMessage

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        
        other_user=self.scope['url_route']['kwargs']['username']
        me = self.scope['user'].username
        #gets the earliest theard between two users
        thread_obj= await self.get_thread(me,other_user)

        #dispays the thread in the debugger window so that the front end can use
        postMan( thread_obj.id)
        self.thread_obj = thread_obj

        chat_room = f"thread_{thread_obj.id}"
        self.chat_room = chat_room
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept"
        })


    async def websocket_receive(self, event):
        print('receive', event)
        front_text = event.get('text',None)
        if front_text is not None:
            loaded_dict_data=json.loads(front_text)
            msg=loaded_dict_data.get('message')
            user = self.scope['user']
            username = user.username

            myResponse = {
                'message': msg,
                'username': username
            }
            await self.create_chat_message(user, msg)

            #broadcasts the message event to be sent
            await self.channel_layer.group_send(
                self.chat_room,
                {
                    'type': 'chat_message',
                    'text': json.dumps(myResponse)
                }
            )
        




    async def chat_message(self, event):
        #sends message
        await self.send({
            'type': 'websocket.send',
            'text': event['text']
        })


    async def websocket_disconnect(self, event):
        print('disconnected', event)

    @database_sync_to_async
    def get_thread(self,user,other_username):
        return Thread.objects.get_or_new(user,other_username)[0]

    @database_sync_to_async
    def create_chat_message(self, me, msg):
        thread_obj  = self.thread_obj
        return ChatMessage.objects.create(thread=thread_obj, user=me, message = msg)


# Returns a list of threads between two users in acs order
def findRightThread(userID, secondUserID):
    conn = sqlite3.connect('../Fur-Finder-Backend/db.sqlite3')
    c = conn.cursor()
    chat_threads= c.execute("SELECT * FROM chat_thread WHERE first_id=="+str(userID)+" and second_id=="+str(secondUserID)+" or first_id=="+str(secondUserID)+" and second_id="+str(userID) +" ORDER by timestamp ASC").fetchall()
    conn.close()
    return chat_threads


# Finds the chat messages using the threadID
def getChatMessages(lowest_thread):
    conn = sqlite3.connect('../Fur-Finder-Backend/db.sqlite3')
    c = conn.cursor()
    messages = c.execute("SELECT * FROM chat_chatmessage WHERE thread_id =='" + str(lowest_thread) + "';").fetchall()
    for index in range(0,len(messages)):
        print ("From: "+ getUsername(messages[index][4])+"\nMessage: "+messages[index][1]+" @"+str(messages[index][2]),"\n")

    conn.close()
    return messages


# Finds the username based on the ID
def getUsername(ID):
    conn = sqlite3.connect('../Fur-Finder-Backend/db.sqlite3')
    c = conn.cursor()
    username = c.execute("SELECT username FROM FurFinderAPI_account WHERE id =='" + str(ID) + "';").fetchall()
    conn.close()

    return username[0][0]


def postMan(threadID):
    messages = getChatMessages(threadID)
    messages = str(messages).strip('[]')
    print(messages)
    # requests.post('http://192.168.0.145:8000/api/UserMessages//', {'user1': getUsername(userID), 'user2': getUsername(secondUserID), 'threadID': threadID, 'message': messages})


