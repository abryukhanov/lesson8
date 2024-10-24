import requests
import pytest

BASE_URL = "https://ru.yougile.com"

def get_headers():
    return {
        "Authorization": "Bearer UyRVA85YVVBheMbOqnY6EpyDwvtBoMZ7vk4PBBN8y9U5n3lWeGYe5wUjyc3GlCZR",
        "Content-Type": "application/json"
    }

def test_create_project():
    url = f"{BASE_URL}/api-v2/projects"
    headers = get_headers()
    payload = {
        "title": "Test Project" 
    }

    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 201, f"Response: {response.text}" 
    json_response = response.json()
    assert "id" in json_response


def test_create_project_without_title():
    url = f"{BASE_URL}/api-v2/projects"
    headers = get_headers()
    payload = {}  

    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 400, f"Response: {response.text}"  
    json_response = response.json()
    assert "message" in json_response

def test_get_projects():
    url = f"{BASE_URL}/api-v2/projects"
    headers = get_headers()

    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Response: {response.text}" 
    json_response = response.json()
    assert isinstance(json_response.get('content'), list), f"Expected list, got: {type(json_response.get('content'))}"

def test_update_project():
    project_id = "41f9984f-06a3-4a10-a11f-7f35603b0bdd"
    url = f"{BASE_URL}/api-v2/projects/{project_id}"
    headers = get_headers()
    payload = {
        "title": "Updated Project Name" 
    }

    response = requests.put(url, headers=headers, json=payload)
    assert response.status_code == 200, f"Response: {response.text}" 
    json_response = response.json()
   

def test_update_project_without_title():
    project_id = "41f9984f-06a3-4a10-a11f-7f35603b0bdd"
    url = f"{BASE_URL}/api-v2/projects/{project_id}"
    headers = get_headers()
    payload = {
        "title": ""  
    }

    response = requests.put(url, headers=headers, json=payload)
    assert response.status_code == 400, f"Response: {response.text}" 
    json_response = response.json()
    assert "message" in json_response


def test_get_project_by_id():
    project_id = "41f9984f-06a3-4a10-a11f-7f35603b0bdd"
    url = f"{BASE_URL}/api-v2/projects/{project_id}"
    headers = get_headers()

    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Response: {response.text}" 
    json_response = response.json()
    assert "title" in json_response, "Title is missing from the response."