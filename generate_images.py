import os
import json
import logging
import urllib.request
import time
import replicate

# Setup basic configuration for logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load prompts from prompts.jsonl
with open("prompts.jsonl", "r") as file:
    prompts = [json.loads(line) for line in file]

PENDING_PREDICTIONS = []
PREDICTIONS = {}

# Generate images
for prompt in prompts:
    logging.info("Generating image for prompt: %s", prompt["prompt"])

    prediction_params = {
        "model": "schnell",
        "prompt": prompt["prompt"],
        "seed": prompt["seed"],
        "width": 1024,
        "height": 1024,
        "lora_scale": 1,
        "num_inference_steps": 4,
        "output_format": "webp",
        "output_quality": 80,
    }

    prediction = replicate.predictions.create(
        prompt["model_version"], input=prediction_params
    )
    PENDING_PREDICTIONS.append(
        f"{prediction.id}::{prompt['prompt_sha']}::{prompt['seed']}"
    )

while len(PENDING_PREDICTIONS) > 0:
    logging.info("Pending predictions count: %d", len(PENDING_PREDICTIONS))
    for pending_prediction in PENDING_PREDICTIONS[
        :
    ]:  # Create a copy of the list to iterate over
        prediction_id, prompt_sha, seed = pending_prediction.split("::")

        logging.info("Fetching prediction for ID: %s", prediction_id)
        # fetch prediction
        prediction = replicate.predictions.get(prediction_id)

        # if prediction is successful, fetch the output image
        if prediction.status == "succeeded":
            logging.info("Prediction succeeded for ID: %s", prediction_id)
            prediction_output_url = prediction.output[0]

            # Create output directory if it doesn't exist
            output_dir = f"./outputs/{prompt['caption_source']}"
            os.makedirs(output_dir, exist_ok=True)

            # Save the output image directly to disk without buffering in memory
            output_path = f"{output_dir}/{prompt_sha}-{seed}.webp"
            urllib.request.urlretrieve(prediction_output_url, output_path)

            # remove prediction from the download queue
            PENDING_PREDICTIONS.remove(pending_prediction)

            logging.info("Image saved to %s", output_path)

        elif prediction.status == "failed":
            logging.error(
                "Prediction failed for ID: %s, Error: %s",
                prediction_id,
                prediction.error,
            )
            PENDING_PREDICTIONS.remove(pending_prediction)
        else:
            logging.info(
                "Prediction status for ID: %s is %s", prediction_id, prediction.status
            )

    time.sleep(5)  # Wait for 5 seconds before checking again
