def generate_quiz(topic):
    return {
        "type": "quiz",
        "content": [
            f"What is {topic}?",
            f"Explain key concepts of {topic}.",
            f"Give a real-world example of {topic}."
        ]
    }

def summarize_notes(text):
    return {
        "type": "summary",
        "content": text[:200] + "..."
    }

def create_study_plan(topic):
    return {
        "type": "study_plan",
        "content": [
            f"Day 1: Learn basics of {topic}",
            f"Day 2: Practice problems",
            f"Day 3: Revision"
        ]
    }