# from flask import Flask, __main__, jsonify, request

# app = Flask(__name__)

# # decorator get
# @app.route("/greet", methods = ["GET"]) 
# def greet( ):
#     name = request.args.get('name', 'User')
#     return jsonify({'message': f"Hello, {name}!"})

# if __name__ == __main__:
#     app.run(debug=True)
    
    
    
    
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/api/greet")
# async def greet(name: str = "world"):
#     return ({"message": f"hello, {name}!"})







###################################################### Threading and Multiprocessing ##################################################



from multiprocessing import Process
import time

def compute_square(n):
    print(f"Computing square of {n}")
    time.sleep(2)  # Simulates heavy computation
    print(f"Square of {n} is {n * n}")

if __name__ == '__main__':
    # Running two processes in parallel
    process_1 = Process(target=compute_square, args=(5,))
    process_2 = Process(target=compute_square, args=(10,))

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

    print("Both computations completed!")




import threading

shared = []
def count_num(thread_id, num):
    for i in range(num):
        shared.append((thread_id, i))


threads = []

for i in range(3):
    thread = threading.Thread(target= count_num, args=(i, 5))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print(shared)








def pattern(n):
    matrix = [[0]*n for i in range(n)]
    num = 1
    for i in range(2*n - 1):
        if i < n:
            row, col = 0, i
        else:
            row, col = i - n + 1, n - 1
        while True:
            if not(0 <= row <= n-1 and  0 <= col <= n-1):
                break

            matrix[row][col] = num
            row += 1
            col -= 1
            num += 1
            
    return matrix
    
    
pat = pattern(4)
for i in pat:
    print(i)







