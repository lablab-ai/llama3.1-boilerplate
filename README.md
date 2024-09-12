
# LLaMA 3.1 Multilingual Translation Boilerplate

**Python Version:** 3.10+  
**Package Manager:** Pip  

## Introduction

This boilerplate provides a complete setup for working with Meta's LLaMA 3.1 model, enabling accurate, context-aware multilingual translations. While the default configuration is optimized for tasks like translation, sentiment analysis, and cultural adaptations, the setup is highly flexible. With minimal adjustments, you can modify the prompt templates to suit any other use case, whether it’s a different AI task or an entirely new application.

This means you can quickly build an app tailored to your needs, be it translations or any other AI-driven task, by simply updating the prompts and user interface. Whether you're a developer, linguist, or someone curious about AI, this setup provides all the tools necessary to explore the capabilities of LLaMA 3.1 and easily adapt it to your unique requirements.

## Current Core Capabilities

- **Multilingual Translation**: Translate text between multiple languages while adapting the translation to specific cultural and contextual nuances.
- **Sentiment Analysis**: Analyze the emotional tone of the input text, providing insights into positive, negative, and neutral sentiments.
- **Cultural Adaptations**: Identify and explain cultural references within the text to make translations contextually relevant.
- **Interactive Translation**: Provide deeper, interactive translations that include explanations, context, etymology, and usage notes.
- **Customizable Prompt Templates**: Modify or extend the built-in prompts to handle different translation tasks or styles tailored to specific needs.

## Getting Started

### Prerequisites

Ensure your development environment meets the following requirements:

- Python 3.10 or higher
- API keys for AI/ML provider ([AI/ML API Keys](https://aimlapi.com/app/keys/)) for hosted models or access to OLLAMA for local models

### Installation

1. Clone the boilerplate repository:

    ```bash
    git clone https://github.com/yourusername/llama3.1-translation-boilerplate.git
    cd llama3.1-translation-boilerplate
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Copy the `.env.example` file to `.env`:

    ```bash
    cp .env.example .env
    ```

2. Add your API credentials in the `.env` file:

    ```bash
    HOSTED_BASE_URL=https://api.aimlapi.com/v1
    HOSTED_API_KEY={ ai/ml api key here }
    LOCAL_BASE_URL=http://localhost:11434/api/chat
    ```

   - **For AI/ML API (Hosted Model)**: Visit [AI/ML API Keys page](https://aimlapi.com/app/keys/) to generate your API key.
   - **For OLLAMA (Local Model)**: Download and set up OLLAMA from [here](https://ollama.com/download) and run the LLaMA 3.1 model locally on your machine.

3. Update the configuration in `config/config.py` to select the correct model for your project. This can be a hosted API or a locally running model.

## Usage

### Running the Application

To start the translation app, run the following command:

```bash
python main.py
```

This will launch the Streamlit app, where you can input text for translation, select source and target languages, and view results such as translation output, sentiment analysis, and cultural reference explanations.

### Customization

You can modify the behavior of the app by editing the `src/utils/prompt_templates.py` file. These templates define how the LLaMA 3.1 model is prompted for tasks such as translation, sentiment analysis, and more.

For example, you can adjust the `get_translation_prompt()` function to adapt translations to different tones or target specific audiences.

## Project Structure

```
llama3.1-translation-boilerplate/
├── config/
│   ├── __init__.py
│   └── config.py                  # Manages API and model configurations
│
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   └── model_integration.py   # Handles API requests for both local and hosted models
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── prompt_templates.py    # Contains customizable prompt templates for tasks
│   │
│   └── __init__.py
│
├── .env.example                    # Example environment file for API keys
├── app.py                          # Main application logic for Streamlit
├── main.py                         # Entry point to start the app
├── README.md
└── requirements.txt                # Lists the required dependencies
```

### Explanation of Key Directories

- **config/**: Contains configuration files, including the API credentials and available model options (local or hosted).
  
- **src/**: The core functionality of the app:
  - **api/**: Contains the logic for interacting with the LLaMA 3.1 models, either via a hosted API or running locally through OLLAMA.
  - **utils/**: Contains customizable prompt templates for translation, sentiment analysis, and cultural references. You can modify these to fit your specific use cases.
  
- **app.py**: This file contains the Streamlit application logic. It defines how the user interface is displayed and how different tasks like translation or sentiment analysis are handled.

## Modifying and Extending

You can easily extend this boilerplate to suit additional needs:

- **Add More Languages**: Update the `app.py` file to add more language options in the dropdown for both source and target languages.
- **Modify Templates**: If you need to change the way the LLaMA model is prompted for translations or analyses, edit the functions in `prompt_templates.py`.
- **Add New Features**: For advanced users, you can integrate additional features such as voice-based translation or live multilingual chat by extending the logic in the `api/` and `utils/` directories.

## Conclusion

This boilerplate provides a robust and flexible framework for integrating the LLaMA 3.1 model into your translation projects. Whether you're looking to build a multilingual translator, perform sentiment analysis across languages, or explore cultural adaptations, this setup offers the foundational tools to get started quickly and scale your project over time.

For any issues or further documentation, you can refer to Meta's LLaMA documentation [here](https://ai.facebook.com/research/publications/introducing-llama/).

--- 
