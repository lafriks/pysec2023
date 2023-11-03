"""Script to download file with progress bar"""

from urllib.request import urlretrieve
import sys

class ProgressBar:
    """Progress print instance"""
    last_progress = 0

    def print_progress(self, block_num, block_size, total_size):
        """Print download progress"""
        p = int((block_num * block_size / total_size) * 22)

        if self.last_progress != p:
            print("*", end="", flush=True)
            self.last_progress = p

    def __enter__(self):
        print('|0%-------50%----100%|')
        return self

    def __exit__(self, exc_type, *_):
        print()
        if exc_type is None:
            return True
        return False

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print("example12 <url> <dest>")
        sys.exit(1)

    download_url = sys.argv[1]
    filename = sys.argv[2]

    print(f"Downloading to file {filename} from URL {download_url}")

    try:
        with ProgressBar() as p:
            urlretrieve(download_url, filename, p.print_progress)
    except Exception as e:
        print(f"Failed to download file: {e}")
