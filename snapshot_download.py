from huggingface_hub import snapshot_download

snapshot_download(repo_id="ibrahimhamamci/CT-RATE", repo_type="dataset", token="your_token_here", local_dir = "./dataset")