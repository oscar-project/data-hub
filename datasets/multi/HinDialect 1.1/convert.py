'''
Converts names form non standard to bcp47.

For languages that have no code, we use the private identifier x- followed by max. 8 chars from file name.
'''
import os
import shutil
from pathlib import Path
from glob import glob
import langcodes 


files_to_ignore = ["requirements.txt"]

if __name__ == "__main__":

    dst = Path("standard/")
    try:
        os.mkdir(dst)
    except FileExistsError:
        pass
    for corpus in glob("*.txt"):
        if corpus not in files_to_ignore:
            (name, tag) = tuple(Path(corpus).stem.split('-')[:2])
            if tag == "mis":
                tag = f"x-{name[:8]}"
                assert langcodes.get(tag) 
                print(f"converting {name} to {tag}")

            shutil.copy(corpus, dst / Path(f"{tag}.txt"))
            

            
