from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/analyze', methods=['POST'])
def analyze_json():
    try:
        # Step 1: Get the JSON data from the request
        input_json = request.get_json()
        if not input_json:
            return jsonify({"error": "Invalid JSON format"}), 400

        # Step 2: Perform analysis (example: adding a key to each dictionary)
        
        #analyzed_data = []
        '''for item in input_json.get("data", []):  # Assuming input has a 'data' key
            item['analyzed'] = True  # Example modification
            analyzed_data.append(item)'''
        #print(analyzed_data)
        #print('hi')

        # Step 3: Return the modified JSON data
        return jsonify(input_json), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
