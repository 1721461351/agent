import  dotenv
from openai import OpenAI
from pydantic import BaseModel, Field


dotenv.load_dotenv()

class SplitTasks(BaseModel):
    task_count: int = Field(..., gt=0 ,le=10, description="拆分的子任务数" )
    task_name: str

client = OpenAI()

