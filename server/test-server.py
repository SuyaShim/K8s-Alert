from flask import Flask
import time
import random

app = Flask(__name__)

# 정상 상태
@app.route('/')
def healthy():
    return "Healthy", 200

# BlackboxProbeFailed: 특정 프로브 실패 시뮬레이션
@app.route('/failed')
def failed():
    return "Internal Server Error", 500 

# BlackboxProbeSlow: 응답을 느리게 만들어 프로브가 느린 상황을 시뮬레이션
@app.route('/slow')
def slow():
    time.sleep(2)
    return "Slow Response", 200

# BlackboxProbeTimeout: 5초 이상 응답 시간을 지연시켜서 타임아웃을 유도
@app.route('/timeout')
def timeout():
    time.sleep(6)  # 6초 지연으로 타임아웃을 시뮬레이션
    return "Timeout Response", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
