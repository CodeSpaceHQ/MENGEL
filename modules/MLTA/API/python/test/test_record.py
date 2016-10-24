#!/usr/bin/python
import sys
import os
import subprocess
from random import randint
import pytest
sys.path.insert(0, os.path.abspath('..'))
from mlta import record as MLTARecord
from mlta.record import ResultRecord
from mlta.record import Project
from mlta.record import MLTARecordError

@pytest.fixture
def mock_data(**opt_params):
    if ('seed' in opt_params):
        seed = opt_params['seed']
    else:
        seed = randint(0, 9)
    record = {}
    record['name'] = 'testRecord{}'.format(seed)
    record['model_type'] = 'model{}'.format(seed)
    record['label'] = 'label{}'.format(seed)
    model_data = {}
    test_data = {}
    for i in range(seed):
        model_data['modelKey{}'.format(i)] = 'modelValue{}'.format(i)
        test_data['testKey{}'.format(i)] = 'testValue{}'.format(i)

    record['model_data'] = model_data
    record['test_data'] = test_data
    record['seed'] = seed
    record['project'] = 'TestProject'

    return record

def compare_dicts(dict1, dict2):
    assert len(dict1.keys()) == len(dict2.keys())
    for key, val in dict1.items():
        assert val == dict2[key]

def compare_records(record1, record2):
    assert record1.label == record2.label
    assert record1.model_type == record2.model_type
    compare_dicts(record1.model_data, record2.model_data)
    compare_dicts(record1.test_data, record2.test_data)

def createRecordFromData(mock_data):
    record = ResultRecord(mock_data['model_type'])
    assert record.model_data == {}
    assert record.test_data == {}
    record.label = mock_data['label']
    for key, val in mock_data['model_data'].items():
        record.add_model_data_pair(key, val)

    for key, val in mock_data['test_data'].items():
        record.add_test_data_pair(key, val)

    assert len(record.model_data) == mock_data['seed']
    assert len(record.test_data) == mock_data['seed']

    return record


#
# TESTS GO BELOW THIS COMMENT
#

def test_record_create(mock_data):
    record = createRecordFromData(mock_data)
    assert record.model_type == mock_data['model_type']
    assert record.label == mock_data['label']

def test_record_add_data(mock_data):
    record = createRecordFromData(mock_data)

    compare_dicts(mock_data['model_data'], record.model_data)
    compare_dicts(mock_data['test_data'], record.test_data)

def test_project_create():
    project = Project('TestProject')
    assert project.name == 'TestProject'
    assert project.records == []

def test_project_add_records():
    project = Project('TestProject1')
    record_1 = createRecordFromData(mock_data())
    record_2 = createRecordFromData(mock_data())
    project.add_record(record_1)
    project.add_record(record_2)
    compare_records(project.records[0], record_1)
    compare_records(project.records[1], record_2)

def test_project_save_records(monkeypatch):
    project = Project('TestProject2')
    project.add_record(createRecordFromData(mock_data()))
    def mock_call_mlta_record(self, args):
        args.append('-v')
        result = subprocess.check_output(args)
        assert result[0] == '0'
        return result.splitlines()[1]
    monkeypatch.setattr(Project, '_call_mlta_record', mock_call_mlta_record)
    project.save_all_records()

def test_project_call_mlta_record():
    with pytest.raises(MLTARecord.MLTARecordError) as excinfo:
        project = Project('TestProject2')
        result = project._call_mlta_record(["mlta-record", "--version"])

    assert excinfo.type == MLTARecord.MLTARecordError
    assert 'MLTA-Record' in str(excinfo.value.message)

def test_project_get_args():
    project = Project('TestProjectArgs')
    data = mock_data(seed=2)
    record = createRecordFromData(data)
    expected_args = ["mlta-record", "-p", "TestProjectArgs", \
        "-m", "{}".format(data['model_type']), \
        "-d", "modelKey1:modelValue1", \
        "-d", "modelKey0:modelValue0", \
        "-D", "testKey1:testValue1", \
        "-D", "testKey0:testValue0"]

    assert len(expected_args) == 13
    project.add_record(record)
    assert expected_args == project._get_args(record)
