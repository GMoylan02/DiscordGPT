from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, SystemMessage
import dotenv

dotenv.load_dotenv()

chat = ChatOpenAI()
conversation = ConversationChain(llm=chat)
system_message = SystemMessage(content="You are a funny Discord chat bot who provides humorous responses during a "
                                       "conversation.")


def get_response(user_input: str) -> str:
    if user_input == '':
        return 'User input not found'

    return chat([system_message, HumanMessage(content=user_input)]).content




