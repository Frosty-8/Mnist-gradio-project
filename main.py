import gradio as gr
from tensorflow.keras.models import load_model #type:ignore
import os

model = load_model("models/mnist_trained_model.h5")

def predict_digit(image):
    import numpy as np
    from PIL import Image, ImageOps

    # Handle dict input (some Gradio versions)
    if isinstance(image, dict):
        if "composite" in image:
            image = image["composite"]
        elif "layers" in image and image["layers"]:
            image = image["layers"][-1]["image"]
        else:
            return {"No input": 1.0}
    # Now image should be a NumPy array
    img = Image.fromarray(np.uint8(image)).convert("L").resize((28, 28))
    img = ImageOps.invert(img)
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)
    prediction = model.predict(img_array)[0]
    return {str(i): float(prediction[i]) for i in range(10)}

gr.Interface(
    fn=predict_digit,
    inputs=gr.Sketchpad(),
    outputs=gr.Label(num_top_classes=3),
    title="Handwritten Digit Recognition",
    description="Draw a digit (0-9) and get a prediction."
).launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 8080)))