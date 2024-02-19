from main import StudentsInMLOps

def test_enrollStudents(count):
    mlops = StudentsInMLOps("Samaha", "20I0424")
    mlops.enrollStudents(3)
    assert mlops.get_total_strength() == 3

def test_dropStudents(count):
    mlops = StudentsInMLOps("", "")
    mlops.enrollStudents(3)
    mlops.dropStudents(2)
    assert mlops.getTotalStrength() == 1    

def test_getClassName():
    mlops = StudentsInMLOps("", "")
    assert mlops.getClassName == "MLOps N" 