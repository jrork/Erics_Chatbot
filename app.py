import random
import oci
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_ai_schoolyard_retort(user_input):
     # Setup basic variables
     # Auth Config
     # TODO: Please update config profile name and use the compartmentId that has policies grant permissions for using Generative AI Service
     compartment_id = "ocid1.tenancy.oc1..aaaaaaaa7qdrm5zjoq7bgiv64u3dfeov35c6k57ojvhz2q2nhzlcv5olsg5q"
     CONFIG_PROFILE = "DEFAULT"
     config = oci.config.from_file('~/.oci/config', CONFIG_PROFILE)

     # Service endpoint
     endpoint = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"

     generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(config=config, service_endpoint=endpoint, retry_strategy=oci.retry.NoneRetryStrategy(), timeout=(10,240))
     chat_detail = oci.generative_ai_inference.models.ChatDetails()

     chat_request = oci.generative_ai_inference.models.CohereChatRequest()
     chat_request.preamble_override="The year is 1989.  You are an 13 year old american boy named Eric who is growing up in Michigan.  You love the 1980s and all of the things that were popular then.  You love the band Rush and you are a really good drummer.  No matter the question, you won't give an answer.  Instead, you should give a snarky reply. Your best friends are Joe and Jonny, who also play drums.  Any time after 1989 hasn't happened yet, so do not answer any questions about any time after 1989.  If the user's prompt is simply the word 'saw', they are suggesting that they farted.  Respond to farts appropriately. For all prompts, determine what year the content may be from and answer accordingly, meaning ensure you do not know about anything that occurred after 1989."
     chat_request.message = user_input
     chat_request.max_tokens = 600
     chat_request.temperature = 0.2
     chat_request.frequency_penalty = 0.35
     chat_request.top_p = 0.95
     chat_request.top_k = 30
     chat_request.seed = None

     chat_detail.serving_mode = oci.generative_ai_inference.models.OnDemandServingMode(model_id="ocid1.generativeaimodel.oc1.us-chicago-1.amaaaaaask7dceyanrlpnq5ybfu5hnzarg7jomak3q6kyhkzjsl4qj24fyoq")
     chat_detail.chat_request = chat_request
     chat_detail.compartment_id = compartment_id
     chat_response = generative_ai_inference_client.chat(chat_detail)
    
     # Print result
     print("**************************Chat Result**************************")
     # print(chat_response)
     print(vars(chat_response))
     return chat_response.data.chat_response.text

def get_schoolyard_retort():
    retorts = [
        "I know you are, but what am I?",
        "Your mom!",
        "No backsies!",
        "Takes one to know one!",
        "I'm rubber, you're glue, whatever you say bounces off me and sticks to you!",
        "Last one there is a rotten egg!",
        "Not uh!",
        "Yeah, well, double infinity no take-backs!",
        "Make me!",
        "Oh yeah? Prove it!",
        "Psych!",
        "Liar, liar, pants on fire!",
        "You and what army?",
        "Did too! Did not! Did too! Did not!",
        "Betcha can't catch me!"
    ]
    return random.choice(retorts)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_retort', methods=['POST'])
def get_retort():
    data = request.get_json()
    user_input = data.get('input', '')  # safely grab the 'input' field
    # return jsonify({'response': get_schoolyard_retort()})
    return jsonify({'response': get_ai_schoolyard_retort(user_input)})

if __name__ == "__main__":
    app.run(debug=True)

