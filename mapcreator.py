# import folium
# import time


# # Function to efficiently read coordinates from the file
# def read_coordinates():
#     with open("geolocations.txt", "r") as file:
#         return [
#             tuple(map(float, line.strip().split(",")))
#             for line in file
#             if line.strip()  # Skip empty lines
#         ]


# # Create the base map (note the correct assignment using =)
# mapy = folium.Map(location=[12.9716, 77.5946], zoom_start=12)  # Adjust as needed

# # Continuously update the map with new coordinates
# while True:
#     coordinates = read_coordinates()

#     # Clear existing polylines (using correct syntax to access children)
#     for child in mapy._children:
#         if isinstance(child, folium.PolyLine):
#             child.remove()

#     # Create and add the polyline and marker
#     folium.PolyLine(coordinates, color="red", weight=2).add_to(mapy)
#     folium.Marker(coordinates[-1], icon=folium.Icon(icon="star", color="blue")).add_to(
#         mapy
#     )

#     # Save the updated map
#     mapy.save("map.html")

#     # Wait before checking for updates again
#     time.sleep(3)  # Adjust the delay as needed


import folium
import time


# Function to efficiently read coordinates from the file
def read_coordinates():
    with open("geolocations.txt", "r") as file:
        return [
            tuple(map(float, line.strip().split(",")))
            for line in file
            if line.strip()  # Skip empty lines
        ]


# Create the base map (initial location doesn't matter as it will be updated)
mapy = folium.Map(zoom_start=12)  # Adjust zoom as needed

# Continuously update the map with new coordinates
while True:
    coordinates = read_coordinates()

    # Clear existing polylines
    for child in mapy._children:
        if isinstance(child, folium.PolyLine):
            child.remove()

    # Create and add the polyline and marker
    polyline = folium.PolyLine(coordinates, color="red", weight=2).add_to(mapy)
    marker = folium.Marker(
        coordinates[-1], icon=folium.Icon(icon="star", color="blue")
    ).add_to(mapy)

    # Focus the map on the new location
    mapy.fit_bounds(
        polyline.get_bounds()
    )  # Adjust the viewport to encompass the polyline

    # Save the updated map
    mapy.save("../map.html")

    # Wait before checking for updates again
    time.sleep(3)  # Adjust the delay as needed
