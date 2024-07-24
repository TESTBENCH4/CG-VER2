import json
import requests



def ppt2pdf(f_path,filename, token):

    headers = {"Authorization": token}
    para = {
        "name": filename,
        "parents": ["1btDd35p-mkjLP3h0wSbtjGw8ojq9bf1O"]
        }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open(f_path, "rb")
        }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
        )
    fi = r.text.split()
    st = fi[4]
    st = st[1:-2]
    return st



# import json
# import requests

# def ppt2pdf(f_path, filename, token):
#     headers = {"Authorization": token}
#     para = {
#         "name": filename,
#         "parents": ["1btDd35p-mkjLP3h0wSbtjGw8ojq9bf1O"]
#     }
#     files = {
#         'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
#         'file': open(f_path, "rb")
#     }
#     try:
#         r = requests.post(
#             "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
#             headers=headers,
#             files=files
#         )
#         r.raise_for_status()  # Raises an HTTPError if the response code was unsuccessful
#         fi = r.json()
#         return fi.get('id', '')  # Return the file ID if available
#     except requests.exceptions.RequestException as e:
#         print(f"Request failed: {e}")
#         return ""
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return ""
