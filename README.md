# Resume Job Agent

An AI-powered Job Search Assistant built using **Python, Google Agent Development Kit (ADK), and Google Gemini**.

The project demonstrates how AI agents can help users discover relevant job opportunities and receive job recommendations based on their skills and career interests.

## Project Overview

Resume Job Agent is designed to simplify the job search process using an AI agent.

The agent uses Google ADK to organize agent behavior and Gemini to understand user requests, interpret job-related information, and generate helpful responses.

## Technologies Used

- **Python** – Core programming language
- **Google ADK** – AI agent development framework
- **Google Gemini** – Large language model
- **Git and GitHub** – Version control and source code management

## Project Architecture

```text
User
  |
  v
Google ADK Agent
  |
  v
Gemini LLM
  |
  v
Job Search Tools
  |
  v
Job Recommendations
  |
  v
User
```

## Project Structure

```text
resume-job-agent/
|
|-- resume_agent/
|   |-- __init__.py
|   |-- agent.py
|   |-- job_tools.py
|   |-- .gitignore
|
|-- .gitignore
|-- README.md
```

## How It Works

1. The user submits a job-related query.
2. Google ADK processes the request through the AI agent.
3. Gemini interprets the user's requirements.
4. The agent uses available job-search tools to retrieve or process relevant job information.
5. The agent generates a response with job recommendations.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sneha2K/resume-job-agent.git
cd resume-job-agent
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install google-adk python-dotenv
```

### 4. Configure Gemini

Create a `.env` file inside the `resume_agent` folder and configure your Google Gemini API credentials according to the authentication method used by your agent.

For API-key authentication, the typical configuration is:

```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here
```

Never commit API keys or `.env` files to GitHub.

### 5. Run the Agent

From the project root directory:

```bash
adk web
```

Open the local URL displayed in your terminal and select the Resume Agent.

## Example User Queries

- Find Python Developer jobs.
- Suggest Data Engineer opportunities.
- Find jobs that match my Python and SQL skills.
- Recommend entry-level AI Engineer roles.

These are example queries illustrating the intended use of the agent.

## Future Enhancements

- Resume upload and parsing
- Skill extraction from resumes
- Job matching and ranking
- Integration with job search APIs
- Personalized job recommendations
- Job application tracking
- Automated job alerts

## Security

- Keep API credentials in environment variables.
- Exclude `.env` files from Git.
- Avoid committing local session data or private user information.

## Author

**Sneha Karri**

GitHub: [sneha2K](https://github.com/sneha2K)
