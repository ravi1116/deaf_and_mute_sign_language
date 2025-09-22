WELCOME TO SIH 
CONGRATS IF YOU MADE IT TILL HERE COZ IF YOU ARE SEEING THIS IT MEAN WE WON THE FIRST LEVEL AND WE WE ARE AT LEVEL 2 OF THE SIH 
🚀 Roadmap for MAITRI

Phase 1: Foundation (Day 1–2)

Goal: Set up base environment + core pipeline.
	•	✅ Choose tech stack:
	•	Backend: Python (FastAPI/Flask).
	•	Frontend: Streamlit or simple React web app.
	•	Models: Hugging Face models for speech-to-text + emotion detection.
	•	✅ Collect sample datasets for testing:
	•	Audio emotions: RAVDESS, CREMA-D.
	•	Facial emotions: FER2013, AffectNet (use pre-trained).
	•	✅ Implement webcam + mic capture → save stream (via frontend).
	•	✅ Set up speech-to-text (Whisper small model) → confirm text output from audio.

📌 Deliverable: You can record yourself, get live transcription & store it in a database.

⸻

Phase 2: Emotion Detection (Day 3–4)

Goal: Detect stress/emotion from audio & video.
	•	✅ Audio module:
	•	Use pre-trained audio emotion recognition model (SpeechEmotionRecognition / SER).
	•	Output: {happy, sad, angry, neutral, stressed}.
	•	✅ Video module:
	•	Use MediaPipe or OpenCV + lightweight CNN (FER+ pre-trained) to classify emotions.
	•	Output: {happy, sad, neutral, fear, anger, surprise}.
	•	✅ Fuse results (rule-based at first):
	•	Example: If both audio & video detect “negative emotion”, increase stress score.

📌 Deliverable: When you talk to webcam, dashboard shows live emotion labels.

⸻

Phase 3: Conversational AI (Day 5–6)

Goal: Enable adaptive supportive dialogue.
	•	✅ Build dialogue engine:
	•	Option A: Rasa/Dialogflow (rule-based + intents).
	•	Option B: Use small LLM (like GPT-2 fine-tuned or distilGPT-2) + predefined prompts.
	•	✅ Map emotional state → supportive responses.
	•	Example:
	•	If stressed → respond with calming messages, breathing tips.
	•	If neutral → check-in questions.
	•	If positive → encouragement.
	•	✅ Store logs: emotion + conversation summary in SQLite/Postgres.

📌 Deliverable: System reacts to user’s stress with a supportive, short conversation.

⸻

Phase 4: Reporting & Dashboard (Day 7)

Goal: Present data for astronauts & ground crew.
	•	✅ Build simple dashboard (Plotly/Streamlit):
	•	Show emotion trend over session timeline.
	•	Stress alerts triggered.
	•	Conversation logs.
	•	✅ Export report (PDF/CSV) summarizing key findings.

📌 Deliverable: Ground-control style dashboard where you can see crew well-being trends.

⸻

Stretch Goals (If Time Allows)
	•	🔹 Physical well-being proxy: detect yawning, eye fatigue (via video).
	•	🔹 Personalized calibration (baseline 1 min “mood scan” per astronaut).
	•	🔹 Offline mode (edge deployment on device without internet).
	•	🔹 Multi-user monitoring (simulate multiple astronauts).

⸻

📊 Final Hackathon Demo Flow
	1.	Start session → webcam + mic capture.
	2.	System detects speech & emotions in real-time.
	3.	Dashboard shows live stress score & emotion.
	4.	If stress ↑ → AI assistant starts supportive conversation.
	5.	At end → report generated for ground crew.
