import pytest
import os
import pickle
import pandas as pd

# Add parent directory to path
import sys
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(PARENT_DIR)

# Define the path to your data folder dynamically
DATA_DIR = os.path.join(PARENT_DIR, "src", "core", "data")

from core.Classifier import ourSVMClassifier, ourMLPClassifier, ourDTClassifier
from core.datasetRead import Dataset


@pytest.fixture(scope="module")
def dataset():
    return Dataset()

@pytest.fixture(scope="module")
def svm_clf():
    return ourSVMClassifier()

@pytest.fixture(scope="module")
def mlp_clf():
    return ourMLPClassifier()

@pytest.fixture(scope="module")
def dt_clf():
    return ourDTClassifier()


# ====================== COMMON TESTS ======================

def test_all_classifiers_can_be_instantiated():
    assert ourSVMClassifier() is not None
    assert ourMLPClassifier() is not None
    assert ourDTClassifier() is not None


# ====================== SVM CLASSIFIER TESTS ======================

def test_svm_train_model(svm_clf, dataset):
    svm_clf.trainModel()
    assert hasattr(svm_clf, 'TrainedSVMclf')
    assert svm_clf.TrainedSVMclf is not None

def test_svm_accuracy_check(svm_clf):
    svm_clf.trainModel()        # Ensure model is trained
    svm_clf.accuracyCheck()     # This will print, but we mainly check it doesn't crash

def test_svm_dump_and_load_pickle(svm_clf):
    svm_clf.trainModel()
    svm_clf.dumpPickle()
    
    pickle_path = os.path.join(DATA_DIR, "svm_classifier.pkl")
    assert os.path.exists(pickle_path), "SVM pickle file was not created"
    
    # Test loading
    svm_clf.loadPickle()
    assert hasattr(svm_clf, 'SVMclf')
    assert svm_clf.SVMclf is not None

def test_svm_run_model(svm_clf):
    svm_clf.trainModel()
    svm_clf.loadPickle()  # Need loaded model for runModel
    
    # Create a sample input (should match feature dimension = 217)
    sample_input = [0] * 217
    
    result = svm_clf.runModel(sample_input, "India", "England")
    assert result is not None
    assert isinstance(result, (int, str))


# ====================== MLP CLASSIFIER TESTS ======================

def test_mlp_train_model(mlp_clf):
    mlp_clf.trainModel()
    assert hasattr(mlp_clf, 'TrainedMLPclf')
    assert mlp_clf.TrainedMLPclf is not None

def test_mlp_accuracy_check(mlp_clf):
    mlp_clf.trainModel()
    mlp_clf.accuracyCheck()

def test_mlp_dump_and_load_pickle(mlp_clf):
    mlp_clf.trainModel()
    mlp_clf.dumpPickle()
    
    pickle_path = os.path.join(DATA_DIR, "mlp_classifier.pkl")
    assert os.path.exists(pickle_path), "MLP pickle file was not created"
    
    mlp_clf.loadPickle()
    assert hasattr(mlp_clf, 'MLPclf')

def test_mlp_run_model(mlp_clf):
    mlp_clf.trainModel()
    mlp_clf.loadPickle()
    
    sample_input = [0] * 217
    result = mlp_clf.runModel(sample_input, "India", "Pakistan")   # Use actual team names from your data
    
    assert result is not None
    assert result in ["India", "Pakistan"] or "Can't Predict" in str(result)


# ====================== DT CLASSIFIER TESTS ======================

def test_dt_train_model(dt_clf):
    dt_clf.trainModel()
    assert hasattr(dt_clf, 'TrainedDTclf')

def test_dt_accuracy_check(dt_clf):
    dt_clf.trainModel()
    dt_clf.accuracyCheck()

def test_dt_dump_and_load_pickle(dt_clf):
    dt_clf.trainModel()
    dt_clf.dumpPickle()

    pickle_path = os.path.join(DATA_DIR, "dt_classifier.pkl")
    assert os.path.exists(pickle_path), "DT pickle file was not created"
    
    dt_clf.loadPickle()
    assert hasattr(dt_clf, 'DTclf')

def test_dt_run_model(dt_clf):
    dt_clf.trainModel()
    dt_clf.loadPickle()
    
    sample_input = [0] * 217
    result = dt_clf.runModel(sample_input, "Australia", "India")
    
    assert result is not None


# ====================== INTEGRATION & EDGE CASE TESTS ======================

def test_pickle_files_exist_after_training():
    """Check all three models create their pickle files"""
    files = [
        DATA_DIR + "/svm_classifier.pkl",
        DATA_DIR + "/mlp_classifier.pkl",
        DATA_DIR + "/dt_classifier.pkl"
    ]
    for f in files:
        assert os.path.exists(f), f"Missing pickle file: {f}"

def test_all_models_have_required_methods():
    for clf_class in [ourSVMClassifier, ourMLPClassifier, ourDTClassifier]:
        clf = clf_class()
        assert hasattr(clf, 'trainModel')
        assert hasattr(clf, 'accuracyCheck')
        assert hasattr(clf, 'dumpPickle')
        assert hasattr(clf, 'loadPickle')
        assert hasattr(clf, 'runModel')