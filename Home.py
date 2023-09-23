import streamlit as st


from utils import caption_block, get_sentiment, spell_check, get_sentence_sentiment, sentiment_sample_text, get_pos


st.title('📝 Natural language processing')
st.caption(caption_block)


tab1, tab2, tab3 = st.tabs(
    ["Sentiment Analysis", "Spelling Correction", "Part-of-speech Tagging"])


with tab1:
    st.header("Sentiment Analysis")
    sentiment_text = st.text_area(
        label="Enter the text to analyse 🔍", value=sentiment_sample_text.strip())
    sentiment_output = get_sentiment(text=sentiment_text)
    st.metric(
        label="$$Sentiment Score$$",
        value=sentiment_output[0],
        delta=round(sentiment_output[1], 2)
    )

    input_sentences = get_sentence_sentiment(sentiment_text)
    for i_sen in input_sentences:
        st.markdown(i_sen)


with tab2:
    st.header("Spelling Correction")

    spelling_text = st.text_input(
        label="Enter the text to spell check 🖋", value="I hav a car")
    spelling_output = spell_check(spelling_text)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Correction ✅")
        st.write(spelling_output)
    with col2:
        st.markdown("#### Input ✍")
        st.caption(spelling_text)


with tab3:
    pos_input_text = st.text_input(
        label="Enter your text ✏", value="I am cool.")
    pos_output_df = get_pos(pos_input_text)
    st.write(pos_output_df)
