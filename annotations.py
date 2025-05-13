def generate_annotations(scene_data):
    print("Generating annotations...")

    # Simulate annotation creation
    annotations = {
        'label': scene_data['geometry'],
        'position': [0, 0, 0],
        'rotation': [0, 0, 0],
        'scale': [1, 1, 1]
    }

    print(f"Annotations: {annotations}")
    return annotations
