from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool
from tools.custom_tool import FileReaderTool
from dotenv import load_dotenv



load_dotenv()


#file_path = "srs2sdd/src/srs2sdd/SRS.docx"
#file_path = "src/srs2sdd/SRS.docx"







@CrewBase
class SrsToSdd():
	"""SrsToSdd crew"""

	
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self, file_path=None):
		self.file_path = file_path

	
	@agent
	def srs_extractor(self) -> Agent:
		return Agent(
			config=self.agents_config['srs_extractor'],
			tools = [FileReaderTool(file_path=self.file_path)],
			verbose=True
		)

	@agent
	def sdd_structure(self) -> Agent:
		return Agent(
			config=self.agents_config['sdd_structure'],
			verbose=True
		)
	
	@agent
	def er_schema_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['er_schema_generator'],
			verbose=True
		)
	
	@agent
	def content_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['content_generator'],
			verbose=True
		)
	
	@agent
	def wireframe_designer(self) -> Agent:
		return Agent(
			config=self.agents_config['wireframe_designer'],
			verbose=True
		)
	
	@agent
	def interface_validator(self) -> Agent:
		return Agent(
			config=self.agents_config['interface_validator'],
			verbose=True
		)
	

	
	@agent
	def validation_compliance(self) -> Agent:
		return Agent(
			config=self.agents_config['validation_compliance'],
			verbose=True
		)
	
	@agent
	def final_formatter(self) -> Agent:
		return Agent(
			config=self.agents_config['final_formatter'],
			tools = [FileWriterTool()],
			verbose=True
		)
	
	

	
	@task
	def extract_srs(self) -> Task:
		return Task(
			config=self.tasks_config['extract_srs'],
		)

	@task
	def define_sdd_structure(self) -> Task:
		return Task(
			config=self.tasks_config['define_sdd_structure'],
		)
	
	@task
	def generate_er_schema(self) -> Task:
		return Task(
			config=self.tasks_config['generate_er_schema'],
		)
	

	
	@task
	def generate_sdd_content(self) -> Task:
		return Task(
			config=self.tasks_config['generate_sdd_content'],
		)
	
	@task
	def generate_wireframe_descriptions(self) -> Task:
		return Task(
			config=self.tasks_config['generate_wireframe_descriptions'],
		)
	
	@task
	def define_interface_validation_rules(self) -> Task:
		return Task(
			config=self.tasks_config['define_interface_validation_rules'],
		)
	

	
	@task
	def validate_sdd(self) -> Task:
		return Task(
			config=self.tasks_config['validate_sdd'],
		)
	
	@task
	def format_export_sdd(self) -> Task:
		return Task(
			config=self.tasks_config['format_export_sdd'],
		)

	
	
	
	
	
	
	
	
	
	@crew
	def crew(self) -> Crew:
		"""Creates the SrsToSdd crew"""
		
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
			
		)


