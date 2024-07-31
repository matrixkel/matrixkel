# # # using flask_restful
# # from flask import Flask, jsonify, request, make_response
# # from flask_restful import Resource, Api
# # from flask_cors import CORS


# # # creating the flask app
# # app = Flask(__name__)
# # # creating an API object
# # api = Api(app)

# # CORS(app)


# # # making a class for a particular resource
# # # the get, post methods correspond to get and post requests
# # # they are automatically mapped by flask_restful.
# # # other methods include put, delete, etc.
# # class Hello(Resource):
# #     # corresponds to the GET request.
# #     # this function is called whenever there
# #     # is a GET request for this resource
# #     def get(self):
# #         return jsonify({"message": "hello world"})

# #     # Corresponds to POST request
# #     def post(self):
# #         data = request.get_json()  # status code
# #         print(data)
# #         return make_response(jsonify(data), 200)


# # # another resource to calculate the square of a number
# # class Square(Resource):
# #     def get(self, num):
# #         return jsonify({"square": num**2})


# # # adding the defined resources along with their corresponding urls
# # api.add_resource(Hello, "/")
# # api.add_resource(Square, "/square/<int:num>")


# # # driver function
# # if __name__ == "__main__":
# #     app.run(debug=True)


# import folium
# from flask import Flask, jsonify, request, make_response
# from flask_restful import Resource, Api
# from flask_cors import CORS

# app = Flask(__name__)
# api = Api(app)

# # Enable CORS for all origins (adjust as needed)
# CORS(app)

# map = folium.Map(
#     location=[12.9716, 77.5946], zoom_start=12
# )  # Initial map centered in Bangalore


# class Location(Resource):
#     def get(self):
#         return jsonify({"message": "hello world"})

#     def post(self):
#         data = request.get_json()
#         latitude = data["latitude"]
#         longitude = data["longitude"]

#         # Update the marker on the existing map
#         print(data)
#         folium.Marker([latitude, longitude]).add_to(map)

#         # Save the updated map to an HTML file
#         map.save("map.html")

#         return make_response(jsonify({"message": "Location updated"}), 200)


# api.add_resource(Location, "/")

# if __name__ == "__main__":
#     app.run(debug=True)


import folium
from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Enable CORS for all origins (adjust as needed)
CORS(app)

map = folium.Map(
    location=[12.9716, 77.5946], zoom_start=12
)  # Initial map centered in Bangalore


class Location(Resource):
    def __init__(self):
        self.file = open("geolocations.txt", "a")  # Open file in append mode

    def get(self):
        return jsonify({"message": "hello world"})

    def post(self):
        data = request.get_json()
        latitude = data["latitude"]
        longitude = data["longitude"]

        # Update the marker on the map
        print(data)
        folium.Marker([latitude, longitude]).add_to(map)

        # Save the updated map to an HTML file
        map.save("map.html")

        # Append location data to the file with a timestamp
        self.file.write(f"{latitude}, {longitude}\n")
        self.file.flush()  # Ensure data is written immediately

        return make_response(jsonify({"message": "Location updated"}), 200)


api.add_resource(Location, "/")

if __name__ == "__main__":
    app.run(debug=True)

    # Close the file when the application stops
    location_resource = Location()  # Create an instance of Location
    location_resource.file.close()
