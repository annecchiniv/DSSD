import requests

class BonitaClient:
    def __init__(self, user, password, base_uri):
        self.user = user
        self.password = password
        self.base_uri = base_uri
        self.session = requests.Session()
        self.jsession_id = None
        self.token = None

    def login(self):
        try:
            login_url = f'{self.base_uri}/loginservice'
            payload = {
                'username': self.user,
                'password': self.password,
                'redirect': 'false'
            }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            response = self.session.post(login_url, data=payload, headers=headers)

            if response.status_code in [200, 204]:
                self.jsession_id = self.session.cookies.get('JSESSIONID')
                self.token = self.session.cookies.get('X-Bonita-API-Token')
                return True
            else:
                raise Exception(f"Error de autenticación: {response.status_code}, {response.text}")
        except requests.RequestException as e:
            print(f"No se pudo conectar al servidor de Bonita OS: {e}")
            return False

    def _do_request(self, method, endpoint, params=None, data=None):
        url = f'{self.base_uri}{endpoint}'
        headers = {
            'X-Bonita-API-Token': self.token
        }
        response = self.session.request(method, url, headers=headers, params=params, json=data)
        if response.status_code == 200 or response.status_code == 204:
            return response.json() if response.status_code == 200 else None
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")

    def get_process_id(self, process_name):
        endpoint = f'/API/bpm/process?f=name={process_name}'
        response = self._do_request('GET', endpoint)
        return response[0]['id'] if response else None

    def initiate_process(self, process_id, variables):
        endpoint = f'/API/bpm/process/{process_id}/instantiation'
        data = {'variables': variables}
        response = self._do_request('POST', endpoint, data=data)
        return response

    def get_task_id_by_name(self, task_name, case_id):
        endpoint = f'/API/bpm/task?f=state=ready&f=caseId={case_id}'  # Filtra por caseId
        tasks = self._do_request('GET', endpoint)
        for task in tasks:
            if task['name'] == task_name:
                return task['id']
        return None

    def complete_task(self, task_id):
        endpoint = f'/API/bpm/userTask/{task_id}/execution'
        response = self._do_request('POST', endpoint)
        return response
    
    def set_variable_by_case(self, case_id, variable_name, value, variable_type):
        """Actualiza una variable del caso."""
        endpoint = f'/API/bpm/caseVariable/{case_id}/{variable_name}'
        data = {
            "value": value,
            "type": variable_type
        }
    
        try:
            response = self._do_request('PUT', endpoint, data=data)
            print(f"Respuesta cruda para la variable {variable_name}: {response}")  # Verifica la respuesta
            return response
        except Exception as e:
            print(f"Error al actualizar la variable {variable_name}: {e}")
            raise

