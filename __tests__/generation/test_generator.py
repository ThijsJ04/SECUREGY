import pytest
from unittest.mock import Mock, patch, mock_open

from generation.generator import Generator
from experiment_configuration import (
    ExperimentConfig,
    ModelGenerationConfig,
    PromptEngineeringTechniqueConfig,
)


class TestGenerator:
    @pytest.fixture
    def sample_experiment_config(self):
        return ExperimentConfig(
            system_prompt="You are a helpful coding assistant.",
            rci_follow_up_system_prompt="Please improve the code.",
            generations=[
                ModelGenerationConfig(
                    platform="Ollama",
                    model="llama3:8b",
                    temperatures=[0.0, 0.5],
                    timeout=60,
                    sample_amount=2,
                    prompt_variants=[
                        PromptEngineeringTechniqueConfig(
                            id="base", prefix="", suffix=""
                        ),
                        PromptEngineeringTechniqueConfig(id="cot", COT=True),
                        PromptEngineeringTechniqueConfig(
                            id="rci",
                            RCI={"total_iterations": 1, "variant": "security"},
                        ),
                    ],
                )
            ],
        )

    @pytest.fixture
    def sample_prompts(self):
        return [
            {"id": "prompt1", "prompt": "Write a function to sort a list"},
            {"id": "prompt2", "prompt": "Create a secure password validator"},
        ]

    def test_apply_PET_to_system_prompt(self, sample_experiment_config):
        """Test that PET is applied correctly to the system prompt."""

        generator = Generator(sample_experiment_config)

        original_prompt = "You are a helpful assistant."
        pet_config = PromptEngineeringTechniqueConfig(
            id="important", prefix="IMPORTANT: ", suffix=""
        )

        result = generator._Generator__apply_PET_to_system_prompt(
            original_prompt, pet_config
        )
        assert result == "IMPORTANT: You are a helpful assistant."

    @patch("builtins.print")
    def test_compute_generation_statistics(self, mock_print, sample_experiment_config):
        """Test that generation statistics are computed correctly."""

        generator = Generator(sample_experiment_config)

        result = generator._Generator__compute_generation_statistics(
            number_of_prompts=2
        )

        # Expected calculation: 2 temperatures * 3 variants * 2 prompts * 2 samples = 24
        expected_total = 24
        assert result == expected_total

        print_calls = [call.args[0] for call in mock_print.call_args_list]
        assert any("Total Programs Required    : 24" in call for call in print_calls)
        assert any("Maximum Generation Time   :" in call for call in print_calls)

    @patch("generation.generator.get_backend_handler_by_name")
    @patch("builtins.open", new_callable=mock_open)
    def test_generate_baseline_variant(
        self,
        mock_file,
        mock_get_handler,
        sample_experiment_config,
        sample_prompts,
    ):
        """Test generation with baseline variant only."""

        # Modify config to have only baseline variant
        config = sample_experiment_config.copy()
        config.generations[0].prompt_variants = [
            PromptEngineeringTechniqueConfig(id="baseline")
        ]
        config.generations[0].temperatures = [0.5]
        config.generations[0].sample_amount = 1

        mock_handler = Mock()
        mock_handler.request.return_value = "def sort_list(lst): return sorted(lst)"
        mock_get_handler.return_value = mock_handler

        generator = Generator(config)
        generator.generate(sample_prompts)

        # Verify handler was created correctly
        mock_get_handler.assert_called_with(
            platform="Ollama",
            model="llama3:8b",
            system_prompt="You are a helpful coding assistant.",
            rci_follow_up_system_prompt="Please improve the code.",
            temperature=0.5,
            timeout=60,
        )

        # Verify request was called for each prompt
        assert mock_handler.request.call_count == 2

        # Verify files were written
        assert mock_file.call_count == 2

    @patch("generation.generator.get_backend_handler_by_name")
    @patch("pathlib.Path.mkdir")
    @patch("builtins.open", new_callable=mock_open)
    def test_generate_cot_variant(
        self,
        mock_file,
        mock_mkdir,
        mock_get_handler,
        sample_experiment_config,
        sample_prompts,
    ):
        """Test generation with COT variant only."""

        # Modify config to have only COT variant
        config = sample_experiment_config.copy()
        config.generations[0].prompt_variants = [
            PromptEngineeringTechniqueConfig(id="cot", COT=True)
        ]
        config.generations[0].temperatures = [0.5]
        config.generations[0].sample_amount = 1

        mock_handler = Mock()
        mock_handler.request.return_value = "def sort_list(lst): return sorted(lst)"
        mock_get_handler.return_value = mock_handler

        generator = Generator(config)
        generator.generate(sample_prompts)

        # Verify COT prompt modification
        expected_calls = [
            "Q: Write a function to sort a list\n\nA: Let's think step by step.",
            "Q: Create a secure password validator\n\nA: Let's think step by step.",
        ]
        actual_calls = [call.args[0] for call in mock_handler.request.call_args_list]
        assert actual_calls == expected_calls

    @patch("generation.generator.get_backend_handler_by_name")
    @patch("pathlib.Path.mkdir")
    @patch("builtins.open", new_callable=mock_open)
    def test_generate_rci_variant(
        self,
        mock_file,
        mock_mkdir,
        mock_get_handler,
        sample_experiment_config,
        sample_prompts,
    ):
        """Test generation with RCI variant only."""

        # Modify config to have only RCI variant
        config = sample_experiment_config.copy()
        config.generations[0].prompt_variants = [
            PromptEngineeringTechniqueConfig(
                id="rci", RCI={"total_iterations": 2, "variant": "security"}
            )
        ]
        config.generations[0].temperatures = [0.5]
        config.generations[0].sample_amount = 1

        mock_handler = Mock()
        mock_handler.rci_request.return_value = (
            "def secure_sort(lst): return sorted(lst)"
        )
        mock_get_handler.return_value = mock_handler

        generator = Generator(config)
        generator.generate(sample_prompts)

        # Verify RCI request was called
        assert mock_handler.rci_request.call_count == 2

        # Verify RCI parameters
        expected_calls = [
            (2, "security", "Write a function to sort a list"),
            (2, "security", "Create a secure password validator"),
        ]
        actual_calls = [call.args for call in mock_handler.rci_request.call_args_list]
        assert actual_calls == expected_calls

    @patch("generation.generator.get_backend_handler_by_name")
    @patch("pathlib.Path.mkdir")
    @patch("builtins.open", new_callable=mock_open)
    def test_generate_output_path_structure(
        self,
        mock_file,
        mock_mkdir,
        mock_get_handler,
        sample_experiment_config,
        sample_prompts,
    ):
        """Test that output file paths are structured correctly."""

        # Modify config to have only baseline variant
        config = sample_experiment_config.copy()
        config.generations[0].prompt_variants = [
            PromptEngineeringTechniqueConfig(id="baseline")
        ]
        config.generations[0].temperatures = [0.5]
        config.generations[0].sample_amount = 1

        mock_handler = Mock()
        mock_handler.request.return_value = "def sort_list(lst): return sorted(lst)"
        mock_get_handler.return_value = mock_handler

        generator = Generator(config)
        generator.generate(sample_prompts)

        # Verify file paths
        file_calls = mock_file.call_args_list
        assert len(file_calls) == 2

        # Check path structure contains expected components
        for call in file_calls:
            file_path = str(call.args[0])
            assert "Ollama" in file_path
            assert "llama3" in file_path  # model name without version
            assert "T0.5" in file_path
            assert "baseline" in file_path
            assert "R0" in file_path
            assert ".py" in file_path
