import tarfile
import os

build_folder_path = "code/docs/_build"
icmp_sender_path = "code/sender/icmp_sender.py"
icmp_receiver_path = "code/receiver/icmp_receiver.py"
readme_path = "code/README.md"

def pack_for_submission():
    with tarfile.open("78.tar.gz", "w:gz") as tar:
        add_files_to_tar(tar, [
            (build_folder_path, "_build"),
            (icmp_sender_path, "icmp_sender.py"),
            (icmp_receiver_path, "icmp_receiver.py"),
            (readme_path, "README.md")
        ])

def add_files_to_tar(tar, files):
    for original_path, arcname in files:
        tar.add(original_path, arcname=arcname)

if __name__ == "__main__":
    pack_for_submission()
