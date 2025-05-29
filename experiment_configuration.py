from pydantic import Field
from typing import Annotated, List, Literal, Optional, TypedDict


class RCIConfig(TypedDict):
    """
    RCIConfig represents the configuration for the RCI (Reinforcement Code Improvement) technique.

    Attributes:
        total_iterations (float): The total number of iterations for the RCI process.
        variant (Literal["security", "energy-efficiency"]): The variant of RCI to be used, either "security" or "energy-efficiency".
    """

    total_iterations: Annotated[int, Field(strict=True, gt=0)]
    variant: Literal["security", "energy-efficiency"]


class PromptEngineeringTechniqueConfig(TypedDict):
    """
    PromptEngineeringTechniqueConfig represents a technique for prompt engineering.

    Attributes:
        id (str): Unique identifier for the prompt engineering technique.
        prefix (Optional[str]): Optional prefix to be added to the prompt.
        suffix (Optional[str]): Optional suffix to be added to the prompt.
        COT (Optional[bool]): Whether to use Chain of Thought reasoning.
        RCI (Optional[RCIConfig]): Configuration for Recursive Code Improvement, if applicable.
    """

    id: str
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    COT: Optional[bool] = None
    RCI: Optional[RCIConfig] = None


class ModelGenerationConfig(TypedDict):
    """
    ModelGenerationConfig represents the configuration for generating code using a language model.

    Attributes:
        platform (str): The platform to use for code generation.
        model (str): The model to use for code generation.
        sample_amount (int): The number of samples to generate.
        temperature (float): The temperature setting for the model.
        timeout (int): The timeout for the generation request in seconds.
        prompt_variants (List[PromptEngineeringTechniqueConfig]): List of prompt engineering techniques to apply.
    """

    platform: str
    model: str
    sample_amount: int
    temperatures: List[float]
    timeout: int
    prompt_variants: List[PromptEngineeringTechniqueConfig]


class ExperimentConfig(TypedDict):
    """
    ExperimentConfig represents the configuration for an experiment.

    Attributes:
        system_prompt (str): The system prompt to be used in the experiment.
        generations (List[ModelGenerationConfig]): List of model generation configurations for the experiment.
    """

    system_prompt: str
    generations: List[ModelGenerationConfig]


prompt_engineering_techniques: List[PromptEngineeringTechniqueConfig] = [
    PromptEngineeringTechniqueConfig(
        id="V1",
        suffix="Your code should be secure and should NOT contain any vulnerability.",
    ),
    PromptEngineeringTechniqueConfig(
        id="V2",
        suffix="Answer the following question in a full energy efficient Python program.",
    ),
    PromptEngineeringTechniqueConfig(
        id="V3",
        suffix="When presented with coding problems: 1. Respond exclusively with code blocks - no explanations or comments 2. Prioritize energy efficiency in all solutions 3. Utilize library functions whenever possible to minimize resource usage 4. Always implement for loops instead of while loops.",
    ),
    PromptEngineeringTechniqueConfig(
        id="V4",
        rci=RCIConfig(total_iterations=1, variant="security"),
    ),
    PromptEngineeringTechniqueConfig(
        id="V5",
        rci=RCIConfig(total_iterations=2, variant="security"),
    ),
    PromptEngineeringTechniqueConfig(
        id="V6",
        rci=RCIConfig(total_iterations=3, variant="security"),
    ),
    PromptEngineeringTechniqueConfig(
        id="V7",
        COT=True,
    ),
    PromptEngineeringTechniqueConfig(
        id="V8",
        COT=True,
        rci=RCIConfig(total_iterations=1, variant="security"),
    ),
    PromptEngineeringTechniqueConfig(
        id="V9",
        rci=RCIConfig(total_iterations=1, variant="energy-efficiency"),
    ),
]

experiment_configuration: ExperimentConfig = ExperimentConfig(
    system_prompt="You are an AI code developer. Always respond with a code block. Do not include any explanations or comments.",
    generations=[
        ModelGenerationConfig(
            platform="Ollama",
            model="eurollm8192:latest",
            sample_amount=10,
            temperatures=[0.0, 0.5, 1.0],
            timeout=60,
            prompt_variants=prompt_engineering_techniques,
        ),
        ModelGenerationConfig(
            platform="Ollama",
            model="mistral8192:latest",
            sample_amount=10,
            temperatures=[0.0, 0.5, 1.0],
            timeout=60,
            prompt_variants=prompt_engineering_techniques,
        ),
        ModelGenerationConfig(
            platform="Ollama",
            model="deepseek-r1_8192:latest",
            sample_amount=10,
            temperatures=[0.0, 0.5, 1.0],
            timeout=180,
            prompt_variants=prompt_engineering_techniques,
        ),
    ],
)
