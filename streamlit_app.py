def main():
    st.title("Streamlit Face-GAN Demo")

    # Step 1. Download models and data files.
    for filename in EXTERNAL_DEPENDENCIES.keys():
        download_file(filename)

    # Step 2. Read in models from the data files.
    tl_gan_model, feature_names = load_tl_gan_model()
    session, pg_gan_model = load_pg_gan_model()

    # Step 3. Draw the sidebar UI.
    ...
    features = ...  # Internally, this uses st.sidebar.slider(), etc.

    # Step 4. Synthesize the image.
    with session.as_default():
        image_out = generate_image(session, pg_gan_model, tl_gan_model,
                features, feature_names)

    # Step 5. Draw the synthesized image.
    st.image(image_out, use_column_width=True)
    
