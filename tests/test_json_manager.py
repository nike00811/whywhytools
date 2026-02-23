import pytest
from pathlib import Path
import json
from whywhytools.json_manager import read_json, write_json

def test_write_and_read_json(tmp_path: Path):
    test_file = tmp_path / "test.json"
    data = {"name": "test", "value": 123}
    
    # Test write_json
    write_json(data, test_file, silent=True)
    assert test_file.exists()
    
    with open(test_file, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    assert loaded_data == data
    
    # Test read_json
    read_data = read_json(test_file)
    assert read_data == data

def test_write_json_force(tmp_path: Path, capsys):
    test_file = tmp_path / "test.json"
    data1 = {"v": 1}
    data2 = {"v": 2}

    write_json(data1, test_file, silent=True)
    
    # Test force=False (default behavior unless explicitly passed)
    write_json(data2, test_file, force=False, silent=True)
    assert read_json(test_file) == data1
    
    # The output should contain "[INFO]" warning about existence
    captured = capsys.readouterr()
    assert "already exists" in captured.out
    
    # Test force=True
    write_json(data2, test_file, force=True, silent=True)
    assert read_json(test_file) == data2

def test_json_manager_type_error(tmp_path: Path):
    test_file = tmp_path / "test.json"
    
    with pytest.raises(TypeError):
        write_json(["not", "a", "dict"], test_file)
        
    with pytest.raises(TypeError):
        read_json(123)
