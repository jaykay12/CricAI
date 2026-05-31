import pytest
import os
import pickle
from pathlib import Path

# Add src to path (same as your script)
import sys
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(PARENT_DIR)

# Define the path to your data folder dynamically
DATA_DIR = os.path.join(PARENT_DIR, "src", "core", "data")

from core.Classifier import ourMLPClassifier, ourDTClassifier, ourSVMClassifier


@pytest.fixture(scope="module")
def models():
    """Fixture to initialize all three models once per test module"""
    SVMClf = ourSVMClassifier()
    MLPClf = ourMLPClassifier()
    DTClf = ourDTClassifier()
    return {
        'SVM': SVMClf,
        'MLP': MLPClf,
        'DT': DTClf
    }


# ====================== BASIC INSTANTIATION TESTS ======================

def test_models_can_be_instantiated():
    """Test that all classifier classes can be instantiated"""
    assert ourSVMClassifier() is not None
    assert ourMLPClassifier() is not None
    assert ourDTClassifier() is not None


# ====================== TRAINING AND PICKLE TESTS ======================

def test_svm_model_training_and_pickling(models):
    """Test SVM model training and pickling"""
    svm = models['SVM']
    
    svm.trainModel()
    svm.accuracyCheck()
    svm.dumpPickle()
    
    # Check if pickle file was created
    pickle_path = os.path.join(DATA_DIR, "svm_classifier.pkl")
    assert os.path.exists(pickle_path), f"SVM pickle file was not created at {pickle_path}"
    
    # Verify pickle can be loaded
    with open(pickle_path, 'rb') as f:
        loaded_model = pickle.load(f)
    assert loaded_model is not None

def test_mlp_model_training_and_pickling(models):
    """Test MLP model training and pickling"""
    mlp = models['MLP']
    
    mlp.trainModel()
    mlp.accuracyCheck()
    mlp.dumpPickle()
    
    pickle_path = os.path.join(DATA_DIR, "mlp_classifier.pkl")
    assert os.path.exists(pickle_path), f"MLP pickle file was not created at {pickle_path}"

def test_dt_model_training_and_pickling(models):
    """Test Decision Tree model training and pickling"""
    dt = models['DT']
    
    dt.trainModel()
    dt.accuracyCheck()
    dt.dumpPickle()
    
    pickle_path = os.path.join(DATA_DIR, "dt_classifier.pkl")
    assert os.path.exists(pickle_path), f"DT pickle file was not created at {pickle_path}"


# ====================== HELPER / INTEGRATION TESTS ======================

def test_all_models_have_required_methods(models):
    """Test that all models implement the expected interface"""
    for name, model in models.items():
        assert hasattr(model, 'trainModel')
        assert hasattr(model, 'accuracyCheck')
        assert hasattr(model, 'dumpPickle')
        assert callable(model.trainModel)
        assert callable(model.accuracyCheck)
        assert callable(model.dumpPickle)

def test_pickle_files_are_created():
    """Verify all three pickle files exist after training"""
    expected_files = ["svm_classifier.pkl", "mlp_classifier.pkl", "dt_classifier.pkl"]
    
    for file in expected_files:
        path = Path(DATA_DIR + "/" + file)
        assert path.exists(), f"Expected pickle file missing: {file}"