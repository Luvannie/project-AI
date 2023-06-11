from flask import Flask, render_template, request
import googlemaps

# Khóa API Google Maps
api_key = 'AIzaSyCT7aw2miELB6v2BiKKJqM-oq6QqHdu3fM'

# Tạo đối tượng client của Google Maps
gmaps = googlemaps.Client(key=api_key)

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Route mặc định
@app.route('/')
def index():
    return render_template('index.html')

# Route xử lý form submit
@app.route('/directions', methods=['POST'])
def directions():
    origin = request.form['origin']
    destination = request.form['destination']
    
    steps = find_directions(origin, destination)
    
    if steps:
        return render_template("directions.html", steps=steps)
    else:
        return render_template("directions.html", error="Không tìm thấy đường đi.")

# Tìm đường đi giữa hai điểm
def find_directions(origin, destination):
    directions_result = gmaps.directions(origin, destination, mode="walking")
    if directions_result:
        return directions_result[0]['legs'][0]['steps']
    return None

if __name__ == '__main__':
    app.run(debug=True)
