import pytest
import os
import pickle
from pathlib import Path

# Add src to path (same as your script)
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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

@pytest.mark.skip(reason="Temporarily disabled")
def test_svm_model_training_and_pickling(models):
    """Test SVM model training and pickling"""
    svm = models['SVM']
    
    svm.trainModel()
    svm.accuracyCheck()
    svm.dumpPickle()
    
    # Check if pickle file was created
    pickle_path = Path("SVM_model.pkl")  # Adjust if your dumpPickle uses different name/path
    assert pickle_path.exists(), f"Pickle file not found: {pickle_path}"
    
    # Verify pickle can be loaded
    with open(pickle_path, 'rb') as f:
        loaded_model = pickle.load(f)
    assert loaded_model is not None

@pytest.mark.skip(reason="Temporarily disabled")
def test_mlp_model_training_and_pickling(models):
    """Test MLP model training and pickling"""
    mlp = models['MLP']
    
    mlp.trainModel()
    mlp.accuracyCheck()
    mlp.dumpPickle()
    
    pickle_path = Path("MLP_model.pkl")   # Adjust filename if different
    assert pickle_path.exists(), f"Pickle file not found: {pickle_path}"

@pytest.mark.skip(reason="Temporarily disabled")
def test_dt_model_training_and_pickling(models):
    """Test Decision Tree model training and pickling"""
    dt = models['DT']
    
    dt.trainModel()
    dt.accuracyCheck()
    dt.dumpPickle()
    
    pickle_path = Path("DT_model.pkl")    # Adjust filename if different
    assert pickle_path.exists(), f"Pickle file not found: {pickle_path}"


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

@pytest.mark.skip(reason="Temporarily disabled")
def test_pickle_files_are_created():
    """Verify all three pickle files exist after training"""
    expected_files = ["SVM_model.pkl", "MLP_model.pkl", "DT_model.pkl"]
    
    for file in expected_files:
        path = Path(file)
        assert path.exists(), f"Expected pickle file missing: {file}"


# Optional: Cleanup after tests (if you want to keep workspace clean)
@pytest.fixture(scope="session", autouse=True)
def cleanup_pickles(request):
    def remove_pickles():
        for file in ["SVM_model.pkl", "MLP_model.pkl", "DT_model.pkl"]:
            try:
                Path(file).unlink(missing_ok=True)
            except:
                pass
    request.addfinalizer(remove_pickles)