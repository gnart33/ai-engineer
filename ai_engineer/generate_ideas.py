import chromadb
from typing_extensions import Annotated
import os
import dotenv
from pathlib import Path
import logging

dotenv.load_dotenv()

import autogen
from autogen import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

# Add at the top after imports
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class AgentFactory:
    """Factory class for creating different types of agents used in the chat system.

    Attributes:
        llm_config (dict): Configuration for the language model including model name, API key,
                          temperature, seed, and timeout settings.
    """

    def __init__(
        self,
        model: str,
        api_key: str,
        verbose: bool = True,
        # docs_path: str = "examples/hackathon01/resource/document/aggregated.md",
    ):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO if verbose else logging.WARNING)
        self.llm_config = {
            "model": model,
            "api_key": api_key,
            "tags": ["gpt-4", "tool"],
        }
        self.logger.info(f"Initialized AgentFactory with model: {model}")
        # self.docs_path = docs_path

    def _termination_msg(self, x):
        """Check if a message indicates termination.

        Args:
            x: Message to check, typically a dict

        Returns:
            bool: True if message indicates termination
        """
        return (
            isinstance(x, dict)
            and "TERMINATE" == str(x.get("content", ""))[-9:].upper()
        )

    def create_boss(self):
        self.logger.info("Creating boss agent")
        agent = autogen.UserProxyAgent(
            name="Boss",
            is_termination_msg=self._termination_msg,
            human_input_mode="NEVER",
            code_execution_config=False,
            default_auto_reply="Reply `TERMINATE` if the task is done.",
            description="The boss who ask questions and give tasks.",
        )
        self.logger.info(f"Created boss agent: {agent}")
        return agent

    def create_boss_assistant(self):
        """Create a boss assistant agent with document retrieval capabilities."""
        self.logger.info("Creating boss assistant agent")
        
        # Validate document path exists
        docs_path = "/Users/nvtrang/Projects/bglabs/ai-engineer/examples/hackathon01/resource/document/01_overview.md"
        if not os.path.exists(docs_path):
            self.logger.error(f"Document path does not exist: {docs_path}")
            raise FileNotFoundError(f"Document path not found: {docs_path}")

        try:
            agent = RetrieveUserProxyAgent(
                name="Boss_Assistant",
                is_termination_msg=self._termination_msg,
                human_input_mode="NEVER",
                default_auto_reply="Reply `TERMINATE` if the task is done.",
                max_consecutive_auto_reply=3,
                retrieve_config={
                    "task": "code",
                    "docs_path": docs_path,
                    "chunk_token_size": 1000,
                    "model": self.llm_config["model"],
                    "collection_name": "groupchat",
                    "get_or_create": True,
                    "embedding_model": "all-MiniLM-L6-v2",
                    "client_settings": {
                        "anonymized_telemetry": False  # Disable telemetry
                    }
                },
                code_execution_config=False,
                description="Assistant who has extra content retrieval power for solving difficult problems.",
            )
            self.logger.info(f"Created boss assistant agent: {agent}")
            return agent
        except Exception as e:
            self.logger.error(f"Failed to create boss assistant: {str(e)}")
            raise

    def create_coder(self):
        """Create a senior Python engineer agent for code implementation.

        Returns:
            AssistantAgent: An agent specialized in writing Python code
        """
        self.logger.info("Creating coder agent")
        agent = AssistantAgent(
            name="Senior_Python_Engineer",
            is_termination_msg=self._termination_msg,
            system_message="You are a senior python engineer, you provide python code to answer questions. Reply `TERMINATE` in the end when everything is done.",
            llm_config=self.llm_config,
            description="Senior Python Engineer who can write code to solve problems and answer questions.",
        )
        self.logger.info(f"Created coder agent: {agent}")
        return agent

    def create_pm(self):
        """Create a product manager agent for project planning and design.

        Returns:
            AssistantAgent: An agent specialized in product management
        """
        self.logger.info("Creating product manager agent")
        agent = autogen.AssistantAgent(
            name="Product_Manager",
            is_termination_msg=self._termination_msg,
            system_message="You are a product manager. Reply `TERMINATE` in the end when everything is done.",
            llm_config=self.llm_config,
            description="Product Manager who can design and plan the project.",
        )
        self.logger.info(f"Created product manager agent: {agent}")
        return agent

    def create_reviewer(self):
        """Create a code reviewer agent for code quality assessment.

        Returns:
            AssistantAgent: An agent specialized in code review
        """
        self.logger.info("Creating code reviewer agent")
        agent = autogen.AssistantAgent(
            name="Code_Reviewer",
            is_termination_msg=self._termination_msg,
            system_message="You are a code reviewer. Reply `TERMINATE` in the end when everything is done.",
            llm_config=self.llm_config,
            description="Code Reviewer who can review the code.",
        )
        self.logger.info(f"Created code reviewer agent: {agent}")
        return agent


