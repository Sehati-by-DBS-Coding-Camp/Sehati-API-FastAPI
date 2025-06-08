from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
import numpy as np

  # Sesuai model
def predict_emotion(text, model, tokenizer, label_encoder,max_sequence_length = 777):
    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=max_sequence_length)
    probabilities = model.predict(padded)[0]
    predicted_index = np.argmax(probabilities)
    predicted_label = label_encoder.inverse_transform([predicted_index])[0]

    # Buat dict hasil
    prob_dict = {
        label: round(float(prob * 100), 2)
        for label, prob in zip(label_encoder.classes_, probabilities)
    }

    return {
        "text": text,
        "predicted_label": predicted_label,
        "confidence": round(float(probabilities[predicted_index] * 100), 2),
        "probabilities": prob_dict
    }