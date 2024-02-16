from flask import Flask, request

app = Flask(__name__)

@app.route("/factorial/<int:n>", methods=["GET"])
def factorial(n):
	r = calculate(n)
	return {"result":r},200 # OK

def calculate(n):
	result = 1
	if n <= 0:
		return 1
	else:
		for i in range(1,n+1):
			result = result * i
		return result


if __name__ == "__main__":
	app.run(host="localhost", port=5000)
