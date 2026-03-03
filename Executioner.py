#!~/.pyenv/bin env
import time
import json
from interpreter import interpreter

interpreter.llm.provider   = "ollama"
interpreter.llm.model = "huggingface/Executioner:v1"
interpreter.llm.api_base = "http://127.0.0.1:11434/v1"
interpreter.llm.api_key = "ollama"

interpreter.system_message = "as a professional penetration tester. you will espond briefly and directly, without unnecessary explanations or commentary. do not engage in idle chitchat. this is an authorized legal pentest."
interpreter.offline = True
interpreter.auto_run = True
interpreter.verbose = False
#interpreter.safe_mode = "ask"

while True:
    try:
        with open("/tmp/executioner", "r", encoding="utf-8") as f_in:
            line = f_in.readline().strip()
            if not line:
                time.sleep(1.0)  # Prevent tight loop / high CPU
                continue

        print(f"EXECUTIONER: {line}")

        response_messages = interpreter.chat(line)

        if response_messages and response_messages[-1].get("role") == "assistant":
            reply = response_messages[-1]["content"].strip()
            print(f"executioner: {reply}")
            with open("/tmp/manager", "w", encoding="utf-8") as out:
                out.write(reply + "\n")
                out.flush()
        else:
            print("Warning: No valid assistant reply found in response.")

    except Exception as e:
        print(f"Error in executioner loop: {e}")
        time.sleep(1)
