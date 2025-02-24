import os
import gdown
import zipfile
import stat

"""
Download and extract a CMU Unity Environment Model.

Author: Minho Lee
GitHub: https://github.com/iminolee/

Additional environment models are available at:
https://drive.google.com/drive/folders/1bmxdT6Oxzt0_0tohye2br7gqTnkMaq20
"""

# Configurations
env_name = "livingroom_1.zip"
ggID = '1bhyrm6MxiEUkf4XZ71veOYf0eVwU9g9C'
output_dir = "/workspace/cmu_vla_challenge_unity/src/vehicle_simulator/mesh/unity"

# Download the env file from google drive
print("Downloading livingroom_1.zip...")
gdown.download(f"https://drive.google.com/uc?export=download&id={ggID}", env_name, quiet=False)

# Unzip the file
print("Unzipping files...")
with zipfile.ZipFile(env_name, "r") as zip_ref:
    members = zip_ref.namelist()

    # Detect root folder inside the zip
    root_folder = None
    first_entry = members[0].split("/")[0]
    if all(entry.startswith(first_entry + "/") for entry in members):
        root_folder = first_entry

    # Extract files while removing the root folder
    for member in members:
        file_path = member[len(root_folder) + 1:] if root_folder else member
        target_path = os.path.join(output_dir, file_path)

        if member.endswith("/"):
            os.makedirs(target_path, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with zip_ref.open(member) as source, open(target_path, "wb") as target:
                target.write(source.read())

# Set file and folder permissions
for root, dirs, files in os.walk(output_dir):
    for d in dirs + files:
        os.chmod(os.path.join(root, d), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

os.remove(env_name)

print("Unity Simulation Environment downloaded successfully!")