from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv
from phi.model.openai import OpenAIChat

load_dotenv()

agent = Agent(
    model=Groq(id='llama-3.3-70b-versatile')
)

agent.print_response("Motivational quote to explore the world")