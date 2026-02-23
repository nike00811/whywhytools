import pytest
from pathlib import Path
from whywhytools.jsonl_manager import read_jsonl, write_jsonl, append_jsonl

def test_write_and_read_jsonl(tmp_path: Path):
    test_file = tmp_path / "test.jsonl"
    data = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
    
    # Write list of dicts
    write_jsonl(data, test_file, silent=True)
    assert test_file.exists()
    
    # Read and verify
    loaded_data = read_jsonl(test_file)
    assert loaded_data == data

def test_write_jsonl_dict_and_force(tmp_path: Path, capsys):
    test_file = tmp_path / "test.jsonl"
    single_data = {"id": 1, "name": "A"}
    
    # Write single dict
    write_jsonl(single_data, test_file, silent=True)
    assert read_jsonl(test_file) == [single_data]
    
    new_data = {"id": 2, "name": "B"}
    # Force=False should not overwrite
    write_jsonl(new_data, test_file, force=False, silent=True)
    assert read_jsonl(test_file) == [single_data]
    
    captured = capsys.readouterr()
    assert "already exists" in captured.out
    
    # Force=True should overwrite
    write_jsonl(new_data, test_file, force=True, silent=True)
    assert read_jsonl(test_file) == [new_data]

def test_append_jsonl(tmp_path: Path):
    test_file = tmp_path / "test.jsonl"
    data1 = {"id": 1}
    data2 = [{"id": 2}, {"id": 3}]
    
    # Append to non-existent creates it
    append_jsonl(data1, test_file)
    assert read_jsonl(test_file) == [data1]
    
    # Append multiple
    append_jsonl(data2, test_file)
    assert read_jsonl(test_file) == [data1, data2[0], data2[1]]

def test_jsonl_manager_type_error(tmp_path: Path):
    test_file = tmp_path / "test.jsonl"
    
    with pytest.raises(TypeError):
        write_jsonl([1, 2, 3], test_file) # List elements must be dicts
        
    with pytest.raises(TypeError):
        read_jsonl(123)
