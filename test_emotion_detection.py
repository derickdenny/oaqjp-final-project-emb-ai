from EmotionDetection import emotion_detector

def test_emotion_detector():
    
    # Test cases
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]
    
    # Run tests
    for statement, expected_emotion in test_cases:
        result = emotion_detector(statement)
        detected_emotion = result['dominant_emotion']
        
        assert detected_emotion == expected_emotion, \
            f"Test failed for: '{statement}'. Expected: {expected_emotion}, Got: {detected_emotion}"
    
    print("All tests passed!")

# Run tests
if __name__ == "__main__":
    test_emotion_detector()