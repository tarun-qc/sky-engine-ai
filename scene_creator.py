import numpy as np
import os

def generate_scene():
    print("Generating synthetic scene...")

    # Simulate asset selection and randomization
    geometry = np.random.choice(['cube', 'sphere', 'cylinder'])
    texture_id = np.random.randint(1, 10)
    animation = np.random.choice(['rotate', 'bounce', 'stretch'])

    scene_data = {
        'geometry': geometry,
        'texture_id': texture_id,
        'animation': animation
    }

    print(f"Scene generated with: {scene_data}")
    return scene_data
