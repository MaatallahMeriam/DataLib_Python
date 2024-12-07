import os
import pytest
from src.datalib.data_processing import load_csv, save_csv, normalize_column

def test_load_csv():
    # Construct the dynamic file path
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'test_file.csv')
    
    # Skip the test if the file does not exist
    if not os.path.exists(file_path):
        pytest.skip(f"Required file {file_path} not found")

    # Test the load_csv function
    data = load_csv(file_path)
    assert data is not None
    assert len(data) > 0  # Add more meaningful assertions as needed

def test_save_csv():
    input_file = os.path.join(os.path.dirname(__file__), 'data', 'test_file.csv')
    output_file = os.path.join(os.path.dirname(__file__), 'data', 'output_file.csv')

    # Skip the test if the input file does not exist
    if not os.path.exists(input_file):
        pytest.skip(f"Required file {input_file} not found")

    # Test the save_csv function
    data = load_csv(input_file)
    save_csv(data, output_file)
    assert os.path.exists(output_file)  # Check if the output file was created
    os.remove(output_file)  # Clean up the test artifact
def test_normalize_column():
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'test_file.csv')

    if not os.path.exists(file_path):
        pytest.skip(f"Required file {file_path} not found")

    data = load_csv(file_path)
    normalized_data = normalize_column(data, 'age')

    # Test if the 'age' column has been normalized
    assert normalized_data['age'].max() == 1.0
    assert normalized_data['age'].min() == 0.0
