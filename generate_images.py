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
    all_prompts = [json.loads(line) for line in file]

BATCH_SIZE = 20
PENDING_PREDICTIONS = []

# Generate images in batches
for i in range(0, len(all_prompts), BATCH_SIZE):
    batch_prompts = all_prompts[i : i + BATCH_SIZE]

    # Generate images for the current batch
    for prompt in batch_prompts:
        output_dir = f"./outputs/{prompt['caption_source']}"
        output_path = f"{output_dir}/{prompt['prompt_sha']}-{prompt['seed']}.webp"

        if os.path.exists(output_path):
            logging.info(f"Image already exists: {output_path}. Skipping generation.")
            continue

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
            "disable_safety_checker": True,
        }

        prediction = replicate.predictions.create(
            prompt["model_version"], input=prediction_params
        )
        PENDING_PREDICTIONS.append(
            f"{prediction.id}::{prompt['prompt_sha']}::{prompt['caption_source']}::{prompt['seed']}"
        )

    # Process the current batch
    while PENDING_PREDICTIONS:
        logging.info("Pending predictions count: %d", len(PENDING_PREDICTIONS))
        for pending_prediction in PENDING_PREDICTIONS[
            :
        ]:  # Create a copy of the list to iterate over
            prediction_id, prompt_sha, caption_source, seed = pending_prediction.split(
                "::"
            )

            logging.info("Fetching prediction for ID: %s", prediction_id)
            prediction = replicate.predictions.get(prediction_id)

            if prediction.status == "succeeded":
                logging.info("Prediction succeeded for ID: %s", prediction_id)
                prediction_output_url = prediction.output[0]

                output_dir = f"./outputs/{caption_source}"
                os.makedirs(output_dir, exist_ok=True)

                output_path = f"{output_dir}/{prompt_sha}-{seed}.webp"
                urllib.request.urlretrieve(prediction_output_url, output_path)

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
                    "Prediction status for ID: %s is %s",
                    prediction_id,
                    prediction.status,
                )

        if PENDING_PREDICTIONS:
            time.sleep(5)  # Wait for 5 seconds before checking again

    logging.info(
        f"Completed batch {i//BATCH_SIZE + 1} of {(len(all_prompts) - 1)//BATCH_SIZE + 1}"
    )
