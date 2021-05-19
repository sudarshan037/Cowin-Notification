from flask import Flask, request
import traceback
#from booking import generateOTP, confirmOTP

app = Flask(__name__)

@app.route("/", methods=['POST'])
def get_pin():
    print("received data")
    try:
        OTP = request.json['OTP']
        #confirmOTP(txnId, OTP)
        print("OTP:", OTP)
        return {
                "result": "Success"
                }
    except:
        traceback.print_exc()
        return {
                "result": "Error Encountered"
                }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
