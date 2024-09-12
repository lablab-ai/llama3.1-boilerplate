import streamlit as st
from src.api.model_integration import stream_response
from src.utils.prompt_templates import (
    get_translation_prompt,
    get_sentiment_analysis_prompt,
    get_cultural_reference_explanation_prompt,
    get_interactive_translation_prompt,
)
from config.config import Config


def setup_page():
    """
    Sets up the page with custom styles and page configuration.
    """
    st.set_page_config(
        page_title="Advanced Llama 3.1 Cultural Translator",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(
        """
        <style>
        :root {
            --llama-color: #4e8cff;
            --llama-color-light: #e6f0ff;
            --llama-color-dark: #1a3a6c;
            --llama-gradient-start: #4e54c8;
            --llama-gradient-end: #8f94fb;
        }
        .stApp {
            margin: auto;
            background-color: var(--background-color);
            color: var(--text-color);
        }
        .logo-container {
            display: flex;
            justify-content: center;
            margin-bottom: 1rem;
        }
        .logo-container img {
            width: 150px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():
    setup_page()

    # Header section with title and subtitle
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 class="header-title">🦙 Meta-Llama 3.1 Cultural Translator</h1>
            <p class="header-subtitle">Powered by Meta's advanced language models</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Meta logo
    st.markdown(
        """
        <div class="logo-container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/7/7b/Meta_Platforms_Inc._logo.svg" alt="Meta Logo">
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Remove the Llama image display

    # Sidebar for settings
    with st.sidebar:
        st.title("🦙 Llama Translator Settings")
        model_name = st.selectbox("Choose a model", Config.AVAILABLE_MODELS)

        source_lang = st.selectbox(
            "From", ["English", "Spanish", "French", "German", "Japanese"]
        )
        target_lang = st.selectbox(
            "To", ["Spanish", "English", "French", "German", "Japanese"]
        )
        cultural_context = st.selectbox(
            "Context", ["Formal", "Casual", "Business", "Youth Slang", "Poetic"]
        )

    # Main container with border
    main_container = st.container(border=True)

    with main_container:
        st.header("Enter Text for Translation and Analysis")
        text = st.text_area(
            "Text to translate",
            "It was the best of times, it was the worst of times...",
            height=200,
        )
        st.caption(f"Character count: {len(text)}")

        if st.button("Translate and Analyze", type="primary"):
            if text:
                # Tabs for different analysis types
                tab1, tab2, tab3, tab4 = st.tabs(
                    [
                        "Translation",
                        "Sentiment Analysis",
                        "Cultural References",
                        "Interactive Translation",
                    ]
                )

                # Tab 1: Translation
                with tab1:
                    st.subheader("Translation Result")
                    translation_container = st.empty()
                    translation_prompt = get_translation_prompt(
                        text, source_lang, target_lang, cultural_context
                    )
                    translation = stream_response(
                        [{"role": "user", "content": translation_prompt}],
                        translation_container,
                        model_name,
                    )

                # Tab 2: Sentiment Analysis
                with tab2:
                    st.subheader("Sentiment Analysis")
                    sentiment_container = st.empty()
                    sentiment_prompt = get_sentiment_analysis_prompt(text, source_lang)
                    sentiment_analysis = stream_response(
                        [{"role": "user", "content": sentiment_prompt}],
                        sentiment_container,
                        model_name,
                    )

                # Tab 3: Cultural References
                with tab3:
                    st.subheader("Cultural References")
                    cultural_container = st.empty()
                    cultural_prompt = get_cultural_reference_explanation_prompt(
                        text, source_lang, target_lang
                    )
                    cultural_references = stream_response(
                        [{"role": "user", "content": cultural_prompt}],
                        cultural_container,
                        model_name,
                    )

                # Tab 4: Interactive Translation
                with tab4:
                    st.subheader("Interactive Translation")
                    interactive_container = st.empty()
                    interactive_prompt = get_interactive_translation_prompt(
                        text, source_lang, target_lang
                    )
                    interactive_translation = stream_response(
                        [{"role": "user", "content": interactive_prompt}],
                        interactive_container,
                        model_name,
                    )

    # Sidebar for additional information and feedback
    with st.sidebar:
        st.subheader("About")
        st.info("This app demonstrates Meta's Llama 3.1 capabilities.")

        st.subheader("Feedback")
        feedback = st.text_area("Leave your feedback here", height=100)
        if st.button("Submit Feedback"):
            st.success("Thank you for your feedback!")


if __name__ == "__main__":
    main()
