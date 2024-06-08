import shutil
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_community.llms import Ollama
from sendEmail import send_email
ollama_mixtral = Ollama(model="mixtral", base_url="https://11434-01hzv9cbn7e9dg1k6ggzbqjkgt.cloudspaces.litng.ai")
email = 'testingcrewai@gmail.com'
message = 'testjkgvrjhfdbingjkbkjvfk m,d'
@CrewBase
class FinancialAnalystCrew:
    """FinancialAnalystCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.groq_llm = ollama_mixtral

    @agent
    def company_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['company_researcher'],
            llm=self.groq_llm
        )

    @agent
    def company_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['company_analyst'],
            llm=self.groq_llm
        )

    @task
    def research_company_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_company_task'],
            agent=self.company_researcher()
        )

    @task
    def analyze_company_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_company_task'],
            agent=self.company_analyst()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the FinancialAnalystCrew crew"""
        return Crew(
            agents=[self.company_researcher(), self.company_analyst()],
            tasks=[self.research_company_task(), self.analyze_company_task()],
            process=Process.sequential,
            verbose=2
        )

def main(report_parsed,receiver_email):
    crew = FinancialAnalystCrew()
    inputs = {"data": report_parsed}
    result=crew.crew().kickoff(inputs=inputs)
    send_email(email, receiver_email, result)
    try:
        shutil.rmtree('uploads')
        print('Folder and its content removed')
    except:
        print('Folder not deleted')