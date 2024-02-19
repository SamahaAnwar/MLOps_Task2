from main import StudentsInMLOps

def test_enrollStudents():
    mlops = StudentsInMLOps("Samaha", "20I0424")
    mlops.enrollStudents(3)
    assert mlops.getTotalStrength() == 3

def test_dropStudents():
    mlops = StudentsInMLOps("", "")
    mlops.enrollStudents(3)
    mlops.dropStudents(2)
    assert mlops.getTotalStrength() == 1    

def test_getClassName():
    mlops = StudentsInMLOps("", "")
    assert mlops.getClassName == "MLOps N" 