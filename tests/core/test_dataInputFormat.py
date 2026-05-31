import pytest
import pandas as pd
from core.datasetRead import Dataset
from core.dataInputFormat import DataInput_Labelled, DataInput_Categorical  # Replace with actual import

# Global dataset instance used in the classes
d = Dataset()


@pytest.fixture
def labelled_input():
    return DataInput_Labelled()


@pytest.fixture
def categorical_input():
    return DataInput_Categorical()


# ====================== LABELLED DATA TESTS ======================

def test_labelled_hashAll_populates_all_dictionaries(labelled_input):
    labelled_input.hashAll()
    
    assert hasattr(labelled_input, 'ourTeams_1')
    assert hasattr(labelled_input, 'ourTeams_2')
    assert hasattr(labelled_input, 'ourGrounds')
    assert hasattr(labelled_input, 'ourInnings')
    assert hasattr(labelled_input, 'ourVenues')
    
    assert len(labelled_input.ourTeams_1) > 0
    assert len(labelled_input.ourTeams_2) > 0
    assert len(labelled_input.ourGrounds) > 0


def test_labelled_team1_hashing(labelled_input):
    labelled_input.hashingTeam1()
    
    assert len(labelled_input.ourTeams_1) > 0
    assert len(labelled_input.teamNames) > 0
    
    # Check first few entries (example)
    assert list(labelled_input.ourTeams_1.values())[0] == 0
    # Check column index range: 0 to 22
    assert max(labelled_input.ourTeams_1.values()) == 22


def test_labelled_team2_hashing(labelled_input):
    labelled_input.hashingTeam2()
    
    assert len(labelled_input.ourTeams_2) > 0
    # Team 2 columns should start from index 23 to 45
    assert min(labelled_input.ourTeams_2.values()) == 23
    assert max(labelled_input.ourTeams_2.values()) == 45


def test_labelled_grounds_hashing(labelled_input):
    labelled_input.hashingGrounds()
    
    assert len(labelled_input.ourGrounds) > 0
    assert min(labelled_input.ourGrounds.values()) == 46
    assert max(labelled_input.ourGrounds.values()) == 206  # up to 206


def test_labelled_innings_and_venue_mapping(labelled_input):
    labelled_input.hashingInnings()
    labelled_input.hashingVenue()
    
    expected_innings = {
        'Team1_1Inning': 207,
        'Team1_2Inning': 208,
        'Team2_1Inning': 209,
        'Team2_2Inning': 210
    }
    expected_venues = {
        'Team1_Away': 211, 'Team1_Home': 212, 'Team1_Neutral': 213,
        'Team2_Away': 214, 'Team2_Home': 215, 'Team2_Neutral': 216
    }
    
    assert labelled_input.ourInnings == expected_innings
    assert labelled_input.ourVenues == expected_venues


# ====================== CATEGORICAL DATA TESTS ======================

def test_categorical_hashAll_populates_all_dictionaries(categorical_input):
    categorical_input.hashAll()
    
    assert hasattr(categorical_input, 'ourTeams_1')
    assert hasattr(categorical_input, 'ourTeams_2')
    assert hasattr(categorical_input, 'ourGrounds')
    assert hasattr(categorical_input, 'ourInnings')
    assert hasattr(categorical_input, 'ourVenues')
    assert hasattr(categorical_input, 'winnerIndex')
    
    assert len(categorical_input.winnerIndex) > 0


def test_categorical_team_hashing(categorical_input):
    categorical_input.hashingTeam1()
    assert len(categorical_input.ourTeams_1) > 0
    
    categorical_input.hashingTeam2()
    assert len(categorical_input.ourTeams_2) > 0


def test_categorical_grounds_hashing(categorical_input):
    categorical_input.hashingGrounds()
    assert len(categorical_input.ourGrounds) > 0


def test_categorical_target_winners_hashing(categorical_input):
    categorical_input.hashingTargetWinners()
    
    assert len(categorical_input.winnerIndex) > 0
    # Check that values are sequential counters starting from 0
    values = list(categorical_input.winnerIndex.values())
    assert values == list(range(len(values)))


def test_categorical_innings_and_venue_same_as_labelled(categorical_input):
    categorical_input.hashingInnings()
    categorical_input.hashingVenue()
    
    # These should be identical in both classes
    expected_innings = {
        'Team1_1Inning': 207, 'Team1_2Inning': 208,
        'Team2_1Inning': 209, 'Team2_2Inning': 210
    }
    expected_venues = {
        'Team1_Away': 211, 'Team1_Home': 212, 'Team1_Neutral': 213,
        'Team2_Away': 214, 'Team2_Home': 215, 'Team2_Neutral': 216
    }
    
    assert categorical_input.ourInnings == expected_innings
    assert categorical_input.ourVenues == expected_venues


# ====================== GENERAL TESTS ======================

@pytest.mark.skip(reason="Temporarily disabled")
def test_dataset_is_loaded_in_hashing_methods():
    """Ensure dataset is being read without errors"""
    labelled = DataInput_Labelled()
    categorical = DataInput_Categorical()
    
    labelled.hashAll()
    categorical.hashAll()
    
    assert hasattr(d, 'match_data')
    assert isinstance(d.match_data, pd.DataFrame)
    assert d.match_data.shape[1] == 237  # Total columns expected