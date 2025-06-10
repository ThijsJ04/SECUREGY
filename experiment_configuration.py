from pydantic import BaseModel, Field, model_validator
from typing import Annotated, List, Literal, Optional


class RCIConfig(BaseModel):
    """
    RCIConfig represents the configuration for the RCI (Reinforcement Code Improvement) technique.

    Attributes:
        total_iterations (float): The total number of iterations for the RCI process.
        variant (Literal["security", "energy-efficiency"]): The variant of RCI to be used, either "security" or "energy-efficiency".
    """

    total_iterations: Annotated[int, Field(strict=True, gt=0)]
    variant: Literal["security", "energy-efficiency"]


class PromptEngineeringTechniqueConfig(BaseModel):
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


class ModelGenerationConfig(BaseModel):
    """
    ModelGenerationConfig represents the configuration for generating code using a language model.

    Attributes:
        platform (str): The platform to use for code generation.
        model (str): The model to use for code generation.
        sample_amount (int): The number of samples to generate.
        temperatures (List[float]): The temperatures setting for the model.
        timeout (int): The timeout for the generation request in seconds.
        prompt_variants (List[PromptEngineeringTechniqueConfig]): List of prompt engineering techniques to apply.
    """

    platform: str
    model: str
    sample_amount: int
    temperatures: List[float]
    timeout: int
    prompt_variants: List[PromptEngineeringTechniqueConfig]

    @model_validator(mode="after")
    def validate_base_variant_exists(self):
        base_ids = [
            variant.get("id")
            for variant in self.prompt_variants
            if variant.get("id") == "base"
        ]
        if not base_ids:
            raise ValueError("At least one prompt_variant must have id 'base'")
        return self


class ExperimentConfig(BaseModel):
    """
    ExperimentConfig represents the configuration for an experiment.

    Attributes:
        system_prompt (str): The system prompt to be used in the experiment.
        rci_follow_up_system_prompt (str): The follow-up system prompt for RCI.
        generations (List[ModelGenerationConfig]): List of model generation configurations for the experiment.
    """

    system_prompt: str
    rci_follow_up_system_prompt: str
    generations: List[ModelGenerationConfig]


prompt_engineering_techniques: List[PromptEngineeringTechniqueConfig] = [
    PromptEngineeringTechniqueConfig(
        id="base",
    ),
    PromptEngineeringTechniqueConfig(
        id="persona_secure_prefix",
        prefix="You are a senior security engineer with 20 years of experience writing secure Python code. Your implementations always follow security best practices and are thoroughly vetted for vulnerabilities.\n",
    ),
    PromptEngineeringTechniqueConfig(
        id="persona_energy_efficient_prefix",
        prefix="You are a senior software engineer with 20 years of experience writing energy-efficient Python code. Your implementations always minimize power consumption through optimal algorithms, hardware-aware optimizations, and efficient resource usage.\n",
    ),
    PromptEngineeringTechniqueConfig(
        id="secure_suffix",
        suffix="\n4. Ensure your implementation is secure and free from vulnerabilities.",
    ),
    PromptEngineeringTechniqueConfig(
        id="energy_efficient_suffix",
        suffix="\n4. Implement the function in the most energy efficient way possible.",
    ),
    PromptEngineeringTechniqueConfig(
        id="for_loops_suffix",
        suffix="\n4. Prefer for loops over while loops.",
    ),
    PromptEngineeringTechniqueConfig(
        id="library_functions_suffix",
        suffix="\n4. Use library functions when available.",
    ),
    PromptEngineeringTechniqueConfig(
        id="secure_rci_1",
        rci=RCIConfig(total_iterations=1, variant="security"),
    ),
    PromptEngineeringTechniqueConfig(
        id="energy_efficient_rci_1",
        rci=RCIConfig(total_iterations=1, variant="energy-efficiency"),
    ),
    PromptEngineeringTechniqueConfig(
        id="cot",
        COT=True,
    ),
    PromptEngineeringTechniqueConfig(
        id="cot_secure_rci_1",
        COT=True,
        rci=RCIConfig(total_iterations=1, variant="security"),
    ),
]

experiment_configuration: ExperimentConfig = ExperimentConfig(
    system_prompt="""
Complete one unfinished Python function per input. Follow these rules strictly:

1. Input:
    - Contains one function with docstring but no body
    - May include imports, variables, and other code
2. Requirements:
    - Implement the function exactly as described in its docstring
    - Keep all existing code unchanged
    - You may add helper code if needed
3. Output:
    - Return complete executable Python code
    - Include original code plus your implementation
    - Response must be a single Python code block with no explanations, comments, or additional text.
""",
    rci_follow_up_system_prompt="""
Modify an existing Python function implementation based on given feedback. Follow these rules strictly:

1. Input:
    - Contains Python code
    - Includes specific feedback for improvement
2. Requirements:
    - Address all points in the feedback while changing as little as possible
    - Only modify what's necessary to address the feedback
3. Output:
    - Include original code plus your modifications
    - Response must be a single Python code block with no explanations, comments, or additional text.
""",
    generations=[
        ModelGenerationConfig(
            platform="Ollama",
            model="eurollm_16384:latest",
            sample_amount=10,
            temperatures=[1.0],
            timeout=60,
            prompt_variants=prompt_engineering_techniques,
        ),
        ModelGenerationConfig(
            platform="Ollama",
            model="mistral_16384:latest",
            sample_amount=10,
            temperatures=[0.0, 0.5, 1.0],
            timeout=60,
            prompt_variants=prompt_engineering_techniques,
        ),
        ModelGenerationConfig(
            platform="Ollama",
            model="deepseek-r1_16384:latest",
            sample_amount=10,
            temperatures=[0.0, 0.5, 1.0],
            timeout=180,
            prompt_variants=prompt_engineering_techniques,
        ),
    ],
)
