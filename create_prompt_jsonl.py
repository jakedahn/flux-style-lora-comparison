import json

SEED = 1337

MODELS = {
    "gpt-4o-mini": {
        "model": "jakedahn/flux-latentpop:bdea1b73bce4e772be82b3d0a6c38fd4343f7a9697e219574907953cd60065aa",
        "trigger_word": "latentpop style",
    },
    "claude-3.5-sonnet": {
        "model": "jakedahn/flux-latentpop:64a823e2efc2df0758e33fae03a6fad2fc75f04d25941153faab73f87ba87a08",
        "trigger_word": "latentpop style",
    },
    "llava-13b-new": {
        "model": "jakedahn/flux-latentpop:22490caf5ecd083c3fa45c0f2490386f091c669d8684e152735564378818e685",
        "trigger_word": "latentpop style",
    },
    "llava-13b-old": {
        "model": "jakedahn/flux-latentpop:39d059823aa57634b56ed8a11ae51fe59af9857f1aea7653e2c2c31c12672a92",
        "trigger_word": "LNTP style",
    },
}

PROMPTS = [
    {
        "prompt": "A tornado made of sharks crashing into a skyscraper. painting in the",
        "sha2": "bd30f5d7e63e8e1421a77a210de3044d3430c800caee9b7d4a0ab359c68841c1",
    },
    {
        "prompt": "A shiny robot wearing a race car suit and black visor stands proudly in front of an F1 race car. The sun is setting on a cityscape in the background.",
        "sha2": "25b41035377cd39df561289bae89c2d332e32a4e7123b7e3745d1b55e8d24749",
    },
    {
        "prompt": "A photo of a light bulb in outer space traveling the galaxy with a sailing boat inside the light bulb.",
        "sha2": "6b4966cd60c141df4ff3ac7c95f6e3e554edf8577299706844bad82f0c2b6d69",
    },
    {
        "prompt": "Dogs sitting around a poker table with beer bottles and chips. Their hands are holding cards.",
        "sha2": "a1a1e34b474e639263589738de964fd24cd84a0cac22a3351fbf22ef8e2b89b3",
    },
    {
        "prompt": "A castle made of tortilla chips, in a river made of salsa. There are tiny burritos walking around the castle.",
        "sha2": "32b35b415c4622f5938c849e6a484ef34525e9ffd12d53899d615651c31afc63",
    },
    {
        "prompt": "An oil painting of a two-story house lifting off the ground like a rocket.",
        "sha2": "ba70e166e641a274da7734c7ba2b598043b3de5208ca95abe34372c9bce69c50",
    },
    {
        "prompt": "A stained glass window depicting a calm tyrannosaurus rex.",
        "sha2": "c8331c01377e36d9eda39f2d04e18982a7665f7faee91ae4693182c797c29d77",
    },
    {
        "prompt": "A photo of an Athenian vase with a painting of pandas playing basketball",
        "sha2": "cb0cca3a396b75380498cc36c0e4d903c310ca08973a55a3b47f7f6288017d14",
    },
    {
        "prompt": "A raccoon detective using a microscope while riding in a train.",
        "sha2": "58476efb0e47038f88f81aaa93abc050a60e2425b2afe98d149b214702c3af27",
    },
    {
        "prompt": "A close-up of two chameleons wearing karate uniforms and fighting, jumping over a waterfall.",
        "sha2": "5a1bf109aa73f7440ad27993259682bf9847126072d8be1a2e0ad19d0386d6f7",
    },
    {
        "prompt": "Portrait of a gecko wearing a train conductor's hat and holding a flag that has a yin-yang symbol on it. Marble statue.",
        "sha2": "22dffa495f3759b0f9a517894c1d3a54c804e6dd740d18f2f4098e6975b69f62",
    },
    {
        "prompt": "A rusty spaceship blasts off in the foreground. A city with tall skyscrapers is in the distance, with a mountain and ocean in the background. A dark moon is in the sky.",
        "sha2": "5ae2890b49a15cff64c5d19c7580932b2d61765e67fd0b7173c532ca0ae57399",
    },
    {
        "prompt": "A group of farm animals (cows, sheep, and pigs) made out of cheese and ham, on a wooden board. There is a dog in the background eyeing the board hungrily.",
        "sha2": "b66351a13422a3278b0cde1db490fedeba3af62732e83bd972d103f02907e5b4",
    },
    {
        "prompt": "An alien octopus floats through a portal reading a newspaper. DSLR photo.",
        "sha2": "5c87c863ba21d494a8df54a54b215e9bb679a9c6b013f8240adf4d21d67bd70d",
    },
    {
        "prompt": "A photo of an astronaut riding a horse in the forest. There is a river in front of them with water lilies.",
        "sha2": "96c75a7c643f028ad1e378d3f12972b523be18f9fc7d0ab7b54a1a0594e6c30b",
    },
    {
        "prompt": "The buildings of downtown Manhattan situated at below Mount Everest. The Great Pyramid is in the foreground.",
        "sha2": "293bbdc5d60bd41ec384ca961088044a6eb74dcf5663c00321b4758531d5972c",
    },
    {
        "prompt": "A photograph of a bird made of wheat bread and an egg.",
        "sha2": "5996c3bd0648a7d8c7daed8e38bd486f31c9644af39ff37525ea8dbcb7d68670",
    },
    {
        "prompt": "A gundam stands tall with its sword raised. A city with tall skyscrapers is in the distance, with a mountain and ocean in the background. A dark moon is in the sky.",
        "sha2": "d4e654c2376f9091c4a1840a90c077216d89d0f764df3312ab8d685e50f548ce",
    },
    {
        "prompt": "A high resolution photo of a rat working out in a gym.",
        "sha2": "4582577d0d08738a2fc6bb49930ed3a968c2eebecedbe0e7ba72bd529b807d3b",
    },
    {
        "prompt": "A dump truck filled with soccer balls scuba diving in a coral reef.",
        "sha2": "40952081965f22cb84d6aa62918c15d52a68bb43097603c831edd38494f4111c",
    },
    {
        "prompt": "A soft beam of light shines down on an armored granite wombat warrior statue holding a broad sword. The statue stands an ornate pedestal in the cella of a temple. wide-angle lens.",
        "sha2": "22dedd0189ef7f2bf9f80861e3d39b971cb4f944d666ce9feca8602edf982a60",
    },
    {
        "prompt": "A portrait of a metal statue of a pharaoh wearing steampunk glasses and a leather jacket over a white t-shirt that has a drawing of a space shuttle on it.",
        "sha2": "21f2e1d0f7d58f979da2ee086036e38573756d0ffee3323b02575eef59b58942",
    },
    {
        "prompt": "A photograph of the inside of a subway train. There are frogs sitting on the seats. One of them is reading a newspaper. The window shows the river in the background.",
        "sha2": "04d4d88f1b9aec98389721815204bc3985715a235bbf94b3e1ad8cdbb92253c1",
    },
    {
        "prompt": "A smiling sloth wearing a leather jacket, a cowboy hat, a kilt and a bowtie. The sloth is holding a quarterstaff and a big book. A shiny VW van with a cityscape painted on it and parked on grass.",
        "sha2": "b9381003217583245fd2303efaf114c5d81daddb69ab40241cc85b2387f263d6",
    },
    {
        "prompt": "Greek statue of a man comforting a cat. The cat has a big head. The man looks angry.",
        "sha2": "d01f7546a279afa4b68700340c9356c32920ff25c10eef627396be08e7bd25ba",
    },
    {
        "prompt": "A photo of a frog reading the newspaper named 'Today' written on it. There is a frog printed on the newspaper too.",
        "sha2": "8b5292a5b65a004ea70228a7ca2850b1f7178ae4aa8d22738127acf3d996c243",
    },
    {
        "prompt": "A cat dreaming about becoming a tiger.",
        "sha2": "2a24c716961062ea8fecc1259e1956688c562803c4d738ffe57581d4e8f1add1",
    },
    {
        "prompt": "A paranoid android freaking out and jumping into the air because it is surrounded by colorful Easter eggs.",
        "sha2": "55fd165aac2c0fa4b73ccfa5298012449ef1f2d0daaff9dcd9400266507f797a",
    },
    {
        "prompt": "A burger patty, with the bottom bun and lettuce and tomatoes. 'COFFEE' written on it in mustard.",
        "sha2": "4310f8ad3437490b0afdc348bae32d169319aae11ac8038f69bbcc4ba29dbfbe",
    },
    {
        "prompt": "The saying 'BE EXCELLENT TO EACH OTHER' on a rough wall with a graffiti image of a green alien wearing a tuxedo.",
        "sha2": "bb519bf1af2bfa878e9ea1f67bbe02e35ca3b639ac44e48033b02b9528a18324",
    },
]


# Create the JSONL file
with open("prompts.jsonl", "w") as jsonl_file:
    for caption_source, model_info in MODELS.items():
        for prompt_data in PROMPTS:
            json_object = {
                "caption_source": caption_source,
                "model": model_info["model"],
                "model_version": model_info["model"].split(":")[-1],
                "prompt": f"{prompt_data['prompt']} {model_info['trigger_word']}",
                "prompt_sha": prompt_data["sha2"],
                "trigger_word": model_info["trigger_word"],
                "seed": SEED,
            }
            jsonl_file.write(json.dumps(json_object) + "\n")

print("prompts.jsonl file has been created successfully.")
