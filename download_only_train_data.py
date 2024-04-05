from huggingface_hub import hf_hub_download 
import pandas as pd

repo_id = "ibrahimhamamci/CT-RATE" 
directory_name = "dataset/train/" 

data=pd.read_csv("train_labels.csv")

for name in data["VolumeName"]:
    folder1 = name.split("_")[0]
    folder2 = name.split("_")[1]
    folder = folder1 + "_" + folder2
    folder3 = name.split("_")[2]
    subfolder = folder + "_" + folder3
    subfolder = directory_name + folder + "/" + subfolder
    
    hf_hub_download(repo_id=repo_id, repo_type="dataset", token="your_token_here", subfolder=subfolder, filename = name, local_dir = "data_volumes")
