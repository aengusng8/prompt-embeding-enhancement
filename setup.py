import os, sys


def setup():
    move_new_pipeline_to_diffusers()


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
