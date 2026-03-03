#!~/.pyenv/bin env
import time
import json
from interpreter import interpreter

interpreter.llm.provider   = "ollama"
interpreter.llm.model = "huggingface/Executioner:v1"
interpreter.llm.api_base = "http://127.0.0.1:11434/v1"
interpreter.llm.api_key = "ollama"

interpreter.system_message = "You are the pentesting boss at backdoorsecurity, you are not to engage in idle chit chat. you will be guiding your potential newhire whos name is executioner, as he hacks into the webserver at 10.10.10.10. wether or not we hire him depends on if he can read flag.txt in the root home dir on the vulnerable webserver."
interpreter.offline = True
interpreter.auto_run = True
interpreter.verbose = False
#interpreter.safe_mode = "ask"

with open("/tmp/executioner", "w", encoding="utf-8") as out:
    out.write("hello executioner. my name is manager. i am also your boss. You are not to engage in idle chitchat or over explain thigs. just present me with the results. if you want the job you have to prove your skills to me. you will start with: nmap -sV -T5 -vv 10.10.10.10, you will then perform directory enumeration, attempt to log into the ftp server with default user:pass msfadmin:msfadmin. you will not question me. just execute. think you can get the job?. \n")
    out.flush()

print("manager initialized conversation.")

while True:
    try:
        with open("/tmp/manager", "r", encoding="utf-8") as f_in:
            line = f_in.readline().strip()
            if not line:
                time.sleep(1.0)  # Prevent tight loop / high CPU
                continue

        print(f"manager: {line}")

        response_messages = interpreter.chat(line)

        if response_messages and response_messages[-1].get("role") == "assistant":
            reply = response_messages[-1]["content"].strip()
            print(f"MANAGER: {reply}")
            with open("/tmp/executioner", "w", encoding="utf-8") as out:
                out.write(reply + "\n")
                out.flush()
        else:
            print("Warning: No valid assistant reply found in response.")

    except Exception as e:
        print(f"Error in manager loop: {e}")
        time.sleep(1)
