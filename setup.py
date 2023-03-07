import os, sys


def setup(clone=False):
    if clone:
        clone_diffusers()
    move_new_pipeline_to_diffusers()


def clone_diffusers():
    if not os.path.exists("v0.13.0.zip"):
        wget_link = "https://github.com/huggingface/diffusers/archive/refs/tags/v0.13.0.zip"
        os.system(f"wget {wget_link}")
    os.system("unzip v0.13.0.zip")
    # os.system("rm v0.13.0.zip")
    print("Successfully clone the stable version of diffusers (v0.13.0)")


def move_new_pipeline_to_diffusers():
    source2destination = [
        (
            "prompt_embeding_enhancement/pipeline_stable_diffusion_prompt_embeding_enhancement.py",
            "diffusers-0.13.0/src/diffusers/pipelines/stable_diffusion/pipeline_stable_diffusion_prompt_embeding_enhancement.py",
        ),
        (
            "prompt_embeding_enhancement/__init__1.py",
            "diffusers-0.13.0/src/diffusers/pipelines/stable_diffusion/__init__.py",
        ),
        (
            "prompt_embeding_enhancement/__init__2.py",
            "diffusers-0.13.0/src/diffusers/pipelines/__init__.py",
        ),
        (
            "prompt_embeding_enhancement/__init__3.py",
            "diffusers-0.13.0/src/diffusers/__init__.py",
        ),
    ]

    for source, destination in source2destination:
        # copy file from source to destination
        os.system(f"cp {source} {destination}")

    print("Successfully move the new pipeline to diffusers")


if __name__ == "__main__":
    # read "clone" to the command line to clone the stable version of diffusers
    clone = len(sys.argv) > 1 and sys.argv[1] == "-clone"
    setup(clone)
