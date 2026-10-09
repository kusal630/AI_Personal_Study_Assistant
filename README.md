# AI Personal Study Assistant

A lightweight Python command-line study assistant that helps students learn through quizzes, note summaries, study plans, and AI-generated explanations.

## Overview

The assistant accepts natural-language requests and routes them to the appropriate capability:

- **Quiz generation** for a requested topic
- **Note summarization** for supplied study material
- **Study-plan creation** for a subject or topic
- **General explanations** powered by OpenAI when no specialized tool matches

It also keeps the last three user inputs in memory so they can be included as context for general AI responses.

## How It Works

The application is organized around a simple agent function in `main.py`:

1. The user enters a request in the command-line interface.
2. The request is saved to the in-memory conversation history.
3. Keyword-based routing selects a specialized study tool when applicable.
4. If no tool matches, the request is sent to OpenAI's `gpt-4o-mini` model.
5. The response is printed in the terminal.

## Project Structure

```text
.
├── main.py       # CLI loop, request routing, and OpenAI integration
├── tools.py      # Quiz, summary, and study-plan helpers
├── memory.py     # In-memory storage for the last three inputs
├── .env          # Local OpenAI API key configuration
└── README.md     # Project documentation
```

## Available Capabilities

| Request type | Example | Result |
|---|---|---|
| Quiz | `quiz Python decorators` | Returns questions about the requested topic |
| Summary | `summary Photosynthesis notes` | Returns a shortened version of the input |
| Study plan | `plan database systems` | Returns a basic three-day revision plan |
| Explanation | `Explain recursion` | Uses OpenAI to generate an explanation |

## Requirements

- Python 3.10 or newer
- An OpenAI API key for general explanation requests
- The following Python packages:
  - `openai`
  - `python-dotenv`

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/kusal630/AI_Personal_Study_Assistant.git
   cd AI_Personal_Study_Assistant
   ```

2. Install dependencies:

   ```bash
   pip install openai python-dotenv
   ```

3. Add your OpenAI API key to `.env`:

   ```env
   OPENAI_API_KEY=your-api-key-here
   ```

4. Start the assistant:

   ```bash
   python main.py
   ```

## Example Session

```text
You: quiz Python decorators
AI: {'type': 'quiz', 'content': [...]}

You: Explain recursion
AI: {'type': 'explanation', 'content': '...'}
```

## Current Limitations

- Tool selection currently uses simple keyword matching.
- Quiz and study-plan responses are template-based.
- Summaries are created by truncating the input rather than using an AI summarization model.
- Memory is stored only while the program is running and is limited to the last three inputs.
- There is currently no automated test suite or dependency lock file.

## Future Improvements

- Add structured argument parsing for topics, difficulty, dates, and available study time.
- Use OpenAI for richer quizzes, summaries, and personalized study plans.
- Replace keyword routing with a more robust agent or intent-classification system.
- Persist conversation history between sessions.
- Add tests, error handling, and a formal dependency file.

## License

No license has been specified for this repository yet.
