# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)


# @app.route('/')
# def home():
#    return "hello word11!"

# # if __name__ == "__main__":
# #     #app.run(debug=True)
# #     #app.run(host='0.0.0.0', port=6000)
# #     app.run(debug=True)
# #     app.run(use_reloader=False)


# @app.route('/t')
# def display():
#    return "hello word11!"

# @app.route('/person/')
# def hello():
#     return jsonify({'name':'Jimit',
#                     'address':'India'})

# @app.route('/api/recommend', methods=['GET', 'POST'])
# def recommend():
#     content_base = ContentBase("./dataset/movies.csv")

#     return "It works!"
