from pydantic import BaseModel, Field, HttpUrl, ConfigDict


class LLMConfig(BaseModel):
    """LLM提供商配置"""
    base_url: HttpUrl = "https://api.deepseek.com"  # 模型基础URL地址
    api_key: str = ""  # 模型API秘钥
    model_name: str = "deepseek-reasoner"  # 模型名字，默认使用deepseek-reasoner带推理的模型，传递tools会自动切换到deepseek-chat
    temperature: float = Field(0.7)  # 温度，默认设置为0.7
    max_tokens: int = Field(8192, ge=0)  # 最大输出token数，默认设置为deepseek-chat模型的最大输出限制
    

class AppConfig(BaseModel):
    """应用配置信息，包含Agent配置、LLM提供商配置、MCP配置、A2A配置"""
    llm_config: LLMConfig
    # Pydantic配置，允许传递额外的字段初始化
    model_config = ConfigDict(extra="allow")
