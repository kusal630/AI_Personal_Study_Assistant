# AI_Personal_Study_Assistant
An intelligent study companion built with the OpenAI Agents SDK that helps students learn more effectively through personalized quizzes, concise note summaries, and adaptive study plans. Built as part of the IIT Jammu Winter School on AI Agents.

Overview
This project demonstrates tool-integrated agentic reasoning using the OpenAI Agents SDK. A single intelligent agent decides when and how to use three custom tools based on the student's input — and with conversation memory enabled, it adapts to previous interactions to provide a truly personalized experience.

Tools & Capabilities
Tool	Input	Output
generate_quiz	Topic, difficulty level, number of questions	MCQ or short-answer quiz with answer key
summarize_notes	Topic or raw notes text	Concise bullet-point summary with key concepts
create_study_plan	Topics list, available days, exam date	Day-wise revision schedule with time allocation

Tech Stack
OpenAI Agents SDK — Agent and tool orchestration

Python 3.10+

OpenAI API — GPT-4o / GPT-4o-mini as the LLM backbone
