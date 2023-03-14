import modal

# get secret env vars
secrets = modal.Secret.from_name("demo-secrets")

# create image and install dependencies
image = modal.Image.debian_slim().pip_install_from_requirements("requirements.txt")

# by default, modal will deploy the config/ directory
# instead, mount and deploy the entire django project
# /root is the base directory modal puts in the container
mounts = [modal.Mount.from_local_dir(local_path=".", remote_path="/root")]
