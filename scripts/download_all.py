import os
import json
import argparse
import requests
import zipfile
import tarfile

def download_file(url, dest_path):
    print(f"🔽 Downloading: {url}")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dest_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print(f"✅ Saved to: {dest_path}")

def extract_file(file_path, extract_to, filetype):
    print(f"📦 Extracting: {file_path}")
    if filetype == "zip":
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    elif filetype == "tar.gz":
        with tarfile.open(file_path, 'r:gz') as tar_ref:
            tar_ref.extractall(extract_to)
    print(f"✅ Extracted to: {extract_to}")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def load_config(path):
    with open(path, "r") as f:
        return json.load(f)

def list_datasets(datasets):
    print("📚 Available datasets:")
    for key, info in datasets.items():
        print(f"• {key} — {info.get('name', '')}")

def process_dataset(key, info, raw_data_root):
    name = info.get("name", key)
    url = info.get("url")
    filetype = info.get("filetype")
    target_dir = os.path.join(raw_data_root, info.get("target_dir", key))

    print(f"\n📁 Processing dataset: {name}")

    if not url:
        print(f"⚠️  Skipped: No URL provided.")
        return

    ensure_dir(target_dir)
    filename = f"{key}.{filetype.replace('.', '')}"
    dest_path = os.path.join(target_dir, filename)

    if os.path.exists(dest_path):
        print(f"✅ Already exists: {dest_path}")
    else:
        try:
            download_file(url, dest_path)
        except Exception as e:
            print(f"❌ Failed to download {name}: {e}")
            return

    try:
        extract_file(dest_path, target_dir, filetype)
    except Exception as e:
        print(f"❌ Failed to extract {name}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Download Document Understanding Datasets")
    parser.add_argument("--only", help="Download a single dataset by key")
    parser.add_argument("--list", action="store_true", help="List available dataset keys")
    args = parser.parse_args()

    config_path = "scripts/datasets_config.json"
    raw_data_root = "datasets_raw"
    datasets = load_config(config_path)

    if args.list:
        list_datasets(datasets)
        return

    ensure_dir(raw_data_root)

    if args.only:
        if args.only not in datasets:
            print(f"❌ Dataset '{args.only}' not found.")
            list_datasets(datasets)
            return
        process_dataset(args.only, datasets[args.only], raw_data_root)
    else:
        for key, info in datasets.items():
            process_dataset(key, info, raw_data_root)

if __name__ == "__main__":
    main()