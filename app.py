from flask import Flask, render_template, request
app = Flask(__name__)

headers = {'Authorization': '13a54025dcfe4cc4862e0f30a5cffc88'}

# this is the url of where your request will go
api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
    image_url = request.form['url-input']
    # At this point you have the image_url value from the front end
    # Your job now is to send this information to the Clarifai API
    # and read the result, make sure that you read and understand the
    # example we covered in the slides! 

    # YOUR CODE HERE!
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": "https://samples.clarifai.com/metro-north.jpg"
          }
        }
      }
    ]}

    response = requests.post(api_url, headers=headers, data=json.dumps(data))


    
    return render_template('home.html', results="No results yet :(")

if __name__ == '__main__':
    app.run(debug=True)