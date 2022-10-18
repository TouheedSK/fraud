from flask import Flask
from flask_restful import Api, Resource, reqparse
from fraud import CalFraud

app = Flask(__name__)
api = Api(app)

args = ["name", "amount", "location", "time", "category", "merchant", "product"]
arg_type = {"name" : str, "amount": int, "location": str, "time": str, "category": str, "merchant": str, "product": str}

demo_args = reqparse.RequestParser()
for arg in args:
	demo_args.add_argument(arg, type = arg_type[arg], help = arg + " is required", required=True)

class demo(Resource) :
	def get(self):
		try:
			data = demo_args.parse_args()
			response = {}
			for arg in args:
				response[arg] = data[arg]
			response = CalFraud(response) 
			response = {"status": 101 , "data" : response}
		except:
			response = {"status": 404}
		# print( response )
		return response

api.add_resource (demo, "/demo")

if __name__ == "__main__":
	app.run(debug=True)