class ChatManager:
    """Manages different types of chat interactions between agents.

    Attributes:
        problem (str): The problem or task to be discussed
        agent_factory (AgentFactory): Factory for creating different agents
        boss, boss_aid, coder, pm, reviewer: Different agent instances
    """

    def __init__(
        self,
        problem: str,
        api_key: str,
        verbose: bool = True,
        model: str = "gpt-4o-mini",
    ):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO if verbose else logging.WARNING)
        self.logger.info(f"Initializing ChatManager with problem: {problem}")
        
        self.problem = problem
        self.agent_factory = AgentFactory(model, api_key, verbose=verbose)
        self.boss = self.agent_factory.create_boss()
        self.boss_aid = self.agent_factory.create_boss_assistant()
        self.coder = self.agent_factory.create_coder()
        self.pm = self.agent_factory.create_pm()
        self.reviewer = self.agent_factory.create_reviewer()
        self.logger.info("Finished initializing all agents")

    def _reset_agents(self):
        self.logger.info("Resetting all agents")
        self.boss.reset()
        self.boss_aid.reset()
        self.coder.reset()
        self.pm.reset()
        self.reviewer.reset()
        self.logger.debug("All agents reset successfully")

    def rag_chat(self):
        self.logger.info("Starting RAG chat")
        # self._reset_agents()
        
        groupchat = autogen.GroupChat(
            agents=[self.boss_aid, self.pm, self.coder, self.reviewer],
            messages=[],
            max_round=12,
            speaker_selection_method="round_robin",
        )
        self.logger.debug(f"Created groupchat with {len(groupchat.agents)} agents")
        
        manager = autogen.GroupChatManager(
            groupchat=groupchat, llm_config=self.agent_factory.llm_config
        )
        self.logger.debug("Created group chat manager")
        
        self.logger.info("Initiating chat with boss assistant")
        self.boss_aid.initiate_chat(
            manager,
            message=self.boss_aid.message_generator,
            problem=self.problem,
            n_results=3,
        )
        self.logger.info("RAG chat completed")

    def norag_chat(self):
        """Initialize and run a chat without RAG capabilities."""
        self._reset_agents()
        groupchat = autogen.GroupChat(
            agents=[self.boss, self.pm, self.coder, self.reviewer],
            messages=[],
            max_round=12,
            speaker_selection_method="auto",
            allow_repeat_speaker=False,
        )
        manager = autogen.GroupChatManager(
            groupchat=groupchat, llm_config=self.agent_factory.llm_config
        )
        self.boss.initiate_chat(
            manager,
            message=self.problem,
        )

    def call_rag_chat(self):
        """Initialize and run a chat with RAG capabilities using function calling."""
        self._reset_agents()

        # Define content retrieval function that will be available to agents
        def retrieve_content(
            message: Annotated[
                str,
                "Refined message which keeps the original meaning and can be used to retrieve content for code generation and question answering.",
            ],
            n_results: Annotated[int, "number of results"] = 3,
        ) -> str:
            """Retrieve relevant content based on the input message.

            Args:
                message (str): The query message to search for relevant content
                n_results (int): Number of results to retrieve

            Returns:
                str: Retrieved content or original message if no content found
            """
            self.boss_aid.n_results = n_results
            _context = {"problem": message, "n_results": n_results}
            ret_msg = self.boss_aid.message_generator(self.boss_aid, None, _context)
            return ret_msg or message

        # Disable human input for boss assistant
        self.boss_aid.human_input_mode = "NEVER"

        # Register content retrieval function for different agents
        for caller in [self.pm, self.coder, self.reviewer]:
            d_retrieve_content = caller.register_for_llm(
                description="retrieve content for code generation and question answering.",
                api_style="function",
            )(retrieve_content)

        # Register execution capability for boss and PM
        for executor in [self.boss, self.pm]:
            executor.register_for_execution()(d_retrieve_content)

        # Set up group chat with round-robin speaker selection
        groupchat = autogen.GroupChat(
            agents=[self.boss, self.pm, self.coder, self.reviewer],
            messages=[],
            max_round=12,
            speaker_selection_method="round_robin",
            allow_repeat_speaker=False,
        )

        manager = autogen.GroupChatManager(
            groupchat=groupchat, llm_config=self.agent_factory.llm_config
        )
        self.boss.initiate_chat(
            manager,
            message=self.problem,
        )
