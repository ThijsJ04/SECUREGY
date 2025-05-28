import os
import ast
import hashlib
from collections import defaultdict
from pathlib import Path
import re
import pandas as pd


def get_file_hash(file_path):
    """Calculate SHA-256 hash of file content."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return hashlib.sha256(content.encode("utf-8")).hexdigest()
    except Exception:
        return None


def is_compilable(file_path):
    """Check if a Python file is syntactically correct using AST."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        ast.parse(content)
        return True
    except Exception:
        return False


def parse_directory_structure(root_path):
    """
    Parse the directory structure and extract information.
    Expected structure: {relative root}/generated_code/{dataset}/{model name}/{prompt variant}/{model name}_{temperature}_{technique}_R{index}/{prompt ID}.py
    """
    root_path = Path(root_path)
    results = []

    # Find all .py files in the structure
    for py_file in root_path.rglob("*.py"):
        parts = py_file.parts

        # Find the index of 'generated_code' in the path
        try:
            gen_code_idx = parts.index("generated_code")
        except ValueError:
            continue  # Skip files not in generated_code structure

        # Check if we have enough parts after generated_code
        if len(parts) < gen_code_idx + 6:
            continue

        dataset = parts[gen_code_idx + 1]
        model_name = parts[gen_code_idx + 2]
        prompt_variant = parts[gen_code_idx + 3]
        run_folder = parts[gen_code_idx + 4]
        prompt_id = py_file.stem  # filename without .py extension

        # Parse run folder to extract temperature and index
        # Expected format: {model name}_{temperature}_{technique}_R{index}
        run_pattern = r"^(.+?)_([0-9.]+)_(.+?)_R(\d+)$"
        match = re.match(run_pattern, run_folder)

        if not match:
            continue

        run_model_name, temperature, technique, index = match.groups()
        temperature = float(temperature)
        index = int(index)

        # Verify model name consistency
        if run_model_name != model_name:
            continue

        file_hash = get_file_hash(py_file)
        is_comp = is_compilable(py_file) if file_hash else False

        results.append(
            {
                "model_name": model_name,
                "prompt_variant": prompt_variant,
                "temperature": temperature,
                "technique": technique,
                "index": index,
                "prompt_id": prompt_id,
                "file_path": str(py_file),
                "file_hash": file_hash,
                "is_compilable": is_comp,
            }
        )

    return results


def analyze_files(file_data):
    """Analyze the file data and compute metrics for each group."""
    # Group by (model_name, prompt_variant, temperature)
    groups = defaultdict(list)

    for file_info in file_data:
        key = (
            file_info["model_name"],
            file_info["prompt_variant"],
            file_info["temperature"],
        )
        groups[key].append(file_info)

    results = []

    for (model_name, prompt_variant, temperature), files in groups.items():
        # Total generations
        total_generations = len(files)

        # Calculate unique files
        # Group by prompt_id to find duplicates across indices
        prompt_groups = defaultdict(list)
        for file_info in files:
            if file_info["file_hash"]:  # Only consider files we could read
                prompt_groups[file_info["prompt_id"]].append(file_info)

        unique_files = []
        for prompt_id, prompt_files in prompt_groups.items():
            # Get unique hashes for this prompt_id
            hash_to_file = {}
            for file_info in prompt_files:
                file_hash = file_info["file_hash"]
                if file_hash not in hash_to_file:
                    hash_to_file[file_hash] = file_info

            # Add unique files to our list
            unique_files.extend(hash_to_file.values())

        total_unique = len(unique_files)

        # Calculate compilable files from unique files
        compilable_files = [f for f in unique_files if f["is_compilable"]]
        total_compilable = len(compilable_files)

        # Calculate max k (minimum indices available across all compilable files)
        if compilable_files:
            # Group compilable files by prompt_id
            compilable_by_prompt = defaultdict(set)
            for file_info in compilable_files:
                compilable_by_prompt[file_info["prompt_id"]].add(file_info["index"])

            # Find the minimum number of indices available for any prompt_id
            if compilable_by_prompt:
                max_k = min(len(indices) for indices in compilable_by_prompt.values())
            else:
                max_k = 0
        else:
            max_k = 0

        results.append(
            {
                "model_name": model_name,
                "prompt_variant": prompt_variant,
                "temperature": temperature,
                "total_generations": total_generations,
                "total_unique": total_unique,
                "total_compilable": total_compilable,
                "max_k": max_k,
            }
        )

    return results


def create_and_export_table(results, output_file="analysis_results.csv"):
    """Create a pandas DataFrame and export to CSV."""
    if not results:
        print("No data found.")
        return None

    # Create DataFrame
    df = pd.DataFrame(results)

    # Sort by model name, prompt variant, and temperature for consistent output
    df = df.sort_values(["model_name", "prompt_variant", "temperature"]).reset_index(
        drop=True
    )

    # Reorder columns to match the desired table format
    column_order = [
        "model_name",
        "prompt_variant",
        "temperature",
        "total_generations",
        "total_unique",
        "total_compilable",
        "max_k",
    ]
    df = df[column_order]

    # Export to CSV
    df.to_csv(output_file, index=False)
    print(f"Results exported to: {output_file}")

    return df


def main(root_path, output_file="analysis_results.csv"):
    """Main function to analyze the file tree and generate the table."""
    print(f"Analyzing directory structure at: {root_path}")

    # Parse directory structure
    file_data = parse_directory_structure(root_path)

    if not file_data:
        print("No Python files found in the expected directory structure.")
        return

    print(f"Found {len(file_data)} Python files.")

    # Analyze files and compute metrics
    results = analyze_files(file_data)

    # Print results table
    df = create_and_export_table(results, output_file)

    return df


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python script.py <root_path> [output_file.csv]")
        print("Example: python script.py /path/to/your/root/directory")
        print("Example: python script.py /path/to/your/root/directory my_results.csv")
        sys.exit(1)

    root_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) == 3 else "analysis_results.csv"

    if not os.path.exists(root_path):
        print(f"Error: Path '{root_path}' does not exist.")
        sys.exit(1)

    main(root_path, output_file)
