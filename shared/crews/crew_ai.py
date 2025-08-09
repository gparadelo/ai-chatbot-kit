from pathlib import Path
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

BASE_DIR = Path(__file__).parent


@CrewBase
class CrewaiConversationalChatbotCrew:
    """CrewaiConversationalChatbot crew"""

    agents_config = str(BASE_DIR / "agent.yaml")
    tasks_config = str(BASE_DIR / "tasks.yaml")

    @agent
    def assistant(self) -> Agent:
        return Agent(
            config=self.agents_config["assistant"],
            verbose=False,
        )

    @task
    def assistant_task(self) -> Task:
        return Task(config=self.tasks_config["assistant_task"], agent=self.assistant())

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiConversationalChatbot crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=0,
        )