you will need ollama and open-interpreter installed.
execute named_pipes.sh to create the pipes.
edit the .py files to your liking, as i use custom models you will have to edit the interpreter.llm.model to match your model.
i like to start the executioner first as that is the initial listener with the manager delivering the initial message.
open a terminal and: python3.xx Executioner.py. "or whatever version of python you use" interpreter requires 3.10-3.11.
open a second terminal and: python3.xx Manager.py.
you may want to change interpreter.auto_run = True to False.
if they jam up after a N selection you can sometimes echo anything into the pipes to break the listener lock.
the interpreter.llm.model is very finicky. took me about 9 hours to get it to work.
the model i am using is xploitr/exploitr:v2 modelfile with dolphin-mixtral:8x7b.
