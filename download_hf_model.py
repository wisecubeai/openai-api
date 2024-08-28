from huggingface_hub import snapshot_download
#model_id="lmsys/vicuna-13b-v1.5"
model_id="microsoft/Phi-3.5-mini-instruct"
snapshot_download(repo_id=model_id, local_dir="Phi-3.5-mini-instruct",
                  local_dir_use_symlinks=False, revision="main")
