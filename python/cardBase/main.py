from urllib import response
import requests

class todoAPI():
    def postCall(n):
        api_url = "https://jsonplaceholder.typicode.com/todos"
        response = requests.post(api_url, json=n)

def main() ->None:
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    print(response.json(), response.status_code)
    
    # create dictionary
    todo = {"userId": 1, "title": "Buy milk", "completed": False}
    print(todoAPI.postCall(todo))

    

if __name__ == '__main__':
    main()