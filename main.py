from scene_creator import generate_scene
from annotations import generate_annotations
from postprocessing import ai_postprocess
from ml_pipeline import integrate_with_pipeline

def main():
    print("Starting synthetic data generation process...")

    # Step 1: Create synthetic scenes
    scene_data = generate_scene()

    # Step 2: Generate annotations
    annotations = generate_annotations(scene_data)

    # Step 3: AI-based postprocessing
    processed_data = ai_postprocess(scene_data)

    # Step 4: Integrate into ML pipeline
    integrate_with_pipeline(processed_data, annotations)

    print("Dataset successfully created and integrated.")

if __name__ == "__main__":
    main()
