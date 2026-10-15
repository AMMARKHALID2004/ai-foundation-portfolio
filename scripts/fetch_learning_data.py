"""Download original lesson assets locally using GitHub CLI; never stage them."""

import argparse
import base64
import hashlib
import json
from pathlib import Path
import subprocess
from urllib.parse import quote


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", help="Fetch only one source repository, e.g. Pandas")
    parser.add_argument("--list", action="store_true", help="List assets without downloading")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "docs/import-manifest.json").read_text())
    sources = manifest["repositories"]
    if args.repo:
        sources = [source for source in sources if source["repository"] == args.repo]
        if not sources:
            parser.error("Unknown source repository; see docs/IMPORTED_WORK.md")
    for source in sources:
        for asset in source["external_data_assets"]:
            destination = (root / asset["local_path"]).resolve()
            source_folder = (root / source["destination"]).resolve()
            if (not source_folder.is_relative_to(root)
                    or source_folder == root
                    or not destination.is_relative_to(source_folder)):
                raise ValueError("Asset path must stay inside its recorded source folder")
            expected = asset["source_sha256"]
            if args.list:
                print(f"{source['repository']}: {asset['path']}")
                continue
            if destination.exists():
                actual = hashlib.sha256(destination.read_bytes()).hexdigest()
                if actual == expected:
                    print(f"Already available: {asset['local_path']}")
                    continue
                raise FileExistsError(f"Preserving different local file: {destination}")
            endpoint = (
                f"repos/AMMARKHALID2004/{source['repository']}/contents/"
                f"{quote(asset['path'], safe='/')}?ref={source['source_commit']}"
            )
            result = subprocess.run(
                ["gh", "api", endpoint, "-H", "Accept: application/vnd.github.raw+json"],
                check=True, capture_output=True,
            )
            content = result.stdout
            actual = hashlib.sha256(content).hexdigest()
            if actual != expected:
                # Some API clients return JSON for this endpoint despite the raw header.
                try:
                    metadata = json.loads(content)
                    content = base64.b64decode(metadata["content"])
                except (ValueError, KeyError, TypeError) as error:
                    raise ValueError(f"Unexpected bytes for {asset['local_path']}") from error
                if hashlib.sha256(content).hexdigest() != expected:
                    raise ValueError(f"Source hash differs for {asset['local_path']}")
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(content)
            print(f"Downloaded: {asset['local_path']}")


if __name__ == "__main__":
    main()
