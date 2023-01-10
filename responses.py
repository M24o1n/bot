def respond_handle(message) -> str : 
    mm = message.lower()

    if mm == "hi":
        return "キタ〜ン✨"
    elif mm == "hello":
        return "こんにちは〜"
    elif mm == "bye":
        return "バイバイ〜"
    elif mm == "goodbye":
        return "さようなら〜"
    elif mm == "good night":
        return "おやすみ〜"
    elif mm == "good morning":
        return "おはよう〜"
    elif mm == "good afternoon":
        return "こんにちは〜"
    elif mm == "english":
        return "I don't speak English"
    else:
        return "I don't understand"