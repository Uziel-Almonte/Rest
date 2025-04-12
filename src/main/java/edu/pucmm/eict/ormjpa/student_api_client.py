import requests
import json

BASE_URL = "http://localhost:7000/api/estudiante"

def list_students():
    """Lists all students."""
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        print("--- All Students ---")
        students = response.json()
        if students:
            for student in students:
                print(f"  Matricula: {student.get('matricula')}, Nombre: {student.get('nombre')}")
        else:
            print("  No students found.")
        print("-" * 20)
        return students
    except requests.exceptions.RequestException as e:
        print(f"Error listing students: {e}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON response: {response.text}")
        return None

def get_student(matricula):
    """Gets a specific student by matricula."""
    try:
        url = f"{BASE_URL}/{matricula}"
        response = requests.get(url)
        response.raise_for_status()
        student = response.json()
        print(f"--- Student {matricula} ---")
        if student:
             print(f"  Matricula: {student.get('matricula')}, Nombre: {student.get('nombre')}")
        else: # Should be caught by raise_for_status, but good practice
             print(f"  Student with matricula {matricula} not found.")
        print("-" * 20)
        return student
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Student with matricula {matricula} not found.")
        else:
            print(f"Error getting student {matricula}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error getting student {matricula}: {e}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON response: {response.text}")
        return None


def create_student(matricula, nombre):
    """Creates a new student."""
    try:
        student_data = {
            "matricula": matricula,
            "nombre": nombre
            # Add other fields like fechaNacimiento if needed by the API
            # "fechaNacimiento": "YYYY-MM-DD"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(BASE_URL, json=student_data, headers=headers)
        response.raise_for_status()
        created_student = response.json()
        print(f"--- Student Created ---")
        print(f"  Matricula: {created_student.get('matricula')}, Nombre: {created_student.get('nombre')}")
        print("-" * 20)
        return created_student
    except requests.exceptions.RequestException as e:
        print(f"Error creating student: {e}")
        # Potentially print response text for more details
        # if e.response is not None:
        #     print(f"Response: {e.response.text}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON response: {response.text}")
        return None

def delete_student(matricula):
    """Deletes a student by matricula."""
    try:
        url = f"{BASE_URL}/{matricula}"
        response = requests.delete(url)
        response.raise_for_status()
        # API returns true/false according to OpenAPI spec
        if response.status_code == 200 and response.json() == True:
             print(f"--- Student {matricula} Deleted Successfully ---")
             return True
        else:
             # This path will now be taken when deleting a non-existent student
             print(f"--- Failed to Delete Student {matricula} (API returned false or unexpected status) ---")
             return False
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Student with matricula {matricula} not found for deletion.")
        else:
            print(f"Error deleting student {matricula}: {e}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error deleting student {matricula}: {e}")
        return False
    except json.JSONDecodeError:
        print(f"Error decoding JSON response: {response.text}")
        return False

# --- Example Usage ---
if __name__ == "__main__":
    print("Running Student API Client Demo...")

    # 1. List all students (assuming some exist from the Java app's bootstrap)
    list_students()

    # 2. Create a new student
    new_student_matricula = 99999
    new_student_nombre = "Test Student Python"
    created = create_student(new_student_matricula, new_student_nombre)

    # 3. List all students again to see the new one
    if created:
        list_students()

    # 4. Consult the newly created student
    if created:
        get_student(new_student_matricula)

    # 5. Consult a non-existent student
    get_student(1111111) # Assuming this doesn't exist

    # 6. Delete the created student
    if created:
        delete_student(new_student_matricula)

    # 7. Try deleting again (should fail)
    if created:
        delete_student(new_student_matricula)

    # 8. List all students one last time
    list_students()

    print("Demo finished.")