def get_translation_prompt(text, source_lang, target_lang, cultural_context):
    """
    Returns a prompt for translating the given text while considering cultural context.
    """
    return f"""
    As an advanced cultural translation assistant, translate the following text from {source_lang} to {target_lang}, adapting it to a {cultural_context} context:

    "{text}"

    Provide your response in markdown format as follows, using Streamlit's markdown capabilities for enhanced visual appeal:

    ## :blue[Translation]
    > [Your translated text here]

    ## :green[Cultural Adaptations]
    - **Adaptation 1**: [Explanation]
    - **Adaptation 2**: [Explanation]
    [Add more adaptations as needed]

    ## :orange[Alternative Phrasings]
    1. ":violet[Original phrase]" → ":rainbow[Alternative 1]", ":rainbow[Alternative 2]"
       - _Context_: [Explain when to use each alternative]

    ## :red[Linguistic Analysis]
    - **Register**: [Formal/Informal/etc.]
    - **Tone**: [Describe the tone of the translation]
    - **Key Challenges**: [Discuss any particularly challenging aspects of the translation]
    """


def get_sentiment_analysis_prompt(text, source_lang):
    """
    Returns a prompt for conducting sentiment analysis on a given text.
    """
    return f"""
    Conduct a comprehensive sentiment analysis of the following {source_lang} text:

    "{text}"

    Provide your analysis in markdown format as follows:

    ## :blue[Overall Sentiment]
    [Positive/Negative/Neutral/Mixed]

    ## :green[Sentiment Breakdown]
    - **Positivity**: :smile: [Score from 0 to 1]
    - **Negativity**: :frowning: [Score from 0 to 1]
    - **Neutrality**: :neutral_face: [Score from 0 to 1]

    ## :orange[Key Emotional Indicators]
    1. **:heart: [Emotion 1]**: 
       - _Evidence_: ":violet[Relevant quote from text]"
       - _Explanation_: [Brief analysis]

    ## :earth_americas: Cultural Context
    [Explain how the sentiment might be perceived in the {source_lang}-speaking culture, considering any cultural-specific expressions or connotations]
    """


def get_cultural_reference_explanation_prompt(text, source_lang, target_lang):
    """
    Returns a prompt to explain cultural references in a source language for a target language audience.
    """
    return f"""
    As a cross-cultural communication expert, explain the cultural references in this {source_lang} text for someone from a {target_lang} background:

    "{text}"

    ## :earth_americas: Cultural References

    1. **:star: [Reference 1]**
       - _Meaning_: :blue[Explanation]
       - _Cultural Significance_: :green[Brief description]
       - _{target_lang} Equivalent_: :orange[Equivalent or similar concept, if applicable]
       - _Usage Example_: ":violet[Show how it's used in a sentence]"

    2. **:star: [Reference 2]**
       - _Meaning_: :blue[Explanation]
       - _Cultural Significance_: :green[Brief description]
       - _{target_lang} Equivalent_: :orange[Equivalent or similar concept, if applicable]
       - _Usage Example_: ":violet[Show how it's used in a sentence]"

    ## :globe_with_meridians: Overall Cultural Context
    [Summarize the cultural differences relevant to this text.]
    """


def get_interactive_translation_prompt(text, source_lang, target_lang):
    """
    Returns a prompt for providing an interactive, detailed translation with context.
    """
    return f"""
    Translate the following text from {source_lang} to {target_lang} and provide an overall analysis of its meaning, usage, and cultural relevance:

    "{text}"

    ## :books: General Translation
    **Text** → ":blue[Overall translation]"

    ## :arrows_counterclockwise: Contextual Usage and Adaptation
    1. ":green[Context 1]" - _Explanation_: [How the translation adapts to cultural context]
    2. ":orange[Context 2]" - _Explanation_: [Alternative contextual usage]

    ## :dna: Etymology and Origin
    - **Origin**: :violet[Brief description of word origins or key concepts]
    - **Related concepts**: :rainbow[If applicable, related words or phrases]

    ## :memo: Usage Notes
    - **Register**: :blue[Formal/Informal/etc.]
    - **Connotations**: :green[Positive/Negative connotations of the translation]
    - **Cultural Significance**: :orange[Explain the cultural impact or relevance of the translation]
    """
