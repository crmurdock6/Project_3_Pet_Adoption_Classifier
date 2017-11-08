import flask
import pickle
import numpy as np


# ---------- MODEL IN MEMORY ---------------- #

# Load pickled dataframe
path = '/Users/murdock/Documents/metis/project3/RF_current_day.pkl'
model_pkl = open(path, 'rb')
RF_model = pickle.load(model_pkl)
# Load LabelEncoder files
path2 = '/Users/murdock/Documents/metis/project3/pkl_files/'
labels = ['BREED', 'COLOR', 'INTAKE_CONDITION', 'INTAKE_TYPE',
          'SEX_ON_OUTCOME']
# Load StandardScalar files
path3 = '/Users/murdock/Documents/metis/project3/standardscalarRF.pkl'
scalar_pkl = open(path3, 'rb')
ss = pickle.load(scalar_pkl)

encoders = []
for label in labels:
    label_pkl = open(path2 + label + '.pkl', 'rb')
    encoder = pickle.load(label_pkl)
    encoders.append(encoder)

breed_encoder = encoders[0]
color_encoder = encoders[1]
int_cond_encoder = encoders[2]
int_type_encoder = encoders[3]
sex_encoder = encoders[4]

# Initialize the app
app = flask.Flask(__name__)


# Homepage
@app.route("/")
def viz_page():
    """
    Homepage: serve our visualization page
    """
    with open("dogapp.html", 'r') as viz_file:
        return viz_file.read()


@app.route("/results", methods=["POST"])
def score():
    """
    When A POST request with json data is made to this url,
    Read the example from the json, predict probability and
    send it with a response
    """
    # Get decision score for our example that came with the request
    data = flask.request.json
    print(data)
    features = data["result"]
    features_for_model = []
    features_for_model += [features[6]]
    features_for_model.append(sex_encoder.transform([features[0]])[0])
    features_for_model += [features[1]]
    features_for_model.append(breed_encoder.transform([features[2]])[0])
    features_for_model.append(color_encoder.transform([features[3]])[0])
    features_for_model.append(int_type_encoder.transform([features[4]])[0])
    features_for_model.append(int_cond_encoder.transform([features[5]])[0])
    print(features_for_model)
    scaled_features = ss.transform(np.array(features_for_model).reshape(1, -1))
    final_outcome = RF_model.predict(scaled_features)
    final_proba = RF_model.predict_proba(scaled_features)
    # Put the result in a nice dict so we can send it as json
    results = {"outcome": [np.asscalar(final_outcome[0]), final_proba[0][0]]}
    print(results)
    return flask.jsonify(results)


if __name__ == '__main__':
    app.run()
