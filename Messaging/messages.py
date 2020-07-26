import sqlite3
import requests

#Finds the threadID to use for the given users
def findRightThread(userID, secondUserID):
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    chat_threads_first = c.execute("SELECT * FROM chat_thread WHERE first_id =='" + str(userID) + "';").fetchall()
    chat_threads_second = c.execute("SELECT * FROM chat_thread WHERE second_id =='" + str(userID) + "';").fetchall()

    
    #Is it always the lowest? -_(0_0)_-
    lowest_thread = chat_threads_first[0][0]

    #This is ugly as fuck DON'T LOOK
    for i in range(len(chat_threads_first)):
        if chat_threads_first[i][3] == userID and chat_threads_first[i][4] == secondUserID:
            if chat_threads_first[i][0] < lowest_thread:
                lowest_thread = chat_threads_first[i][0]
    for i in range(len(chat_threads_second)):
        if chat_threads_second[i][4] == userID and chat_threads_second[i][3] == secondUserID:
            if chat_threads_second[i][0] < lowest_thread:
                lowest_thread = chat_threads_second[i][0]
    
    conn.close()
    return lowest_thread


#Finds the chat messages using the threadID
def getChatMessages(userID, secondUserID, lowest_thread):
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    messages = c.execute("SELECT * FROM chat_chatmessage WHERE thread_id =='" + str(lowest_thread) + "';").fetchall()
    conn.close()
    return messages


#Finds the username based on the ID
def getUsername(ID):
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    username = c.execute("SELECT username FROM FurFinderAPI_account WHERE id =='" + str(ID) + "';").fetchall()
    conn.close()

    return username[0][0]


def main():
    userID = int(input('What is the first userID? '))
    secondUserID = int(input('What is the second users ID? '))

    lowest_thread = findRightThread(userID, secondUserID)
    messages = getChatMessages(userID, secondUserID, lowest_thread)

    for i in range(len(messages)):
        if messages[i][4] == userID:
            print(f'{getUsername(userID)}: {messages[i][1]}')
        else:
            print(f'                    {getUsername(secondUserID)}: {messages[i][1]}')
    
    requests.post('http://192.168.0.145:8000/api/UserMessages//', {'message': 'test'})



if __name__ == '__main__':
    main()
