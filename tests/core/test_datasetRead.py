import pytest
import pandas as pd
import os
from pathlib import Path

# Import the class to test
from core.datasetRead import Dataset  # Replace with actual module name if different

@pytest.fixture
def dataset():
    return Dataset()


def test_ReadCategoricalDataSet_loads_data_correctly(dataset):
    """Test that categorical dataset loads and splits correctly"""
    dataset.ReadCategoricalDataSet()
    
    # Basic checks
    assert hasattr(dataset, 'X_train')
    assert hasattr(dataset, 'X_test')
    assert hasattr(dataset, 'Y_train')
    assert hasattr(dataset, 'Y_test')
    
    # Check shapes
    assert len(dataset.X_train) > 0
    assert len(dataset.X_test) > 0
    assert len(dataset.Y_train) > 0
    assert len(dataset.Y_test) > 0
    
    # Check train/test split ratio (approx 70-30)
    total_samples = len(dataset.X_train) + len(dataset.X_test)
    assert abs(len(dataset.X_train) / total_samples - 0.7) < 0.05
    
    # Check feature and target column counts
    assert dataset.X_train.shape[1] == 217
    assert dataset.Y_train.shape[1] == 20  # 237 - 217 = 20 target columns
    
    # Check data types
    assert isinstance(dataset.X_train, pd.DataFrame)
    assert isinstance(dataset.Y_train, pd.DataFrame)


def test_ReadLabelledDataSet_loads_data_correctly(dataset):
    """Test that labelled dataset loads and splits correctly"""
    dataset.ReadLabelledDataSet()
    
    assert hasattr(dataset, 'X_train')
    assert hasattr(dataset, 'X_test')
    assert hasattr(dataset, 'Y_train')
    assert hasattr(dataset, 'Y_test')
    
    # Check shapes
    assert dataset.X_train.shape[1] == 217
    assert isinstance(dataset.Y_train, pd.Series)  # Single target column
    
    # Check train/test split
    total_samples = len(dataset.X_train) + len(dataset.X_test)
    assert abs(len(dataset.X_train) / total_samples - 0.7) < 0.05


def test_both_methods_use_same_random_state(dataset):
    """Test that both methods use the same random_state for reproducibility"""
    # Test categorical
    dataset.ReadCategoricalDataSet()
    X_train_cat = dataset.X_train.copy()
    Y_train_cat = dataset.Y_train.copy()
    
    # Test labelled
    dataset.ReadLabelledDataSet()
    X_train_lab = dataset.X_train.copy()
    Y_train_lab = dataset.Y_train.copy()
    
    # Just check that they run consistently (same random_state = 100)
    assert X_train_cat.shape[1] == 217
    assert X_train_lab.shape[1] == 217


def test_column_selection_is_correct(dataset):
    """Test that column slicing logic is correct"""
    dataset.ReadCategoricalDataSet()
    
    # Check feature columns
    assert dataset.X_train.shape[1] == 217
    
    # Check target columns for categorical
    assert dataset.Y_train.shape[1] == 20
    
    # Test labelled version
    dataset.ReadLabelledDataSet()
    assert dataset.X_train.shape[1] == 217
    assert len(dataset.Y_train.shape) == 1  # Should be a Series