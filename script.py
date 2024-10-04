# from flask import Flask, request, send_from_directory
# import os

# app = Flask(__name__)

# # Directory where images will be stored
# UPLOAD_FOLDER = "uploaded_images"
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# # Ensure the folder exists
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)


# # Serve the uploaded image
# @app.route("/images/<filename>")
# def uploaded_file(filename):
#     return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# # Endpoint to upload image
# @app.route("/upload", methods=["POST"])
# def upload_file():
#     if "file" not in request.files:
#         return "No file part"
#     file = request.files["file"]
#     if file.filename == "":
#         return "No selected file"

#     if file:
#         file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
#         file.save(file_path)
#         return f"File uploaded successfully: {file.filename}"


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)


from flask import Flask, request
import os

app = Flask(__name__)

# Directory where uploaded images are saved
UPLOAD_FOLDER = "uploaded_images"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# Function to get the next image name
def get_next_image_name():
    files = os.listdir(UPLOAD_FOLDER)
    img_count = len([f for f in files if f.startswith("new-img-")])
    return f"new-img-{img_count + 1}.jpg"


@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    # Get the next image name
    new_filename = get_next_image_name()

    # Save the file with the new name
    file.save(os.path.join(UPLOAD_FOLDER, new_filename))
    return f"File uploaded and saved as {new_filename}", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
